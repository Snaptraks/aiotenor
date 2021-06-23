import aiohttp
import asyncio
import json

from . import errors


async def json_or_text(response):
    text = await response.text(encoding="utf-8")
    try:
        if "application/json" in response.headers["Content-Type"]:
            return json.loads(text)
    except KeyError:
        # Thanks Cloudflare
        pass

    return text


class Route:
    BASE = "https://g.tenor.com/v1"

    def __init__(self, path):
        self.url = f"{self.BASE}{path}"


class HTTPClient:
    def __init__(self, api_key):
        self.api_key = api_key
        # self.session = aiohttp.ClientSession()
        self.session = None

    async def request(self, route, parameters=None):
        if parameters is None:
            parameters = {}
        parameters["key"] = self.api_key

        if self.session is None:
            self.session = await self._create_session()

        params = {}
        for k, v in parameters.items():
            if v is not None:
                params[k] = v

        for tries in range(5):
            async with self.session.get(route.url, params=params) as resp:
                data = await json_or_text(resp)

                # print(resp.status)

                if "error" in data and resp.status == 200:
                    raise errors.TenorException(data["error"])

                if 200 <= resp.status < 300:
                    return data

                if resp.status == 404:
                    raise errors.NotFound(data)

                if resp.status == 429:
                    # we are rate limited, wait for 30s
                    await asyncio.sleep(30)
                    continue

                return data

        if resp.status >= 500:
            raise errors.TenorServerError(data)

    async def _create_session(self):
        return aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()

    async def search(self, **parameters):
        return await self.request(Route("/search"),
                                  parameters=parameters)

    async def trending(self, **parameters):
        return await self.request(Route("/trending"),
                                  parameters=parameters)

    async def categories(self, **parameters):
        return await self.request(Route("/categories"),
                                  parameters=parameters)

    async def search_suggestions(self, **parameters):
        return await self.request(Route("/search_suggestions"),
                                  parameters=parameters)

    async def autocomplete(self, **parameters):
        return await self.request(Route("/autocomplete"),
                                  parameters=parameters)

    async def trending_terms(self, **parameters):
        return await self.request(Route("/trending_terms"),
                                  parameters=parameters)

    async def registershare(self, **parameters):
        return await self.request(Route("/registershare"),
                                  parameters=parameters)

    async def gifs(self, **parameters):
        return await self.request(Route("/gifs"),
                                  parameters=parameters)

    async def random(self, **parameters):
        return await self.request(Route("/random"),
                                  parameters=parameters)

    async def anonid(self, **parameters):
        return await self.request(Route("/anonid"),
                                  parameters=parameters)
