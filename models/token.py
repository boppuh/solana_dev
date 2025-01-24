from dataclasses import dataclass
from typing import Optional


@dataclass
class Token:
    address: str
    decimals: int
    owner: Optional[str] = None
    amount: Optional[int] = None
    account: Optional[str] = None
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

    @classmethod
    def from_trending_dict(cls, data: dict):
        return cls(
            address=data["address"],
            decimals=data["decimals"],
            name=data["name"],
            symbol=data["symbol"],
        )

    def __repr__(self):
        return (f"Token(account='{self.account}', address='{self.address}', amount={self.amount}, "
                f"decimals={self.decimals}, owner='{self.owner}', name='{self.name}', symbol='{self.symbol}')")

    def set_name(self, name: str):
        self.name = name

    def set_symbol(self, symbol: str):
        self.symbol = symbol
