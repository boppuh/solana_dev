from utils.solana_utils import SolanaUtils
from utils.printer import PrintingUtils
from clients.telegram_client import TgClient
from api.solscan_networker import SolscanNetworker
from api.bitquery_networker import BitQueryNetworker
import asyncio

from gql import gql
from gql.transport.websockets import WebsocketsTransport


async def main():
    transport = WebsocketsTransport(
        url="wss://streaming.bitquery.io/eap?token=ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8",
        headers={"Sec-WebSocket-Protocol": "graphql-ws"})

    # Use `/eap` instead of `/graphql` if you are using chains on EAP endpoint
    await transport.connect()
    print("Connected")

    # Define the subscription query
    query = gql("""
        subscription {
            Solana {
                DEXPools {
                    Block {
                        Time
                    }
                    Pool {
                        Base {
                            ChangeAmount
                            PostAmount
                            Price
                            PriceInUSD
                        }
                        Quote {
                            ChangeAmount
                            PostAmount
                            Price
                            PriceInUSD
                        }
                        Dex {
                            ProgramAddress
                            ProtocolFamily
                        }
                        Market {
                            BaseCurrency {
                                MintAddress
                                Name
                                Symbol
                            }
                            QuoteCurrency {
                                MintAddress
                                Name
                                Symbol
                            }
                            MarketAddress
                        }
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


# Run the asyncio event loop
if __name__ == "__main__":
    asyncio.run(main())

# """
# This module demonstrates the usage of the
# TokenNetworker class to fetch top traders from the Bitquery API.
# """


# async def main():

#     bitqueryNetworker = BitQueryNetworker()
#     trending_tokens = bitqueryNetworker.fetch_trending_tokens()
#     print(trending_tokens)

#     result = await bitqueryNetworker.get_pool_addresses()
#     print(result)

#     networker = SolscanNetworker()
#     printer = PrintingUtils(file_name="tokens.txt")
#     tg_client = TgClient()
#     await tg_client.connect_client()

#     printer.write("Trending tokens")

#     tokens = networker.getTrendingTokens()

#     printer.print_trending_tokens_table(tokens=tokens)

#     for token in tokens:
#         printer.write("Top owners of token: " + token.address)
#         owners = networker.getTopOwnersOfToken(token.address)
#         printer.print_owners_table(owners=owners)

#     WALLET_ADDRESS = "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A"

#     printer.write("Tokens for wallet address: " + WALLET_ADDRESS)

#     tokens = networker.getTokensForWalletAddress(WALLET_ADDRESS)

#     printer.print_tokens_table(tokens=tokens)

#     printer.close()

#     addresses = []

#     messages = await tg_client.scrape_messages(
#         entity_name="CryptoBoltzSquad", limit=200)

#     for message in messages:
#         addresses.extend(
#             SolanaUtils.find_solana_addresses_in_string(message['text']))

#     for address in addresses:
#         print(address)


# if __name__ == "__main__":
#     asyncio.run(main())
