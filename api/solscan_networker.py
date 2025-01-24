import json

from api.base_networker import BaseNetworker
from models.owner import Owner
from models.token import Token
from models.transfer import Transfer
from utils.constants import SOLSCAN_BASE_URL
from datetime import datetime

HEADERS = {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3MzQ5MTU1NTcxNjUsImVtYWlsIjoicm1hdGh0cmFkaW5nQGdtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImFwaVZlcnNpb24iOiJ2MiIsImlhdCI6MTczNDkxNTU1N30.UmkCER3DAtMR2HPn535Dw9CHz6N1e1gAKjZG2wxh3GM"}


class SolscanNetworker:
    def __init__(self):
        self.base_networker = BaseNetworker(SOLSCAN_BASE_URL)

    def getTrendingTokens(self, limit: int = 10):
        params = {
            "limit": limit
        }
        try:
            response = self.base_networker.get(
                "token/trending", params=params, headers=HEADERS)
            tokens_response = json.loads(json.dumps(response["data"]))
            tokens = [Token.from_trending_dict(
                token) for token in tokens_response]
            return tokens
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def getTokensForWalletAddress(self,
                                  address: str,
                                  page: int = 1,
                                  page_size: int = 10):

        params = {
            "address": address,
            "type": "token",
            "page": page,
            "page_size": page_size
        }

        try:

            print(f"Fetching tokens for wallet address: {address}")

            response = self.base_networker.get(
                "account/token-accounts", params=params, headers=HEADERS)

            tokens_response = json.loads(json.dumps(response["data"]))
            tokens = [Token.from_dict(token) for token in tokens_response]

            token_metadata = response["metadata"]["tokens"]
            for token in tokens:
                token_metadata_info = token_metadata.get(token.address, {})
                token.set_name(token_metadata_info.get("name", ""))
                token.set_symbol(token_metadata_info.get("symbol", ""))

            return tokens

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def getTopOwnersOfToken(self,
                            token: str,
                            page: int = 1,
                            page_size: int = 10,
                            from_amount: str = "",
                            to_amount: str = ""):
        params = {
            "address": token,
            "page": page,
            "page_size": page_size
        }

        if from_amount:
            params["from_amount"] = from_amount
        if to_amount:
            params["to_amount"] = to_amount

        try:

            print(f"Fetching top owners of token: {token}")

            response = self.base_networker.get(
                "token/holders", params=params, headers=HEADERS)

            # print("Response: ", response)

            response_data = json.loads(json.dumps(response["data"]["items"]))

            # print("Response data: ", response_data)

            owners = [Owner.from_dict(owner) for owner in response_data]

            # print("Owners: ", owners)

            return owners

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def getCurrentPriceForToken(self, address: str):

        # Get the current date
        current_date = datetime.now()

        # Format the date as YYYYMMDD
        formatted_date = current_date.strftime('%Y%m%d')

        params = {
            "address": address
            # "date": [formatted_date]
        }

        try:
            response = self.base_networker.get(
                "token/price", params=params, headers=HEADERS)

            print("Response: ", response)
            return response

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def getTransfers(self, address: str, page_size: int):
        params = {
            "address": address,
            "page_size": page_size
        }
        try:
            response = self.base_networker.get(
                "account/transfer", params=params, headers=HEADERS)
            # print(response)
            transfers = [Transfer.from_dict(transfer)
                         for transfer in response["data"]]
            return transfers
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
