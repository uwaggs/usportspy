# Development Guide

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- Python 3.8+

## Setup

Sync dependencies:
```bash
make sync
```

## Development Workflow

### Build the package
```bash
make build
```

### Install locally for testing
```bash
make install
```

This builds and installs the package into your environment, allowing you to test your changes.

### Test your changes

After installing, test the package in a Python shell or script:
```python
import usportspy
```

Or run the test suite:
```bash
make test
```

**Note:** `make test` does not automatically reinstall the package. If you've made code changes, run `make install` first to ensure tests use the latest version.

### Clean build artifacts
```bash
make clean
```

### Publish to PyPI

1. Update the version number in `pyproject.toml`
2. Upload to PyPI:
```bash
make upload
```

Note: PyPI does not allow re-uploading the same version number.

## Available Make Commands

Run `make help` to see all available commands.
