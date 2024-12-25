# from gql import gql
# from gql.transport.websockets import WebsocketsTransport


# async def main():
#     transport = WebsocketsTransport(
#         url="wss://streaming.bitquery.io/eap?token=ory_at_UG26K0pX40J1GwEhIVqXhnkexcJRd1PCA9bp_7pbFJM.26VQ7W1wNprXy5jQVZ318frOaNifaD9meR5SoLp-hS8",
#         headers={"Sec-WebSocket-Protocol": "graphql-ws"})

#     # Use `/eap` instead of `/graphql` if you are using chains on EAP endpoint
#     await transport.connect()
#     print("Connected")

#     # Define the subscription query
#     query = gql("""
#         subscription {
#             Solana {
#                 DEXPools {
#                     Block {
#                         Time
#                     }
#                     Pool {
#                         Base {
#                             ChangeAmount
#                             PostAmount
#                             Price
#                             PriceInUSD
#                         }
#                         Quote {
#                             ChangeAmount
#                             PostAmount
#                             Price
#                             PriceInUSD
#                         }
#                         Dex {
#                             ProgramAddress
#                             ProtocolFamily
#                         }
#                         Market {
#                             BaseCurrency {
#                                 MintAddress
#                                 Name
#                                 Symbol
#                             }
#                             QuoteCurrency {
#                                 MintAddress
#                                 Name
#                                 Symbol
#                             }
#                             MarketAddress
#                         }
#                     }
#                 }
#             }
# }
#     """)

#     async def subscribe_and_print():
#         try:
#             async for result in transport.subscribe(query):
#                 print(result)
#         except asyncio.CancelledError:
#             print("Subscription cancelled.")

#     # Run the subscription and stop after 100 seconds
#     try:
#         await asyncio.wait_for(subscribe_and_print(), timeout=100)
#     except asyncio.TimeoutError:
#         print("Stopping subscription after 100 seconds.")

#     # Close the connection
#     await transport.close()
#     print("Transport closed")
