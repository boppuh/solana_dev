from managers.screened_tokens_manager import ScreenedTokensManager
from utils.solana_utils import SolanaUtils
from utils.printer import PrintingUtils
from clients.telegram_client import TgClient
from api.solscan_networker import SolscanNetworker
# from api.bitquery_networker import BitQueryNetworker
import asyncio
import logging


class TelegramMessageHandler:
    def __init__(self, screened_tokens_manager):
        self.screened_tokens_manager = screened_tokens_manager

    def handle_new_message(self, message):
        # logging.info("Message content: %s", message)
        addresses = SolanaUtils.find_pump_fun_addresses_in_string(message)
        for address in addresses:
            self.screened_tokens_manager.add_address(address)


async def main():

    solscan_networker = SolscanNetworker()
    printer = PrintingUtils(file_name="tokens.txt")

    # Temp until we get the BitQuery API sorted out
    # bitqueryNetworker = BitQueryNetworker()
    # trending_tokens = bitqueryNetworker.fetch_trending_tokens()
    # print(trending_tokens)

    # result = await bitqueryNetworker.get_pool_addresses()
    # print(result)
    screened_tokens_manager = ScreenedTokensManager(
        solscan_networker=solscan_networker,
        printer=printer)

    logging.basicConfig(filename='solana_dev.log', level=logging.INFO)

    print("Fetching data from Solscan API")

    tg_client = TgClient(
        message_handler=TelegramMessageHandler(screened_tokens_manager))
    await tg_client.connect_client()

    # printer.write("Trending tokens")

    # tokens = solscan_networker.getTrendingTokens()

    # printer.print_trending_tokens_table(tokens=tokens)

    # for token in tokens:
    #     printer.write("Top owners of token: " + token.address)
    #     owners = solscan_networker.getTopOwnersOfToken(token.address)
    #     printer.print_owners_table(owners=owners)

    # WALLET_ADDRESS = "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A"

    # printer.write("Tokens for wallet address: " + WALLET_ADDRESS)

    # tokens = solscan_networker.getTokensForWalletAddress(WALLET_ADDRESS)

    # printer.print_tokens_table(tokens=tokens)

    # printer.close()

    # addresses = []

    # await tg_client.send_message('me', 'Hello once again!')

    # messages = await tg_client.scrape_messages(
    #     entity_name="CryptoBoltzSquad", limit=200)

    # for message in messages:
    #     addresses.extend(
    #         SolanaUtils.find_solana_addresses_in_string(message['text']))

    # for address in addresses:
    #     print(address)


if __name__ == "__main__":
    asyncio.run(main())
