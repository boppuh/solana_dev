"""
This module interacts with the Bitquery API to fetch top traders on the Solana blockchain.
"""

import requests

from solana_dev.utils.constants import ACCESS_TOKEN, BASE_TOKEN

# Define the URL for the API endpoint
URL = "https://streaming.bitquery.io/eap"

# Define the GraphQL query and variables
QUERY = """
query TopTraders($token: String, $base: String) {
    Solana {
        DEXTradeByTokens(
            orderBy: {descendingByField: "volumeUsd"}
            limit: {count: 100}
            where: {
                Trade: {
                    Currency: {MintAddress: {is: $token}},
                    Side: {Amount: {gt: "0"}, Currency: {MintAddress: {is: $base}}}
                },
                Transaction: {Result: {Success: true}}
            }
        ) {
            Trade {
                Account {
                    Owner
                }
                Dex {
                    ProgramAddress
                    ProtocolFamily
                    ProtocolName
                }
            }
            bought: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: buy}}}})
            sold: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: sell}}}})
            volume: sum(of: Trade_Amount)
            volumeUsd: sum(of: Trade_Side_AmountInUSD)
        }
    }
}
"""


class TokenNetworker:
    """
    A class to interact with the Bitquery API for a specific token.

    Attributes:
        token (str): The token mint address.
    """

    def __init__(self, token: str):
        """
        Initializes the TokenNetworker with the given token.

        Args:
            token (str): The token mint address.
        """
        self.token = token

    def fetch_top_traders(self):
        """
        Fetches the top traders from the Bitquery API for the given token and base.

        Args:
            base (str): The base mint address.

        Returns:
            dict: The response data from the Bitquery API.

        Raises:
            Exception: If the query fails to run.
        """
        variables = {
            "token": self.token,
            "base": BASE_TOKEN
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        response = requests.post(
            URL, json={'query': QUERY, 'variables': variables}, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()

        return response.raise_for_status()
