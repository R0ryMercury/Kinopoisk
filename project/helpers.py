import calendar
import datetime
import bcrypt
import jwt
from project.constants import (
    JWT_ALGORITHM,
    JWT_SECRET,
    TOKEN_EXPIRE_DAYS,
    TOKEN_EXPIRE_MINUTES,
)


def get_hashed_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)


def generate_tokens(data):
    minutes = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )
    data["exp"] = calendar.timegm(minutes.timetuple())
    access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    days = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
    data["exp"] = calendar.timegm(days.timetuple())
    refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def check_tokens(tokens):

    try:
        data = jwt.decode(
            tokens["refresh_token"], JWT_SECRET, algorithms=[JWT_ALGORITHM]
        )
    except Exception:
        return False
    return data
