from enum import Enum


class UserStatus(Enum):
    CREATED = "CREATED"
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"


class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    CHINESE = "zh"
    JAPANESE = "ja"
    KOREAN = "ko"
    RUSSIAN = "ru"
    ARABIC = "ar"
    PORTUGUESE = "pt"
    HINDI = "hi"
    BENGALI = "bn"
    ITALIAN = "it"
    TURKISH = "tr"
    DUTCH = "nl"
    POLISH = "pl"
    UKRAINIAN = "uk"


class Timezone(Enum):
    UTC = "UTC"
    US_EASTERN = "America/New_York"
    US_CENTRAL = "America/Chicago"
    US_MOUNTAIN = "America/Denver"
    US_PACIFIC = "America/Los_Angeles"

    EUROPE_LONDON = "Europe/London"
    EUROPE_BERLIN = "Europe/Berlin"
    EUROPE_PARIS = "Europe/Paris"

    ASIA_TOKYO = "Asia/Tokyo"
    ASIA_SHANGHAI = "Asia/Shanghai"
    ASIA_KOLKATA = "Asia/Kolkata"

    AUSTRALIA_SYDNEY = "Australia/Sydney"
    SOUTH_AMERICA_SAO_PAULO = "America/Sao_Paulo"
    AFRICA_JOHANNESBURG = "Africa/Johannesburg"
    PACIFIC_AUCKLAND = "Pacific/Auckland"