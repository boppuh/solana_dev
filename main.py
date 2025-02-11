from managers.screened_tokens_manager import ScreenedTokensManager
from utils.solana_utils import SolanaUtils
from utils.printer import PrintingUtils
from clients.telegram_client import TgClient
# from clients.jupiter_client import JupiterClient
from api.bitquery_streamer import subscribe, pull, test_connection
from api.jupiter_network_v2 import get_quote
from api.solscan_networker import SolscanNetworker
from operations.trading_session import TailTradingSession
from datetime import datetime
# from api.bitquery_networker import BitQueryNetworker
import asyncio
import logging
import subprocess
import time
from api.bitquery_streamer import subscribe


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


def pullToken():
    solscan_networker = SolscanNetworker()
    tokens = solscan_networker.getTokensForWalletAddress(
        "3jgub3P9KP3XA9Dwh7XpKu35BiQNTZZXbPmfBAJMsroL")
    print("Tokens: ", tokens)

    for token in tokens:
        print("Getting token price for:", token.address)
        current_price = solscan_networker.getCurrentPriceForToken(
            token.address)
        print(current_price)


def getTransfers():
    solscan_networker = SolscanNetworker()
    transfers = solscan_networker.getTransfers(
        "3jgub3P9KP3XA9Dwh7XpKu35BiQNTZZXbPmfBAJMsroL")
    # print(transfers)
    for transfer in transfers:
        print("Token address: ", transfer.token_address,
              "Block time: ", transfer.block_time,
              "To address: ", transfer.to_address,
              "From address: ", transfer.from_address)


def demoTradingSession():
    print("Kicking off trading session")
    trading_session = TailTradingSession(
        "3jgub3P9KP3XA9Dwh7XpKu35BiQNTZZXbPmfBAJMsroL", SolscanNetworker())
    trading_session.prepare()
    trading_session.start()


def send_mac_notification(title, message, sound="default"):
    script = f'display notification "{message}" with title "{title}" sound name "{sound}"'
    subprocess.run(["osascript", "-e", script])


def testMacNotifications():
    while True:
        send_mac_notification("Hello", "This is a test message", "Glass")
        time.sleep(5)


if __name__ == "__main__":
    # asyncio.run(pull())
    # let jupiterClient = JupiterClient()
    asyncio.run(subscribe())
    # testMacNotifications()
    # demoTradingSession()
    # getTransfers()
    # pullToken()
    # asyncio.run(main())
