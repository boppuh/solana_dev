# import base58
# import base64
# import json
# import os

# from solders import message
# from solders.pubkey import Pubkey
# from solders.keypair import Keypair
# from solders.transaction import VersionedTransaction

# from solana.rpc.types import TxOpts
# from solana.rpc.async_api import AsyncClient
# from solana.rpc.commitment import Processed

# from jupiter_python_sdk.jupiter import Jupiter, Jupiter_DCA


# class JupiterClient:

#     # Replace PRIVATE-KEY with your private key as string
#     private_key = Keypair.from_bytes(
#         base58.b58decode(os.getenv("PRIVATE-KEY")))
#     # Replace SOLANA-RPC-ENDPOINT-URL with your Solana RPC Endpoint URL
#     async_client = AsyncClient("SOLANA-RPC-ENDPOINT-URL")
#     jupiter = Jupiter(
#         async_client=async_client,
#         keypair=private_key,
#         quote_api_url="https://quote-api.jup.ag/v6/quote?",
#         swap_api_url="https://quote-api.jup.ag/v6/swap",
#         open_order_api_url="https://jup.ag/api/limit/v1/createOrder",
#         cancel_orders_api_url="https://jup.ag/api/limit/v1/cancelOrders",
#         query_open_orders_api_url="https://jup.ag/api/limit/v1/openOrders?wallet=",
#         query_order_history_api_url="https://jup.ag/api/limit/v1/orderHistory",
#         query_trade_history_api_url="https://jup.ag/api/limit/v1/tradeHistory"
#     )


# """
# EXECUTE A SWAP
# """


# async def test(self):
#     transaction_data = await self.jupiter.swap(
#         input_mint="So11111111111111111111111111111111111111112",
#         output_mint="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
#         amount=5_000_000,
#         slippage_bps=1,
#     )
#     # Returns str: serialized transactions to execute the swap.

#     raw_transaction = VersionedTransaction.from_bytes(
#         base64.b64decode(transaction_data))
#     signature = self.private_key.sign_message(
#         message.to_bytes_versioned(raw_transaction.message))
#     signed_txn = VersionedTransaction.populate(
#         raw_transaction.message, [signature])
#     opts = TxOpts(skip_preflight=False, preflight_commitment=Processed)
#     result = await self.async_client.send_raw_transaction(txn=bytes(signed_txn), opts=opts)
#     transaction_id = json.loads(result.to_json())['result']
#     print(f"Transaction sent: https://explorer.solana.com/tx/{transaction_id}")
