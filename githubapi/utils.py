import aiohttp
from githubapi import ENDPOINT as endpoint
# response = await client.get(f"{endpoint}{url}")


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{endpoint}{url}') as resp:
            return await resp.json()
