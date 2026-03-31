# signNow API Python SDK
## v3.0.0

[![Python Version](https://img.shields.io/badge/codebase-python--3.8+-blue)](https://www.python.org/)

Package metadata and build configuration follow [PEP 517/518](https://peps.python.org/pep-0517/) and live in `pyproject.toml`.

### About SignNow
SignNow is a powerful web-based e-signature solution that streamlines the signing process and overall document flow for businesses of any size. SignNow offers SaaS as well as public and private cloud deployment options using the same underlying API. With SignNow you can easily sign, share and manage documents in compliance with international data laws and industry-specific regulations. SignNow enables you to collect signatures from partners, employees and customers from any device within minutes. For more details, please, visit [SignNow API Reference](https://docs.signnow.com/docs/signnow/welcome).

### Requirements
- Python 3.8+
- pip

### Quick Start

#### Option 1: Local installation

```bash
# 1. Installation
cd python-sdk
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .

# 2. Configuration (create .env file)
cp env.example .env
# Edit .env file: add your credentials and basic token (see details in Credentials section below)

# 3. Run example
python examples/auth_check_example.py
```

#### Option 2: Docker (recommended)

```bash
# 1. Configuration
cd python-sdk
cp env.example .env
# Edit .env file: add your credentials and basic token (see details in Credentials section below)

# 2. Build and run
docker-compose build
docker-compose up -d signnow-sdk
docker-compose exec signnow-sdk bash

# 3. Inside the container
python examples/auth_check_example.py
```

### Installation

#### From source
```bash
git clone https://github.com/signnow/PythonSdk.git
cd python-sdk
pip install -r requirements.txt
pip install -e .
```

#### Using pip (when published)
```bash
pip install signnow-python-sdk
```

### Configuration

Copy `env.example` to `.env` and fill in your credentials:

```bash
cp env.example .env
```

Then edit `.env` with your credentials:

```bash
SIGNNOW_API_HOST=https://api.signnow.com
SIGNNOW_API_BASIC_TOKEN=your_basic_token
SIGNNOW_API_USERNAME=your_username
SIGNNOW_API_PASSWORD=your_password
SIGNNOW_DOWNLOADS_DIR=./downloads
```

Alternatively, you can set these as environment variables.

### Credentials
To run examples or use the SDK in your project, you will need API keys. Follow these steps to obtain them:

1. Register for an account on SignNow [here](https://www.signnow.com/api)
2. Create a new application.
3. Obtain the Basic Authentication API token for your application.
4. Add your email, password, and the Basic token to the .env file.

Now, you are ready to use the SDK.

### Code quality
CI runs [Black](https://github.com/psf/black) (format check) and [Flake8](https://flake8.pycqa.org/) (lint) on push/PR. Run locally:

```bash
pip install -e ".[dev]"
make format   # format code with Black
make lint     # check format and run Flake8
```

### Run tests

#### Quick start
```bash
# Install dev dependencies once
pip install -r requirements.txt
pip install -e ".[dev]"

# Run all the tests
pytest tests/ -v
# or
make test

# Run with coverage report
pytest tests/ --cov=signnow --cov-report=html --cov-report=term
# or
make test-cov
```

#### Docker (recommended)
```bash
make docker-test          # all tests in Docker
make docker-test-cov      # with coverage
```

> **Note:** Tests do not require a `.env` file — they use mocked HTTP responses.
> Only the `examples/` scripts require real credentials.

See `make help` for the full list of available targets.

### Error Handling

All SDK errors are raised as `SignNowApiException`. The exception carries structured
context you can inspect:

```python
from signnow.core.exception import SignNowApiException

try:
    response = client.send(request).get_response()
except SignNowApiException as e:
    print(e)                  # human-readable summary
    print(e.endpoint)         # e.g. "POST /oauth2/token"
    print(e.response_code)    # e.g. 401
    print(e.response)         # raw response body (str)
    print(e.payload)          # request body that was sent
    print(e.cause)            # underlying exception, if any
```

Common status codes:

| Code | Meaning | Typical cause |
|------|---------|---------------|
| 401  | Unauthorized | Invalid or expired token / wrong Basic token |
| 403  | Forbidden | Insufficient permissions for the resource |
| 404  | Not Found | Wrong document/template/group ID |
| 422  | Unprocessable | Validation error (missing fields, bad values) |

### Usage

#### Basic Authentication Example
```python
from signnow.api.user.request import UserGetRequest
from signnow.api.user.response import UserGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

try:
    # Create a new instance of the API client containing a freshly created bearer token
    client: ApiClient = SdkFactory.create_api_client()
    
    # Get user information
    request = UserGetRequest()
    response: UserGetResponse = client.send(request).get_response()
    
    print(f"User ID: {response.id}")
    print(f"User name: {response.first_name} {response.last_name}")
except SignNowApiException as e:
    print(f"ERROR: {e}")
```

#### Using an Existing Bearer Token
```python
from signnow.api.user.request import UserGetRequest
from signnow.api.user.response import UserGetResponse
from signnow.core.api_client import ApiClient
from signnow.core.exception import SignNowApiException
from signnow.core.factory import SdkFactory

try:
    # Create a new instance without authentication
    client: ApiClient = SdkFactory.create_api_client_with_bearer_token("your_bearer_token")
    
    # Get user information
    request = UserGetRequest()
    response: UserGetResponse = client.send(request).get_response()
    
    print(f"User ID: {response.id}")
    print(f"User name: {response.first_name} {response.last_name}")
except SignNowApiException as e:
    print(f"ERROR: {e}")
```

#### Using the SDK Class Directly
```python
from signnow.api.document.request import DocumentGetRequest
from signnow.api.document.response import DocumentGetResponse
from signnow.core.exception import SignNowApiException
from signnow.sdk import Sdk

try:
    # Create SDK instance
    sdk = Sdk()
    client = sdk.build().authenticate().get_api_client()
    
    # Get document
    request = DocumentGetRequest()
    request.with_document_id("your_document_id")
    response: DocumentGetResponse = client.send(request).get_response()
    
    print(f"Document ID: {response.id}")
    print(f"Document Name: {response.document_name}")
except SignNowApiException as e:
    print(f"ERROR: {e}")
```

### Examples
You can find more examples of API usage in the [examples](./examples) directory.
You may also want to check [examples/preset_data.py](./examples/preset_data.py) and fill in your document IDs, template IDs, etc. before running them.
If you already have a bearer token (e.g. from running [auth_check_example.py](./examples/auth_check_example.py)), you can save it as `PRESET_BEARER_TOKEN` in [preset_data.py](./examples/preset_data.py) so other examples reuse it automatically.

### Project Structure
```
python-sdk/
├── signnow/
│   ├── __init__.py
│   ├── sdk.py                 # Main SDK class
│   ├── core/                  # Core modules
│   │   ├── api_client.py      # HTTP client for API requests
│   │   ├── config.py          # Configuration management
│   │   ├── exception.py       # Custom exceptions
│   │   ├── factory.py         # SDK factory
│   │   ├── request.py         # Request interface and decorators
│   │   ├── response.py        # Response parser
│   │   ├── token.py           # Token classes
│   │   └── collection/        # Typed collection utilities
│   └── api/                   # API modules
│       ├── auth/              # OAuth2 authentication
│       ├── document/          # Document CRUD, download, merge
│       ├── documentfield/     # Prefill text fields
│       ├── documentgroup/     # Document groups
│       ├── documentgroupinvite/ # Group invite management
│       ├── documentgrouptemplate/ # Group templates
│       ├── documentinvite/    # Field & free-form invites, signing links
│       ├── embeddededitor/    # Embedded editor links
│       ├── embeddedgroupinvite/ # Embedded group invites
│       ├── embeddedinvite/    # Embedded signing invites
│       ├── embeddedsending/   # Embedded sending links
│       ├── folder/            # Folder operations
│       ├── proxy/             # Proxy file/JSON responses
│       ├── smartfields/       # Smart field prefill
│       ├── template/          # Templates, routing, bulk invite
│       ├── user/              # User management
│       ├── webhook/           # Webhook subscriptions (v1)
│       └── webhookv2/         # Event subscriptions (v2)
├── examples/                  # Runnable usage examples
├── tests/                     # Unit tests
├── pyproject.toml             # Build config & dev dependencies
├── Makefile                   # Dev/test workflow targets
├── Dockerfile                 # Container image
├── docker-compose.yml         # Docker services
└── README.md
```

### Features
- ✅ Modern Python 3.8+ syntax with type hints
- ✅ Dataclasses for request/response models
- ✅ Decorator-based API endpoint definition
- ✅ Automatic authentication & token refresh
- ✅ Environment variable and file-based configuration
- ✅ Structured error handling via `SignNowApiException`
- ✅ Streaming file downloads (constant memory usage)
- ✅ Document groups & group invites
- ✅ Embedded editor, signing & sending links
- ✅ Webhook subscriptions (v1 & v2)
- ✅ Smart fields & template routing
- ✅ Bulk invite via CSV
- ✅ Docker-based development workflow
- ✅ Full unit test suite

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing
Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.
