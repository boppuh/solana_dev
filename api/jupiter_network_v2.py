import requests
import json


def get_quote():
    print("get_uote()")
    url = "https://api.jup.ag/swap/v1/quote"
    params = {
        "inputMint": "So11111111111111111111111111111111111111112",
        "outputMint": "G98W2gqXzKXcAp4vGPYEYQDC3hkRaPcTqK24n8BSpump",
        "amount": 10000000,
        "slippageBps": 50,
        "restrictIntermediateTokens": True
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        quote_response = response.json()
        print(json.dumps(quote_response, indent=2))
    else:
        print(
            f"Failed to retrieve quote. Status code: {response.status_code}, with reason: {response.raw}")


def get_quote_v2():
    url = "https://api.jup.ag/swap/v1/swap"
    headers = {
        "Content-Type": "application/json",
        # Add API key if required
        # "x-api-key": "YOUR_API_KEY"
    }
    data = {
        "quoteResponse": quote_response,
        "userPublicKey": public_key,
        "dynamicComputeUnitLimit": True,
        "dynamicSlippage": True,
        "prioritizationFeeLamports": {
            "priorityLevelWithMaxLamports": {
                "maxLamports": 1000000,
                "priorityLevel": "veryHigh"
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to retrieve swap response. Status code: {response.status_code}")
        return None


# Usage:
# quote_response =  # Your quote response object
# public_key =  # Your public key string

swap_response = swap(quote_response, public_key)
print(swap_response)

get_quote_v2()
