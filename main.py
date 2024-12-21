"""
This module demonstrates the usage of the 
TokenNetworker class to fetch top traders from the Bitquery API.
"""

import json

from api.token_networker import TokenNetworker

if __name__ == "__main__":
    TOKEN = "F4Tph9ggvRQ2Yg5pBM8ifai5jHoMVBdYiVmYCBTmpump"
    networker = TokenNetworker(TOKEN)
    data = networker.fetch_top_traders()
    print(json.dumps(data, indent=2))
