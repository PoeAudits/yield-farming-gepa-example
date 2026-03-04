# Python Makefile (uv + ruff)
.DEFAULT_GOAL := help
.PHONY: \
	help install sync lock run test lint fmt clean \
	optimize optimize-mock optimize-interactive optimize-resume \
	optimize-interactive-test optimize-resume-test \
	telegram telegram-mock \
	yield-preview yield yield-mock yield-analyze

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Install dependencies
	uv sync

sync: ## Sync dependencies (alias for install)
	uv sync

lock: ## Update lock file
	uv lock

run: ## Run the project
	uv run python -m $(shell basename $(CURDIR) | tr '-' '_')

test: ## Run tests
	uv run pytest

lint: ## Lint code (ruff check)
	uv run ruff check .

fmt: ## Format code (ruff format)
	uv run ruff format .

yield-preview: ## Show yield farming classifier dataset summary
	uv run python examples/yield_farming_classifier/preview.py

yield: ## Run yield farming classifier optimization with real evaluator
	uv run python examples/yield_farming_classifier/run.py

yield-mock: ## Run yield farming classifier optimization with mock evaluator
	uv run python examples/yield_farming_classifier/run.py --mock

yield-analyze: ## Analyze pareto frontier and extract hard examples for review
	uv run python examples/yield_farming_classifier/analyze_pareto.py

clean: ## Clean build artifacts
	rm -rf __pycache__ .pytest_cache .ruff_cache dist build *.egg-info .venv
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
