from typing import List
from tabulate import tabulate

from models.token import Token


class PrintingUtils:

    @staticmethod
    def print_tokens_table(tokens: List[Token]):
        token_data = [
            {
                "Account": token.account,
                "Address": token.address,
                "Amount": token.amount,
                "Decimals": token.decimals,
            }
            for token in tokens
        ]

        print(tabulate(token_data, headers="keys", tablefmt="grid"))

    @staticmethod
    def print_owners_table(owners: List[Token]):
        owners_data = [
            {
                "Address": owner.address,
                "Amount": owner.amount,
                "Decimals": owner.decimals,
                "Owner": owner.owner,
                "Rank": owner.rank
            }
            for owner in owners
        ]

        print(tabulate(owners_data, headers="keys", tablefmt="grid"))
