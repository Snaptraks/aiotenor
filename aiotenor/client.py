from .http import HTTPClient
from .response import Gif, Category


class Tenor:
    def __init__(
        self,
        *,
        api_key,
    ):
        self.http = HTTPClient(api_key)

    async def close(self):
        await self.http.close()

    async def search(
        self,
        query,
        *,
        anon_id=None,
        ar_range=None,
        contentfilter=None,
        limit=None,
        locale=None,
        media_filter=None,
        pos=None,
    ):
        response = await self.http.search(
            q=query,
            anon_id=anon_id,
            ar_range=ar_range,
            contentfilter=contentfilter,
            limit=limit,
            locale=locale,
            media_filter=media_filter,
            pos=pos,
        )
        return response["next"], [Gif(gif) for gif in response["results"]]

    async def trending(
        self,
        *,
        anon_id=None,
        ar_range=None,
        contentfilter=None,
        limit=None,
        locale=None,
        media_filter=None,
        pos=None,
    ):
        response = await self.http.trending(
            anon_id=anon_id,
            ar_range=ar_range,
            contentfilter=contentfilter,
            limit=limit,
            locale=locale,
            media_filter=media_filter,
            pos=pos,
        )
        return response["next"], [Gif(gif) for gif in response["results"]]

    async def categories(
        self,
        *,
        anon_id=None,
        contentfilter=None,
        locale=None,
        type=None,
    ):
        response = await self.http.categories(
            anon_id=anon_id,
            contentfilter=contentfilter,
            locale=locale,
            type=type,
        )
        return [Category(category) for category in response["tags"]]

    async def search_suggestions(
        self,
        query,
        *,
        anon_id=None,
        limit=None,
        locale=None,
    ):
        response = await self.http.search_suggestions(
            q=query,
            anon_id=anon_id,
            limit=limit,
            locale=locale,
        )
        return response["results"]

    async def autocomplete(
        self,
        query,
        *,
        anon_id=None,
        limit=None,
        locale=None,
    ):
        response = await self.http.autocomplete(
            q=query,
            anon_id=anon_id,
            limit=limit,
            locale=locale,
        )
        return response["results"]

    async def trending_terms(
        self,
        *,
        anon_id=None,
        limit=None,
        locale=None,
    ):
        response = await self.http.trending_terms(
            anon_id=anon_id,
            limit=limit,
            locale=locale,
        )
        return response["results"]

    async def registershare(
        self,
        id,
        *,
        anon_id=None,
        locale=None,
        query=None,
    ):
        response = await self.http.registershare(
            id=id,
            anon_id=anon_id,
            locale=locale,
            q=query,
        )
        return response["status"]

    async def gifs(
        self,
        ids,
        *,
        anon_id=None,
        limit=None,
        media_filter=None,
        pos=None,
    ):
        response = await self.http.gifs(
            ids=ids,
            anon_id=anon_id,
            limit=limit,
            media_filter=media_filter,
            pos=pos,
        )
        return response["next"], [Gif(gif) for gif in response["results"]]

    async def random(
        self,
        query,
        *,
        anon_id=None,
        ar_range=None,
        contentfilter=None,
        limit=None,
        locale=None,
        media_filter=None,
        pos=None,
    ):
        response = await self.http.random(
            q=query,
            anon_id=anon_id,
            ar_range=ar_range,
            contentfilter=contentfilter,
            limit=limit,
            locale=locale,
            media_filter=media_filter,
            pos=pos,
        )
        return response["next"], [Gif(gif) for gif in response["results"]]

    async def anonid(
        self,
    ):
        response = await self.http.anonid()
        return response["anon_id"]
