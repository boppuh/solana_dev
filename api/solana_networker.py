"""
This module interacts with the Bitquery API to fetch data from the Solana blockchain.
"""

import requests

from solana_dev.utils.constants import ACCESS_TOKEN, BASE_URL

QUERY = """
query TrendingTokens {
  Solana {
    DEXTradeByTokens(
      limit: { count: 10 }
      orderBy: { descendingByField: "tradesCountWithUniqueTraders" }
    ) {
      Trade {
        Currency {
          Name
          Symbol
          MintAddress
        }
      }
      tradesCountWithUniqueTraders: count(distinct: Transaction_Signer)
    }
  }
}
"""


class SolanaNetworker:
    """
    SolanaNetworker class for interacting with the BitQuery API.
    """

    def fetch_trending_tokens(self):
        """
        Fetches the trending tokens from the BitQuery API.

        Returns:
            dict: A dictionary containing the trending tokens data if the request is successful.

        Raises:
            Exception: If the query fails to run.
        """
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        response = requests.post(
            BASE_URL, json={'query': QUERY}, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()

        return response.raise_for_status()
