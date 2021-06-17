from urllib.parse import quote

import aiohttp


class Route:
    BASE = "https://g.tenor.com/v1"

    def __init__(self, path, **parameters):
        self.path = path
        url = f"{self.BASE}{self.path}"
        if parameters:
            url = url.format_map({k: quote(v) if isinstance(
                v, str) else v for k, v in parameters.items()})
        self.url = url


class HTTPClient:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def request(self, route):
        async with self.session.get(route.url) as resp:
            print(resp)
