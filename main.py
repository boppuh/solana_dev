"""
This module demonstrates the usage of the
TokenNetworker class to fetch top traders from the Bitquery API.
"""

from api.solscan_networker import SolscanNetworker
from clients.telegram_client import TgClient
from utils.printer import PrintingUtils
from utils.solana_utils import SolanaUtils

import asyncio


async def main():
    networker = SolscanNetworker()
    printer = PrintingUtils(file_name="tokens.txt")
    tg_client = TgClient()
    await tg_client.connect_client()

    printer.write("Trending tokens")

    tokens = networker.getTrendingTokens()

    printer.print_trending_tokens_table(tokens=tokens)

    for token in tokens:
        printer.write("Top owners of token: " + token.address)
        owners = networker.getTopOwnersOfToken(token.address)
        printer.print_owners_table(owners=owners)

    WALLET_ADDRESS = "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A"

    printer.write("Tokens for wallet address: " + WALLET_ADDRESS)

    tokens = networker.getTokensForWalletAddress(WALLET_ADDRESS)

    printer.print_tokens_table(tokens=tokens)

    printer.close()

    addresses = []

    messages = await tg_client.scrape_messages(
        entity_name="CryptoBoltzSquad", limit=200)

    for message in messages:
        addresses.extend(
            SolanaUtils.find_solana_addresses_in_string(message['text']))

    for address in addresses:
        print(address)


if __name__ == "__main__":
    asyncio.run(main())
