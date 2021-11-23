import jwt
from jwt.exceptions import DecodeError

from models import User

SECRET_KEY = "some_generated_secret_key"
ALGORITHM = "HS256"


def create_access_token(login_: str, pwd: str):
    return jwt.encode(
        {"login": login_, "password": pwd}, SECRET_KEY, algorithm=ALGORITHM
    )


def verify_token(encoded_jwt: str):
    try:
        decoded_jwt = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=[ALGORITHM])
        login_ = decoded_jwt.get("login")
        pwd = decoded_jwt.get("password")
        user = User.query.filter_by(login=login_, password=pwd).first()
        if user is not None:
            return True
        raise DecodeError
    except DecodeError:
        return False
