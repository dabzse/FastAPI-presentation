from passlib.context import CryptContext


passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class MakeHash():
    def bcrypt(password: str):
        return passwd_context.hash(password)

    def verify(hashed_passwd, plain_passwd):
        return passwd_context.verify(plain_passwd, hashed_passwd)
