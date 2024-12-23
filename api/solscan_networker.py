import json

from api.base_networker import BaseNetworker
from models.owner import Owner
from models.token import Token
from utils.constants import SOLSCAN_BASE_URL

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
            print(response)
            tokens_response = json.loads(json.dumps(response["data"]))
            print(tokens_response)
            tokens = [Token.from_dict(token) for token in tokens_response]
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

            response = self.base_networker.get(
                "token/holders", params=params, headers=HEADERS)
            response_data = json.loads(json.dumps(response["data"]["items"]))
            owners = [Owner.from_dict(owner) for owner in response_data]

            return owners

        except Exception as e:
            print(f"An error occurred: {e}")
            return None
