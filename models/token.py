from dataclasses import dataclass
from typing import Optional


@dataclass
class Token:
    account: str
    address: str
    amount: int
    decimals: int
    owner: str
    name: Optional[str] = None
    symbol: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            account=data["token_account"],
            address=data["token_address"],
            amount=data["amount"],
            decimals=data["token_decimals"],
            owner=data["owner"]
        )

    def set_name(self, name: str):
        self.name = name

    def set_symbol(self, symbol: str):
        self.symbol = symbol
