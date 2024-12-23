from api.base_networker import BaseNetworker
from utils.constants import SOLSCAN_BASE_URL

HEADERS = {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3MzQ5MTU1NTcxNjUsImVtYWlsIjoicm1hdGh0cmFkaW5nQGdtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImFwaVZlcnNpb24iOiJ2MiIsImlhdCI6MTczNDkxNTU1N30.UmkCER3DAtMR2HPn535Dw9CHz6N1e1gAKjZG2wxh3GM"}


class SolscanNetworker:
    def __init__(self):
        self.base_networker = BaseNetworker(SOLSCAN_BASE_URL)

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
            return self.base_networker.get(
                "account/token-accounts", params=params, headers=HEADERS)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def getTopHoldersForToken(self,
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
            return self.base_networker.get(
                "token/holders", params=params, headers=HEADERS)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
