from dataclasses import dataclass


@dataclass
class Transfer:
    block_id: int
    trans_id: str
    block_time: int
    time: str
    activity_type: str
    from_address: str
    from_token_account: str
    to_address: str
    to_token_account: str
    token_address: str
    token_decimals: int
    amount: int
    flow: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            block_id=data["block_id"],
            trans_id=data["trans_id"],
            block_time=data["block_time"],
            time=data["time"],
            activity_type=data["activity_type"],
            from_address=data["from_address"],
            from_token_account=data["from_token_account"],
            to_address=data["to_address"],
            to_token_account=data["to_token_account"],
            token_address=data["token_address"],
            token_decimals=data["token_decimals"],
            amount=data["amount"],
            flow=data["flow"]
        )

    def __repr__(self):
        return (f"Transfer(block_id='{self.block_id}', trans_id='{self.trans_id}', block_time={self.block_time}, "
                f"time={self.time}, activity_type='{self.activity_type}', from_address='{self.from_address}', from_token_account='{self.from_token_account}, "
                f"to_address='{self.to_address}', to_token_account='{self.to_token_account}', token_address='{self.token_address}', token_decimals={self.token_decimals}, "
                f"amount={self.amount}, flow={self.flow}")
