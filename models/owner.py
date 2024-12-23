from dataclasses import dataclass


@dataclass
class Owner:
    rank: int
    address: str
    amount: int
    decimals: int
    owner: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            rank=data["rank"],
            address=data["address"],
            amount=data["amount"],
            decimals=data["decimals"],
            owner=data["owner"],
        )

    @classmethod
    def __repr__(self):
        return (f"Owner(rank={self.rank}, address='{self.address}', amount={self.amount}, "
                f"decimals={self.decimals}, owner='{self.owner}')")
