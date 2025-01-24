import time

SOLANA_ADDRESS_1 = "So11111111111111111111111111111111111111111"
SOLANA_ADDRESS_2 = "So11111111111111111111111111111111111111112"


class TailTradingSession:
    def __init__(self, wallet_address, solscan_networker):
        self.wallet_address = wallet_address
        self.solscan_networker = solscan_networker
        self.cached_token_addresses = set([])
        self.trades = set([])  # Need an object for open trade (or just trade)
        print("Initializing trading session")
        # self.trades = []

    def prepare(self):
        print("Preparing trading session")
        transfers = self.solscan_networker.getTransfers(
            self.wallet_address, 100)
        for transfer in transfers:
            if not transfer.token_address in self.cached_token_addresses and transfer.token_address != SOLANA_ADDRESS_1 and transfer.token_address != SOLANA_ADDRESS_2 and transfer.to_address == self.wallet_address:
                print("Caching token: ", transfer.token_address)
                self.cached_token_addresses.add(transfer.token_address)

    # TODO: If we want to have a stop loss, we'll have to stream the coin prices and check if the price is below a certain threshold
    def start(self):
        while True:
            print("Checking for new coins")
            transfers = self.solscan_networker.getTransfers(
                self.wallet_address, 10)
            for transfer in transfers:
                if not transfer.token_address in self.cached_token_addresses and transfer.token_address != SOLANA_ADDRESS_1 and transfer.token_address != SOLANA_ADDRESS_2 and transfer.to_address == self.wallet_address:
                    print("BUY THE COIN")
                    self.cached_token_addresses.add(
                        transfer.token_address)  # Do we need this
                    self.trades.add(transfer.token_address)
                elif transfer.token_address in self.cached_token_addresses and transfer.token_address in self.trades and transfer.to_address == self.wallet_address:
                    print("ADD TO POSITION")
                elif transfer.token_address in self.cached_token_addresses and transfer.token_address in self.trades and transfer.from_address == self.wallet_address:
                    print("SELL THE COIN")
                    self.trades.remove(transfer.token_address)

            time.sleep(5)
