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
        self.file.write(text + "\n")
        if add_new_line:
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

        self.write(tabulate(owners_data, headers="keys", tablefmt="grid"))
