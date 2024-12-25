TRENDING_TOKENS_QUERY = """
query TrendingTokens {
  Solana {
    DEXTradeByTokens(
      limit: { count: 10 }
      orderBy: { descendingByField: "tradesCountWithUniqueTraders" }
    ) {
      Trade {
        Currency {
          Name
          Symbol
          MintAddress
        }
      }
      tradesCountWithUniqueTraders: count(distinct: Transaction_Signer)
    }
  }
}
"""
