from pydantic import BaseSettings


class DevSettings(BaseSettings):
    algorithm: str
    secret_key: str
    database_port: str
    database_name: str
    database_hostname: str
    database_password: str
    database_username: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env-dev"


dev_settings = DevSettings()