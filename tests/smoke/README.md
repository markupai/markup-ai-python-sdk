# Markup AI Python SDK Smoke Tests

This project contains the smoke test suite for the `markup-ai` Python SDK. The tests are
designed to validate the core functionality of the SDK using Behavior-Driven
Development (BDD) patterns.

## Overview

The smoke test suite uses `pytest` and `pytest-bdd` to ensure that the main API
endpoints and SDK wrappers are functioning correctly. The tests currently do not
cover all endpoints and SDK wrappers, specifically those that add data to the Markup AI
production account, such as style guides.

## Project Structure

```text
tests/smoke/
├── resources/              # Test assets (e.g., sample text files)
├── style_checks/           # Gherkin features and step definitions for style checks
├── style_guides/           # Gherkin features and step definitions for style guides
├── style_rewrites/         # Gherkin features and step definitions for style rewrites
├── style_suggestions/      # Gherkin features and step definitions for style suggestions
├── conftest.py             # Shared pytest fixtures and BDD steps
├── constants.py            # Test constants
├── pyproject.toml          # Poetry configuration and dependencies
└── README.md               # This file
```

## Requirements

- Python 3.13.7 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- A valid Production Markup AI API token

## Setup

1. **Install Dependencies**:
   Navigate to the `tests/smoke` directory and install the dependencies:
   ```bash
   poetry install
   ```
   *Note: This will also install the local version of the `markup-ai-api` SDK in
   editable
   mode.*

2. **Environment Configuration**:
   Create a `.env` file in the `tests/smoke` directory or set the following environment
   variable:
   ```env
   TOKEN=your_markup_ai_api_token
   ```

## Running Tests

To execute all smoke tests, run:

```bash
poetry run pytest
```

To run a specific feature or test file:

```bash
poetry run pytest style_checks/test_create_style_check.py
```

To run a specific test case within a file:

```bash
poetry run pytest style_checks/test_create_style_check.py -k "test_create_style_check"
```

## Environment Variables

| Variable | Description                              | Required |
|----------|------------------------------------------|----------|
| `TOKEN`  | Your Markup AI API authentication token. | Yes      |

## Scripts

The following scripts/commands are commonly used:

- `poetry run pytest`: Runs the full suite.
- `poetry run ruff check .`: (Optional) Runs linting checks on the test code.
