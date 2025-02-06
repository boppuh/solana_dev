import asyncio
import websockets
import json

BITQUERY_WS_URL = "wss://streaming.bitquery.io/graphql"
# Replace with your actual Bitquery API key
API_KEY = "ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8"

# GraphQL subscription query
QUERY = """
subscription {
  Solana {
    BalanceUpdates(
      where: { Account: { is: "YourSolanaWalletAddress" } } # Replace with your Solana wallet address
    ) {
      Account
      Currency {
        Symbol
        Mint
        Decimals
      }
      Value
      Transaction {
        Signature
      }
      Block {
        Slot
        Timestamp
      }
    }
  }
}
"""


async def subscribe():
    """Subscribes to real-time Solana balance updates."""
    async with websockets.connect(BITQUERY_WS_URL, extra_headers={"X-API-KEY": API_KEY}) as ws:
        await ws.send(json.dumps({"query": QUERY}))
        while True:
            response = await ws.recv()
            data = json.loads(response)
            print(json.dumps(data, indent=2))  # Pretty-print the response

# Export the subscribe method for external use
