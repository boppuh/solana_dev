POOL_ADDRESSES_QUERY = """
subscription {
  Solana {
    Instructions(
      where: {Transaction: {Result: {Success: true}}, Instruction: {Program: {Method: {is: "initialize2"}, Address: {is: "675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8"}}}}
    ) {
      Block {
        Time
        Date
      }
      Transaction {
        Signature
      }
      Instruction {
        AncestorIndexes
        CallerIndex
        Depth
        Data
        ExternalSeqNumber
        InternalSeqNumber
        Index
        Accounts {
          Address
          IsWritable
          Token {
            Mint
            Owner
            ProgramId
          }
        }
        CallPath
        Logs
        Program {
          AccountNames
          Method
          Json
          Name
          Arguments {
            Type
            Name
          }
        }
      }
    }
  }
}
"""
