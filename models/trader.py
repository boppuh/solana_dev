#!/usr/bin/env python3

"""
This module defines the Trader class, which represents a trader on a decentralized exchange (DEX).
"""

class Trader:
    """
    Represents a trader on a decentralized exchange (DEX).

    Attributes:
        owner (str): The owner of the trader account.
        dex_name (str): The name of the decentralized exchange.
        bought (float): The amount bought by the trader.
        sold (float): The amount sold by the trader.
        volume (float): The trading volume.
        volume_usd (float): The trading volume in USD.
    """
    def __init__(
        self,
        owner: str,
        dex_name: str,
        bought: float,
        sold: float,
        volume: float,
        volume_usd: float,
    ):
        self.owner = owner
        self.dex_name = dex_name
        self.bought = bought
        self.sold = sold
        self.volume = volume
        self.volume_usd = volume_usd

    def __repr__(self):
        return (
            f"Trader(owner='{self.owner}', dex_name='{self.dex_name}', "
            f"bought={self.bought}, sold={self.sold}, "
            f"volume={self.volume}, volume_usd={self.volume_usd})"
        )
