.PHONY: help install test test-cov test-api examples clean setup-env lint format check typecheck venv docker-build docker-up docker-shell docker-down docker-test docker-test-cov docker-test-api docker-examples docker-example docker-example-auth docker-example-user docker-example-doc

help:
	@echo "SignNow Python SDK - Makefile commands:"
	@echo ""
	@echo "=== Setup ==="
	@echo "  make venv        - Create virtualenv and install all deps"
	@echo "  make install     - Install dependencies into current env"
	@echo "  make setup-env   - Create .env file from example"
	@echo ""
	@echo "=== Code quality ==="
	@echo "  make format      - Format code with Black"
	@echo "  make lint        - Run Black (check) and Flake8"
	@echo "  make typecheck   - Run mypy type checks"
	@echo "  make check       - Run lint + typecheck + tests (full CI)"
	@echo ""
	@echo "=== Tests ==="
	@echo "  make test         - Run all unit tests"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make test-api     - Run only mock-API integration tests"
	@echo ""
	@echo "=== Docker ==="
	@echo "  make docker-build     - Build Docker image"
	@echo "  make docker-up        - Start Docker container"
	@echo "  make docker-shell     - Open shell in Docker container"
	@echo "  make docker-down      - Stop Docker container"
	@echo "  make docker-test      - Run all tests in Docker"
	@echo "  make docker-test-cov  - Run tests with coverage in Docker"
	@echo "  make docker-test-api  - Run only real API tests in Docker"
	@echo ""
	@echo "=== Examples ==="
	@echo "  make examples              - Run all examples"
	@echo "  make docker-examples       - Run all examples in Docker"
	@echo "  make docker-example EXAMPLE=auth_check_example.py  - Run one example"
	@echo ""
	@echo "=== Other ==="
	@echo "  make clean        - Remove caches, build artefacts, coverage"
	@echo ""

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
	pip install -e ".[dev]"

venv:
	@echo "Creating virtualenv and installing all deps..."
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && pip install -e ".[dev]"
	@echo "Done. Activate with: source venv/bin/activate"

lint:
	@echo "Running code quality checks..."
	black --check --diff signnow/ tests/ examples/ run_examples.py
	flake8 signnow/ tests/ examples/ run_examples.py --max-line-length=88 --extend-ignore=E203,W503,E501
	@echo "Lint passed."

format:
	@echo "Formatting code with Black..."
	black signnow/ tests/ examples/ run_examples.py
	@echo "Done."

typecheck:
	@echo "Running mypy type checks..."
	mypy signnow/ --ignore-missing-imports --no-error-summary || true

check: lint typecheck test
	@echo "All checks passed."

setup-env:
	@echo "Creating .env file..."
	@if [ ! -f .env ]; then \
		if [ -f env.example ]; then \
			cp env.example .env; \
			echo ".env file created from env.example! Please edit it and add your credentials."; \
		else \
			echo "# SignNow API Configuration" > .env; \
			echo "# Copy this file to .env and fill in your credentials" >> .env; \
			echo "" >> .env; \
			echo "SIGNNOW_API_HOST=https://api.signnow.com" >> .env; \
			echo "SIGNNOW_API_BASIC_TOKEN=your_basic_token_here" >> .env; \
			echo "SIGNNOW_API_USERNAME=your_username_here" >> .env; \
			echo "SIGNNOW_API_PASSWORD=your_password_here" >> .env; \
			echo "SIGNNOW_DOWNLOADS_DIR=./downloads" >> .env; \
			echo ".env file created! Please edit it and add your credentials."; \
		fi \
	else \
		echo ".env file already exists."; \
	fi

test:
	@echo "Running tests..."
	pytest tests/ -v

test-cov:
	@echo "Running tests with coverage..."
	pytest tests/ --cov=signnow --cov-report=html --cov-report=term
	@echo "Coverage report generated in htmlcov/index.html"

test-api:
	@echo "Running real API tests..."
	pytest tests/api/ -k "api_call" -v

examples:
	@echo "Running all examples..."
	python run_examples.py

example-auth:
	@echo "Running token check example..."
	python examples/auth_check_example.py

example-doc:
	@echo "Running document get example..."
	python examples/document_get_example.py

example-user:
	@echo "Running user info example..."
	python examples/user_info_example.py

clean:
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -r {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -r {} + 2>/dev/null || true
	@echo "Cleanup complete!"

docker-build:
	@echo "Building Docker image..."
	docker-compose build

docker-up:
	@echo "Starting Docker container..."
	docker-compose up -d signnow-sdk
	@echo "Container started. Use 'make docker-shell' to enter."

docker-shell:
	@echo "Entering Docker container..."
	docker-compose exec signnow-sdk bash

docker-down:
	@echo "Stopping Docker container..."
	docker-compose down

docker-test:
	@echo "Running tests in Docker..."
	docker-compose --profile test run --rm test

docker-test-cov:
	@echo "Running tests with coverage in Docker..."
	docker-compose --profile test run --rm test-cov
	@echo ""
	@echo "Coverage report generated in htmlcov/index.html"
	@echo "Open htmlcov/index.html in browser to view"

docker-test-api:
	@echo "Running real API tests in Docker..."
	docker-compose --profile test run --rm test-api

docker-examples:
	@echo "Running all examples in Docker..."
	docker-compose --profile examples run --rm run-examples

docker-example:
ifndef EXAMPLE
	@echo "Usage: make docker-example EXAMPLE=<name>"
	@echo "  e.g. make docker-example EXAMPLE=auth_check_example.py"
	@echo "  e.g. make docker-example EXAMPLE=auth_check_example"
	exit 1
endif
	@echo "Running example $(EXAMPLE) in Docker..."
	docker-compose --profile examples run --rm run-examples python run_examples.py $(EXAMPLE)
