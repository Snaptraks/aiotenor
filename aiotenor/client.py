import enum

import aiohttp


class ContentFilter(enum.Enum):
    OFF = "off"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Tenor:
    def __init__(
        self,
        *,
        api_key,
    ):
        self.api_key = api_key
        self.session = aiohttp.ClientSession()

    async def request(self, route):
        async with self.session.get(route.url) as resp:
            print(resp)

    def search(
        self,
        query,
        *,
        anon_id=None,
        ar_range="all",
        contentfilter=ContentFilter.OFF,
        limit=20,
        locale="en_US",
        media_filter=None,
        pos=None,
    ):
        pass

    def trending(
        self,
        *,
        anon_id=None,
        ar_range="all",
        contentfilter=ContentFilter.OFF,
        limit=20,
        locale="en_US",
        media_filter=None,
        pos=None,
    ):
        pass
