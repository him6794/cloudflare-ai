#!/usr/bin/env python3
"""
Example usage of the cfai package.
Replace with your actual account_id and api_token.
"""

import requests
from cloudflare_ai_python import CloudflareAI

# Replace with your actual values
account_id = "your_account_id"
api_token = "your_api_token"

def main():
    client = CloudflareAI(account_id, api_token)

    # List models
    print("Listing available models:")
    try:
        models_response = client.list_models()
        if 'result' in models_response:
            for model in models_response['result'][:5]:  # Show first 5
                print(f"- {model.get('name', 'Unknown')}: {model.get('description', 'No description')[:100]}...")
        else:
            print("No models found or error in response.")
    except Exception as e:
        print(f"Error listing models: {e}")

    # Run a model
    print("\nRunning a model:")
    try:
        response = client.run_model("@cf/meta/llama-3.1-8b-instruct", "Say hello in one word.")
        if 'result' in response and 'response' in response['result']:
            print(f"Response: {response['result']['response']}")
        else:
            print("Unexpected response format.")
            print(response)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("Error: Unauthorized. Please check your API token and ensure it has the correct permissions (Workers AI - Read and Edit).")
            print("Get a new token from: https://dash.cloudflare.com/?to=/:account/ai/workers-ai")
        elif e.response.status_code == 403:
            print("Error: Forbidden. Your account may not have access to Workers AI.")
        else:
            print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"Error running model: {e}")

if __name__ == "__main__":
    main()