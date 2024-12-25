import asyncio
import aiohttp
import logging
import requests

from api.queries.PoolAddressesQuery import POOL_ADDRESSES_QUERY
from api.queries.TrendingTokensQuery import TRENDING_TOKENS_QUERY
from utils.constants import ACCESS_TOKEN, BITQUERY_BASE_URL, BITQUERY_STREAMING_URL


class BitQueryNetworker:
    def __init__(self):
        pass

    def get(self, query: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        response = requests.post(
            BITQUERY_BASE_URL, json={'query': query}, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()

        return response.raise_for_status()

    def fetch_trending_tokens(self):
        return self.get(TRENDING_TOKENS_QUERY)

    async def get_pool_addresses(self):
        headers = {
            "Sec-WebSocket-Protocol": "graphql-ws",
            "Content-Type": "application/json"
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(BITQUERY_STREAMING_URL, json={'query': POOL_ADDRESSES_QUERY}, headers=headers) as response:
                    response.raise_for_status()
                    data = await response.json()
                    instructions = data.get("data", {}).get(
                        "Solana", {}).get("Instructions", [])
                    if not instructions:
                        return {"poolAddress": "", "tokenA": "", "tokenB": ""}
                    instruction = instructions[0]
                    accounts = instruction.get(
                        "Instruction", {}).get("Accounts", [])
                    pool_address = accounts[4].get(
                        "Address") if len(accounts) > 4 else None
                    token_a = accounts[8].get("Address") if len(
                        accounts) > 8 else None
                    token_b = accounts[9].get("Address") if len(
                        accounts) > 9 else None
                    return {"poolAddress": pool_address, "tokenA": token_a, "tokenB": token_b}
        except aiohttp.ClientError as e:
            logging.error(f"Error fetching data: {e}")
            return {"poolAddress": "", "tokenA": "", "tokenB": ""}
