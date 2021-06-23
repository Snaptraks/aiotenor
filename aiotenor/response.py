from .enums import GifFormat

__all__ = (
    "Gif",
    "Category",
    "Media",
)


def parse_media(data):
    return {GifFormat(k): Media(v, k) for k, v in data.items()}


class Gif:
    def __init__(self, data):
        self.created = data.get("created")
        self.hasaudio = data.get("hasaudio")
        self.hascaption = data.get("hascaption")
        self.id = data.get("id")
        self.itemurl = data.get("itemurl")
        media = data.get("media")
        if media is not None:
            # can media be more than len == 1?
            self.media = parse_media(media[0])
        self.tags = data.get("tags")
        self.title = data.get("title")
        self.url = data.get("url")

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} url={self.url}>"

    @property
    def gif_url(self):
        return self.media[GifFormat.GIF].url

    @property
    def mp4_url(self):
        return self.media[GifFormat.MP4].url


class Category:
    def __init__(self, data):
        self.character = data.get("character")
        self.image = data.get("image")
        self.name = data.get("name")
        self.path = data.get("path")
        self.searchterm = data.get("searchterm")

    def __repr__(self):
        return f"<{self.__class__.__name__} name={self.name}>"


class Media:
    def __init__(self, data, format):
        self.dims = data.get("dims")
        self.duration = data.get("duration")
        self.format = GifFormat(format)
        self.preview = data.get("preview")
        self.size = data.get("size")
        self.url = data.get("url")

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} url={self.url}"
            f" format={repr(self.format)}>"
        )
