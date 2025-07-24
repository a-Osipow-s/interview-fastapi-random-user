import jwt

from datetime import datetime, timedelta

from api.core.config import settings

from api.enums.cache import CACHE_PREFIXES

def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.now()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    return jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm
    )

def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    return jwt.decode(
        token,
        public_key,
        algorithms=[algorithm]
    )

def get_token_ttl(exp: int) -> float:
    exp_datetime: datetime = datetime.fromtimestamp(exp)
    return (exp_datetime - datetime.now()).total_seconds()

def build_blacklist_token_key(token: str) -> str:
    return f'{CACHE_PREFIXES.TOKEN_BLACKLIST}: {token}'