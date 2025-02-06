import base58
import base64
import json

from solders import message
from solders.pubkey import Pubkey
from solders.keypair import Keypair
from solders.transaction import VersionedTransaction

from solana.rpc.types import TxOpts
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Processed

from jupiter_python_sdk.jupiter import Jupiter, Jupiter_DCA

# Replace PRIVATE-KEY with your private key as string
private_key = Keypair.from_bytes(base58.b58decode(os.getenv("PRIVATE-KEY")))
# Replace SOLANA-RPC-ENDPOINT-URL with your Solana RPC Endpoint URL
async_client = AsyncClient("SOLANA-RPC-ENDPOINT-URL")
jupiter = Jupiter(
    async_client=async_client,
    keypair=private_key,
    quote_api_url="https://quote-api.jup.ag/v6/quote?",
    swap_api_url="https://quote-api.jup.ag/v6/swap",
    open_order_api_url="https://jup.ag/api/limit/v1/createOrder",
    cancel_orders_api_url="https://jup.ag/api/limit/v1/cancelOrders",
    query_open_orders_api_url="https://jup.ag/api/limit/v1/openOrders?wallet=",
    query_order_history_api_url="https://jup.ag/api/limit/v1/orderHistory",
    query_trade_history_api_url="https://jup.ag/api/limit/v1/tradeHistory"
)
