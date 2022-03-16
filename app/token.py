from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas

# to get a string like this, run:
# openssl rand -hex 32
SECRET_KEY = "82c0754b7ffefa28dfeacd2fd191eb1884b4329ab17e314235b330c276aab8c7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError as e:
        raise credentials_exception from e
