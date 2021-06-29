import asyncio

import unittest

import aiotenor
import config


LIMIT = 10


class TenorTest(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.client = aiotenor.Tenor(api_key=config.api_key)

    async def asyncTearDown(self):
        await self.client.close()
        await asyncio.sleep(0.5)  # silence asyncio errors

    async def test_001_route(self):
        route = aiotenor.http.Route("/search")
        self.assertEqual(route.url, f"{aiotenor.http.Route.BASE}/search")

    async def test_002_client_instanciation(self):
        self.assertIsInstance(self.client, aiotenor.Tenor)

    async def test_003_tenor_search_for_one(self):
        next_, results = await self.client.search(
            "sea of thieves fishing",
            limit=1,
            ar_range=aiotenor.ARRange.WIDE,
            contentfilter=aiotenor.ContentFilter.LOW,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )
        self.assertLessEqual(len(results), 1)
        self.assertIsNotNone(results[0].url)
        self.assertIsInstance(results[0].gif_url, str)
        self.assertIsInstance(results[0].mp4_url, str)

    async def test_004_tenor_search_for_many(self):
        next_, results = await self.client.search(
            "sea of theives",
            limit=LIMIT,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )
        self.assertLessEqual(len(results), LIMIT)
        for g in results:
            self.assertIsInstance(g, aiotenor.Gif)

    async def test_005_tenor_trending(self):
        next_, results = await self.client.trending(
            limit=LIMIT,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )
        self.assertLessEqual(len(results), LIMIT)
        for g in results:
            self.assertIsInstance(g, aiotenor.Gif)

    async def test_006_tenor_categories(self):
        categories = await self.client.categories(
            type=aiotenor.CategoryType.FEATURED,
            contentfilter=aiotenor.ContentFilter.HIGH,
        )
        for c in categories:
            self.assertIsInstance(c, aiotenor.Category)

    async def test_007_tenor_search_suggestions(self):
        results = await self.client.search_suggestions(
            "happy",
            limit=LIMIT,
        )
        self.assertLessEqual(len(results), LIMIT)
        for sug in results:
            self.assertIsInstance(sug, str)

    async def test_008_tenor_autocomplete(self):
        results = await self.client.autocomplete(
            "hap",
            limit=LIMIT,
        )
        self.assertLessEqual(len(results), LIMIT)
        for sug in results:
            self.assertIsInstance(sug, str)

    async def test_009_tenor_trending_terms(self):
        results = await self.client.trending_terms(
            limit=LIMIT,
        )
        self.assertLessEqual(len(results), LIMIT)
        for term in results:
            self.assertIsInstance(term, str)

    async def test_010_tenor_registershare(self):
        query = "sea of thieves"
        next_, results = await self.client.search(
            query,
            limit=1,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )

        status = await self.client.registershare(
            id=results[0].id,
            query=query,
        )
        self.assertEqual(status, "ok")

        with self.assertRaises(aiotenor.errors.TenorException):
            status = await self.client.registershare(
                id="some fake id",
            )

    async def test_011_tenor_gifs(self):
        next_, results = await self.client.search(
            "sea of thieves",
            limit=LIMIT,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )
        ids = [g.id for g in results]

        next_, results = await self.client.gifs(
            ids,
            media_filter=aiotenor.MediaFilter.MINIMAL,
        )

        self.assertLessEqual(len(results), LIMIT)
        for g in results:
            self.assertIsInstance(g, aiotenor.Gif)
            self.assertIn(g.id, ids)

    async def test_012_tenor_random(self):
        next_, results = await self.client.random(
            "sea of thieves",
            limit=LIMIT,
        )
        self.assertLessEqual(len(results), LIMIT)
        for g in results:
            self.assertIsInstance(g, aiotenor.Gif)

    async def test_013_tenor_anonid(self):
        anon_id = await self.client.anonid()
        self.assertIsInstance(anon_id, str)

    async def test_014_tenor_gifs_wrong_id(self):
        with self.assertRaises(aiotenor.errors.TenorException):
            next_, results = await self.client.gifs(
                ["some fake id"],
                media_filter=aiotenor.MediaFilter.MINIMAL,
            )


if __name__ == '__main__':
    unittest.main()
