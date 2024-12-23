"""
This module demonstrates the usage of the
TokenNetworker class to fetch top traders from the Bitquery API.
"""

import json

from utils.printer import PrintingUtils
from models.owner import Owner
from models.token import Token
from api.solscan_networker import SolscanNetworker

if __name__ == "__main__":

    networker = SolscanNetworker()
    json_data = networker.getTokensForWalletAddress(
        "4yCqEknZEJwPngkAaX4F2peVUGGhWB82kwBKK7LHGg1A")
    data_str = json.dumps(json_data["data"])
    data_dict = json.loads(data_str)

    tokens = [Token.from_dict(token) for token in data_dict]
    token_metadata = json_data["metadata"]["tokens"]
    for token in tokens:
        token_metadata_info = token_metadata.get(token.address, {})
        token.set_name(token_metadata_info.get("name", ""))
        token.set_symbol(token_metadata_info.get("symbol", ""))

    PrintingUtils.print_tokens_table(tokens=tokens)

    holder_json_data = networker.getTopHoldersForToken(
        "B8q1emW1dKLerpaiLi9n4ZVSCMLaDZUe8T6mPekPpump")
    holders_data_items = json.dumps(holder_json_data["data"]["items"])
    holders_data = json.loads(holders_data_items)

    holders = [Owner.from_dict(holder)
               for holder in holders_data]

    PrintingUtils.print_owners_table(owners=holders)
