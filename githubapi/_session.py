import httpx
from githubapi import ENDPOINT as endpoint

async def make_request(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{endpoint}{url}")
        return response.json()
