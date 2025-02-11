import asyncio
from gql import Client, gql
from gql.transport.websockets import WebsocketsTransport

BITQUERY_WS_URL = "wss://streaming.bitquery.io/eap"
# Replace with your actual Bitquery API key
API_KEY = "ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8"

# GraphQL subscription query
QUERY = """
subscription {
  Solana {
    BalanceUpdates(
      # Replace with your Solana wallet address
      where: { Account: { is: "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A" } }
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


async def example():
    transport = WebsocketsTransport(
        url="wss://streaming.bitquery.io/graphql?token=ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8",
        headers={"Sec-WebSocket-Protocol": "graphql-ws"}
    )

    # Use `/eap` instead of `/graphql` if you are using chains on EAP endpoint
    await transport.connect()
    print("Connected")

    # Define the subscription query
    query = gql("""
    subscription MyQuery {
      EVM(network: eth) {
        count: Blocks {
          Block {
            TxCount
          }
        }
      }
    }
  """)

    async def subscribe_and_print():
        try:
            async for result in transport.subscribe(query):
                print(result)
        except asyncio.CancelledError:
            print("Subscription cancelled.")

    # Run the subscription and stop after 100 seconds
    try:
        await asyncio.wait_for(subscribe_and_print(), timeout=100)
    except asyncio.TimeoutError:
        print("Stopping subscription after 100 seconds.")

    # Close the connection
    await transport.close()
    print("Transport closed")
