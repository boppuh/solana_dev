"""
This module demonstrates the usage of the
TokenNetworker class to fetch top traders from the Bitquery API.
"""

from api.solscan_networker import SolscanNetworker
from utils.printer import PrintingUtils

if __name__ == "__main__":

    networker = SolscanNetworker()

    tokens = networker.getTokensForWalletAddress(
        "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A")

    PrintingUtils.print_tokens_table(tokens=tokens)

    owners = networker.getTopOwnersOfToken(
        "B8q1emW1dKLerpaiLi9n4ZVSCMLaDZUe8T6mPekPpump")

    PrintingUtils.print_owners_table(owners=owners)
