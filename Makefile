.PHONY: help build clean install upload sync test

help:
	@echo "Available commands:"
	@echo "  make build   - Build distribution packages using uv"
	@echo "  make clean   - Remove build artifacts"
	@echo "  make install - Install the package from built wheel"
	@echo "  make upload  - Upload package to PyPI"
	@echo "  make sync    - Sync dependencies with uv"
	@echo "  make test    - Run tests with pytest"

build:
	uv build

clean:
	rm -rf build dist *.egg-info

install: build
	uv pip install dist/usportspy*.whl --force-reinstall

upload: clean build
	uv run twine upload dist/*

sync:
	uv sync

test:
	uv run pytest --test-delay=1
