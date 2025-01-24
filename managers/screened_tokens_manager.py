from api.solscan_networker import SolscanNetworker
from utils.printer import PrintingUtils


class ScreenedTokensManager:
    def __init__(self,
                 solscan_networker: SolscanNetworker,
                 printer: PrintingUtils):
        self.solscan_networker = solscan_networker
        self.printer = printer

        self.addresses = set([])
        self.tokens = set([])

    def add_address(self, address: str):
        print(f"Adding address: {address}")
        self.addresses.add(address)
        owners = self.solscan_networker.getTopOwnersOfToken(address)
        self.printer.write("Top owners of token: " + address)
        self.printer.print_owners_table(owners=owners)
        for owner in owners:
            tokens = self.solscan_networker.getTokensForWalletAddress(
                owner.owner)
            self.printer.write("Tokens for wallet address: " + owner.owner)
            self.printer.print_tokens_table(tokens=tokens)
