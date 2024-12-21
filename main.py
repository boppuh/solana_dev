"""
This module demonstrates the usage of the 
TokenNetworker class to fetch top traders from the Bitquery API.
"""

import json

from api.solana_networker import SolanaNetworker
from api.token_networker import TokenNetworker

if __name__ == "__main__":

    solana_networker = SolanaNetworker()
    data = solana_networker.fetch_trending_tokens()
    print(json.dumps(data, indent=2))

    TOKEN = "F4Tph9ggvRQ2Yg5pBM8ifai5jHoMVBdYiVmYCBTmpump"
    token_networker = TokenNetworker(TOKEN)
    data = token_networker.fetch_top_traders()
    print(json.dumps(data, indent=2))
