from typing import List
from tabulate import tabulate

from models.token import Token


class PrintingUtils:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(file_name, "w", encoding="utf-8")

    def close(self):
        self.file.close()

    def write(self, text, add_new_line=True):
        print(text + "\n")
        self.file.write(text + "\n")
        if add_new_line:
            print("\n")
            self.file.write("\n")

    def print_tokens_table(self, tokens: List[Token]):
        token_data = [
            {
                "Account": token.account,
                "Address": token.address,
                "Amount": token.amount,
                "Decimals": token.decimals,
            }
            for token in tokens
        ]

        # print(tabulate(token_data, headers="keys", tablefmt="grid"))
        self.write(tabulate(token_data, headers="keys", tablefmt="grid"))

    def print_trending_tokens_table(self, tokens: List[Token]):
        token_data = [
            {
                "Symbol": token.symbol,
                "Name": token.name,
                "Address": token.address,
            }
            for token in tokens
        ]

        # print(tabulate(token_data, headers="keys", tablefmt="grid"))
        self.write(tabulate(token_data, headers="keys", tablefmt="grid"))

    def print_owners_table(self, owners: List[Token]):
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

        # print(tabulate(owners_data, headers="keys", tablefmt="grid"))
        self.write(tabulate(owners_data, headers="keys", tablefmt="grid"))
