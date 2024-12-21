#!/usr/bin/env python3

import requests
import json

url = "https://streaming.bitquery.io/eap"

payload = json.dumps(
    {
        "query": 'query TopTraders($token: String, $base: String) {\n  Solana {\n    DEXTradeByTokens(\n      orderBy: {descendingByField: "volumeUsd"}\n      limit: {count: 10}\n      where: {Trade: {Currency: {MintAddress: {is: $token}}, Side: {Amount: {gt: "0"}, Currency: {MintAddress: {is: $base}}}}, Transaction: {Result: {Success: true}}}\n    ) {\n      Trade {\n        Account {\n          Owner\n        }\n        Dex {\n          ProgramAddress\n          ProtocolFamily\n          ProtocolName\n        }\n      }\n      bought: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: buy}}}})\n      sold: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: sell}}}})\n      volume: sum(of: Trade_Amount)\n      volumeUsd: sum(of: Trade_Side_AmountInUSD)\n    }\n  }\n}\n',
        "variables": '{\n  "token": "F4Tph9ggvRQ2Yg5pBM8ifai5jHoMVBdYiVmYCBTmpump",\n  "base": "So11111111111111111111111111111111111111112"\n}',
    }
)
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ory_at_2aYyvWLjd1KPRv89UmMDyBaOnYkZaJN8adbII9q3A8s.CaqgR897nCYC_GpOZOiCdoFUkSSazhrMyAsT7Jhco9U",
}

response = requests.request("POST", url, headers=headers, data=payload)
jsonResponse = response.json()

trades = jsonResponse["data"]["Solana"]["DEXTradeByTokens"]

traders = []
for trade in trades:
    owner = trade["Trade"]["Account"]["Owner"]
    dex_name = trade["Trade"]["Dex"]["ProtocolName"]
    bought = float(trade["bought"])
    sold = float(trade["sold"])
    volume = float(trade["volume"])
    volume_usd = float(trade["volumeUsd"])


pretty_json = json.dumps(trades, indent=4)
print(pretty_json)

# print(response.text)

# import json
# import requests
# from utils.api_key import api_key

# BITQUERY_API_KEY = api_key
# BITQUERY_ENDPOINT = "https://graphql.bitquery.io"


# def get_top_solana_token_holders(token, base, limit=10):
#     query = """
#     query TopTraders($token: String, $base: String) {
#         Solana {
#             DEXTradeByTokens(
#                 orderBy: {descendingByField: "volumeUsd"}
#                 limit: {count: 100}
#                 where: {
#                     Trade: {
#                     Currency: {MintAddress: {is: $token}},
#                     Side: {Amount: {gt: "0"}, Currency: {MintAddress: {is: $base}}}
#                     },
#                     Transaction: {Result: {Success: true}}
#                 }
#             ) {
#             Trade {
#                 Account {
#                     Owner
#                 }
#                 Dex {
#                     ProgramAddress
#                     ProtocolFamily
#                     ProtocolName
#                 }
#             }
#                 bought: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: buy}}}})
#                 sold: sum(of: Trade_Amount, if: {Trade: {Side: {Type: {is: sell}}}})
#                 volume: sum(of: Trade_Amount)
#                 volumeUsd: sum(of: Trade_Side_AmountInUSD)
#             }
#         }
#     }
#     """
#     variables = {
#     "token": token,
#     "base": base
#     }
#     # Prepare the payload
#     payload = json.dumps({
#         "query": query,
#         "variables": variables
#     })

#     # variables = {"token": token, "base": base, "limit": limit}

#     headers = {"Content-Type": "application/json", "X-API-KEY": BITQUERY_API_KEY}

#     response = requests.post(BITQUERY_ENDPOINT, headers=headers, data=payload)

#     # response = requests.post(
#     #     BITQUERY_ENDPOINT,
#     #     json={"query": query, "variables": variables},
#     #     headers=headers,
#     # )

#     # Raise an error if the request was not successful
#     response.raise_for_status()

#     data = response.json()
#     # Check if there are any errors returned from the GraphQL endpoint
#     if "errors" in data:
#         raise Exception(data["errors"])

#     # Extract the top holders from the response
#     tokens = data.get("data", {}).get("solana", {}).get("tokens", [])
#     if not tokens:
#         return []
#     return tokens[0].get("tokenHolders", [])


# # Example usage:
# mint_address = "F4Tph9ggvRQ2Yg5pBM8ifai5jHoMVBdYiVmYCBTmpump"  # Replace with the token's mint address
# base = "So11111111111111111111111111111111111111112"
# top_holders = get_top_solana_token_holders(mint_address, base=base)
# for holder in top_holders:
#     print(f"Address: {holder['holder']['address']}, Amount: {holder['amount']}")
