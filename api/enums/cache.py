from enum import Enum


class CACHE_PREFIXES(Enum):
    TOKEN_BLACKLIST = 'token_blacklist'


class TOKEN_BLACKLIST_VALUES(Enum):
    FALSE = 'false'
    TRUE = 'true'