import asyncio
import requests
import websockets
import json

import websockets.client

BITQUERY_WS_URL = "wss://streaming.bitquery.io/eap"
# Replace with your actual Bitquery API key
API_KEY = "ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8"

# GraphQL subscription query
QUERY = """
subscription {
  Solana {
    BalanceUpdates(
      where: { Account: { is: "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A" } } # Replace with your Solana wallet address
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


async def pull():
    url = "https://streaming.bitquery.io/graphql"
    response = requests.get(url, headers={"X-API-KEY": API_KEY})

    print(response.status_code)  # Should be 200 if the key is valid
    # Should contain information about the account's balance updates
    print(response.text)


async def subscribe():
    """Subscribes to real-time Solana balance updates."""
    async with websockets.client.connect(BITQUERY_WS_URL, extra_headers={"X-API-KEY": API_KEY}) as ws:
        print("HERE - 1")
        await ws.send(json.dumps({"query": QUERY}))
        print("HERE - 2")
        while True:
            print("HERE - 3")
            response = await ws.recv()
            data = json.loads(response)
            print(json.dumps(data, indent=2))  # Pretty-print the response


async def test_connection():
    try:
        async with websockets.client.connect("wss://streaming.bitquery.io/eap") as ws:
            print("✅ Successfully connected to Bitquery WebSocket!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

# Export the subscribe method for external use
