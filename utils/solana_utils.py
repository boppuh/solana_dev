import base58
import re


class SolanaUtils:

    @staticmethod
    def is_valid_solana_address(address):
        # Check if the length is 44
        if len(address) != 44:
            return False

        # Validate base58 encoding
        try:
            decoded = base58.b58decode(address)
            encoded = base58.b58encode(decoded).decode('utf-8')
            if encoded != address:
                return False
        except ValueError:
            return False

        return True

    @staticmethod
    def find_solana_addresses_in_string(input_string):
        # Ensure the input is a valid string
        if not isinstance(input_string, str):
            return []

        # Regular expression to match all 44-character substrings
        matches = re.findall(r'[A-HJ-NP-Za-km-z1-9]{44}', input_string)

        # Validate each match
        valid_addresses = [
            match for match in matches if SolanaUtils.is_valid_solana_address(match)]

        return valid_addresses
