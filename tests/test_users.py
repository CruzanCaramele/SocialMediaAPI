import pytest
from app import schemas
from .database import client, session


def test_create_user(client):
    res = client.post("/users/", json={"email": "zeemann@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "zeemann@gmail.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    assert res.status_code == 200