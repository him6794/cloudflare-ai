# Cloudflare AI Python Package

This package provides a simple and comprehensive way to interact with Cloudflare Workers AI from Python.

## Installation

Install the package using pip:

```bash
pip install .
```

Or from a local directory:

```bash
pip install -e .
```

## Usage

### Initialize the Client

```python
from cloudflare_ai import CloudflareAI

# Replace with your actual values
account_id = "your_account_id"
api_token = "your_api_token"

client = CloudflareAI(account_id, api_token)
```

### List Available Models

```python
models = client.list_models()
for model in models['result']:
    print(f"Model: {model['name']}, Description: {model.get('description', 'N/A')}")
```

### Run a Model

```python
response = client.run_model("@cf/meta/llama-3.1-8b-instruct", "Where did the phrase Hello World come from")
print(response['result']['response'])
```

### Backward Compatibility

For backward compatibility, you can still use the old function:

```python
from cloudflare_ai import call_cloudflare_ai

response = call_cloudflare_ai(account_id, api_token, "@cf/meta/llama-3.1-8b-instruct", "Hello World")
```

## API Reference

### CloudflareAI Class

- `__init__(account_id, api_token)`: Initialize the client.
- `list_models()`: Returns a list of available models with detailed information.
- `run_model(model, prompt, **kwargs)`: Run a specific model with a prompt and optional parameters.

### Parameters

- `account_id`: Your Cloudflare Account ID
- `api_token`: Your Cloudflare API Token
- `model`: The model identifier (e.g., "@cf/meta/llama-3.1-8b-instruct")
- `prompt`: The text prompt to send to the model
- `**kwargs`: Additional parameters like max_tokens, temperature, etc.

## Getting Your API Credentials

1. Go to the [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/ai/workers-ai)
2. Select "Use REST API"
3. Click "Create a Workers AI API Token"
4. Review the prefilled information and select "Create API Token"
5. Copy the API Token and Account ID

**Important**: Ensure your API token has the following permissions:
- Workers AI - Read
- Workers AI - Edit

If you get a 401 Unauthorized error, your token may be invalid or expired. Create a new one following the steps above.

## Development

### Setting up PyPI Publishing

To automatically publish to PyPI when pushing to main branch:

1. Create a PyPI account at https://pypi.org/
2. Generate an API token from your PyPI account settings
3. Add the token as a repository secret named `PYPI_API_TOKEN` in your GitHub repository settings

### Running Tests Locally

```bash
pip install -e .[dev]
pytest
```

### Code Quality

```bash
flake8 cloudflare_ai
```