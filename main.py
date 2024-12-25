from utils.solana_utils import SolanaUtils
from utils.printer import PrintingUtils
from clients.telegram_client import TgClient
from api.solscan_networker import SolscanNetworker
from api.bitquery_networker import BitQueryNetworker
import asyncio
import logging


class MessageHandler:
    def handle_new_message(self, message):
        logging.info("Message content: %s", message)


async def main():

    # Temp until we get the BitQuery API sorted out
    # bitqueryNetworker = BitQueryNetworker()
    # trending_tokens = bitqueryNetworker.fetch_trending_tokens()
    # print(trending_tokens)

    # result = await bitqueryNetworker.get_pool_addresses()
    # print(result)

    logging.basicConfig(filename='solana_dev.log', level=logging.INFO)

    print("Fetching data from Solscan API")

    networker = SolscanNetworker()
    printer = PrintingUtils(file_name="tokens.txt")
    tg_client = TgClient(message_handler=MessageHandler())
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

    await tg_client.send_message('me', 'Hello once again!')

    messages = await tg_client.scrape_messages(
        entity_name="CryptoBoltzSquad", limit=200)

    for message in messages:
        addresses.extend(
            SolanaUtils.find_solana_addresses_in_string(message['text']))

    for address in addresses:
        print(address)


if __name__ == "__main__":
    asyncio.run(main())
