# Contributing to signNow Python SDK

Thank you for your interest in contributing! This guide will help you get started.

## Prerequisites

- Python 3.8+
- pip
- Docker & docker-compose (optional, recommended)

## What we welcome

We welcome contributions in these areas:

- bug fixes
- documentation improvements
- tests
- performance improvements with evidence
- better error handling
- API consistency improvements
- support for new upstream API features
- refactoring that reduces maintenance burden without changing behavior

We are more cautious about:

- breaking public API changes
- large stylistic rewrites
- new dependencies
- “helper” abstractions that hide important API behavior
- speculative features that the upstream API does not support

The reason is simple: SDK users usually value **stability and clarity** more than novelty.

## Development workflow

### 1. Create a branch

```bash
git checkout -b your-feature-branch
```

### 2. Make changes

All SDK source lives under `signnow/`. Each API domain is a sub-package under
`signnow/api/` with `request/` and `response/` directories.

### 3. Format & lint

```bash
make lint      # check formatting + Flake8
make format    # auto-format with Black
```

### 4. Run tests

```bash
make test          # all unit tests
make test-cov      # with coverage report (htmlcov/)
make test-api      # only mock-API integration tests
```

Or run the full CI check in one command:

```bash
make check         # lint + typecheck + tests
```

Tests do **not** require a `.env` file — they use mocked HTTP responses.

### 5. Docker (optional)

```bash
make docker-build
make docker-test
```

## Project conventions

### Code style

- **Formatter:** [Black](https://github.com/psf/black) with default 88-char line length.
- **Linter:** [Flake8](https://flake8.pycqa.org/) (E203/W503/E501 ignored).
- **Type hints:** Use them on all public APIs. Run `make typecheck` (mypy) to verify.

### Naming

| Item | Convention | Example |
|------|-----------|---------|
| Request class | `{Entity}{Method}Request` | `DocumentPostRequest` |
| Response class | `{Entity}{Method}Response` | `DocumentPostResponse` |
| Request file | `{entity}_{method}_request.py` | `document_post_request.py` |
| Response file | `{entity}_{method}_response.py` | `document_post_response.py` |
| Test file | `test_{domain}.py` | `test_document.py` |

### Request/response pattern

Every API endpoint is a pair of request + response classes:

```python
# signnow/api/example/request/thing_get_request.py
from signnow.core.request import RequestInterface, api_endpoint

@api_endpoint(
    name="getThing",
    url="/thing/{thing_id}",
    method="get",
    auth="bearer",
    namespace="example",
    entity="thing",
)
class ThingGetRequest(RequestInterface):
    def __init__(self):
        self._uri_params = {}

    def with_thing_id(self, thing_id: str) -> "ThingGetRequest":
        self._uri_params["thing_id"] = thing_id
        return self

    def uri_params(self):
        return dict(self._uri_params)

    def payload(self):
        return {}
```

### Tests

- One test file per API domain in `tests/api/`.
- Test request creation, response structure, and mock API calls.
- Use the `mock_api_client` fixture from `conftest.py` for API-call tests.

## Submitting a pull request

1. Ensure `make check` passes.
2. Write or update tests for your changes.
3. Keep commits focused — one logical change per commit.
4. Open a PR against `master` with a clear description.

## Reporting issues

Open an issue on GitHub with:
- Minimal reproduction steps
- Full traceback if applicable
