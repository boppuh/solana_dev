

from base_networker import BaseNetworker
from solana_dev.utils.constants import SOLSCAN_BASE_URL

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "_ga=GA1.1.1234011513.1733638900; _ga_PS3V7B7KV0=GS1.1.1734801227.6.0.1734801227.0.0.0; cf_clearance=PQqrbgg1qB5jFFG9Q3g1uSNkpEQOb7sH3Zhnw51BG6g-1734801230-1.2.1.1-mF16SJBRvUGhmkemL9HscOopA8yE91rY2aYdFBoxO2P.RV.MbeZhL5y1jwGMCk8ZsAUj.HdYRrmXh2JZSRu8ZHM0Z_Ju3GsQcWoBn2D669beEEl_dJNrymqR_jUjmEsFFms0VudNMkau_VGORZETS1dtIV5wa7wuTjS9TE._AzMsj8r8bCLIBFYCplGrd5WRnTJmVgVJwJwujPXjPHLgJ8Fw8_vesusTU1.aMg_bGnZ5LgDnRQiBZw3V1sMtuFLchzTarjw7NGFuONUyCjwpGhsoi11HPI.BKk9TFLd3FRPHM3fT.RDozwMMhGuAdfoNw_G0YND5kCkZITISC3CyAtj38vA7ncup5p4M_q0urpE_twgpJwfSSyWLWQrv67FepPLHNzRHfhS8LTJG...y6RgRW4rBwxLKik3iNYRov4CSsTKDTJHP6nB5BLi6L8tRUXS6.Q7jebrTGKYlbKNMiQ",
    "if-none-match": 'W/"1a53-allhQdrcg5wnXQFR7e43q0WT4ac"',
    "origin": "https://solscan.io",
    "priority": "u=1, i",
    "referer": "https://solscan.io/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sol-aut": "FB9dls0fK42nN-t2=HLWZRhI0CrO71s8VfOT-V-=",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}


class SolscanNetworker:
    def __init__(self):
        self.base_networker = BaseNetworker(SOLSCAN_BASE_URL)

    def getTokensForWalletAddress(self, address: str):
        params = {
            "address": address
        }
        try:
            return self.base_networker.get(
                "account/tokens", params=params, headers=HEADERS)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
