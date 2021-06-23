import enum


__all__ = (
    "ARRange",
    "ContentFilter",
    "MediaFilter",
    "CategoryType",
    "GifFormat",
)


class Enum(enum.Enum):
    def __call__(cls, value):
        try:
            return cls._enum_value_map_[value]
        except (KeyError, TypeError):
            raise ValueError(f"{value!r} is not a valid {cls.__name__}")

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


class StrEnum(str, Enum):
    def __str__(self):
        return self.value


class ARRange(StrEnum):
    ALL = "all"
    WIDE = "wide"
    STANDARD = "standard"


class ContentFilter(StrEnum):
    OFF = "off"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class MediaFilter(StrEnum):
    BASIC = "basic"
    MINIMAL = "minimal"


class CategoryType(StrEnum):
    FEATURED = "featured"
    EMOJI = "emoji"
    TRENDING = "trending"


class GifFormat(Enum):
    GIF = "gif"
    MEDIUMGIF = "mediumgif"
    TINYGIF = "tinygif"
    NANOGIF = "nanogif"
    MP4 = "mp4"
    LOOPEDMP4 = "loopedmp4"
    TINYMP4 = "tinymp4"
    NANOMP4 = "nanomp4"
    WEBM = "webm"
    TINYWEBM = "tinywebm"
    NANOWEBM = "nanowebm"
