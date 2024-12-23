"""
This module demonstrates the usage of the
TokenNetworker class to fetch top traders from the Bitquery API.
"""

from api.solscan_networker import SolscanNetworker
from utils.printer import PrintingUtils

if __name__ == "__main__":

    networker = SolscanNetworker()
    printer = PrintingUtils(file_name="tokens.txt")

    printer.write("Trending tokens")

    tokens = networker.getTrendingTokens()

    printer.print_tokens_table(tokens=tokens)

    WALLET_ADDRESS = "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A"

    printer.write("Tokens for wallet address: " + WALLET_ADDRESS)

    tokens = networker.getTokensForWalletAddress(WALLET_ADDRESS)

    printer.print_tokens_table(tokens=tokens)

    TOKEN_ADDRESS = "B8q1emW1dKLerpaiLi9n4ZVSCMLaDZUe8T6mPekPpump"

    printer.write("Top owners of token: " + TOKEN_ADDRESS)

    owners = networker.getTopOwnersOfToken(TOKEN_ADDRESS)

    printer.print_owners_table(owners=owners)

    printer.close()
