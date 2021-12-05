from .. database import get_db
from typing import List, Optional
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from starlette.responses import Response
from sqlalchemy.sql.functions import mode, user, func
from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT


router = APIRouter(
    tags = ["posts"],
    prefix="/posts"
)


# @router.get("/", response_model=List[schemas.PostResponse], status_code=HTTP_200_OK)
@router.get("/", response_model=List[schemas.PostOut] , status_code=HTTP_200_OK)
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, search: Optional[str] = ""):

    """Retrieve limited posts based on search"""
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
                       models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
                       models.Post.id).filter(models.Post.title.contains(search)).limit(limit).all()
    
    
    return posts


@router.post("/", response_model=schemas.PostResponse, status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), 
                 current_user: int = Depends(oauth2.get_current_user)):

    """Make a new post by dictionary"""
    new_post = models.Post(owner_id=current_user.id ,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return  new_post


@router.get("/{id}", response_model=schemas.PostOut, status_code=HTTP_200_OK)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    """Filter post by ID"""
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
                    models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
                    models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"post with {id} was not found")

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    """Get the post to be deleted"""
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()


    "Check if post exists"
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    "Check if post belongs to logged in user"
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")
    
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)


@router.put("/{id}", status_code=HTTP_201_CREATED, response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):

    """ Retrieve post to be edited from Database"""
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    "Check if post exists"
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    post_query.update(updated_post.dict(), synchronize_session=False)

    "Check if post belongs to logged in user"
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    db.commit()
    return  post_query.first()
