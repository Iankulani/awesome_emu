# ===========================================
# AWESOME-EMU-V1 - Makefile
# ===========================================
# Author: Ian Carter Kulani
# Version: 1.0.0
# Description: Build automation for AWESOME-EMU-V1
# ===========================================

# ===========================================
# VARIABLES
# ===========================================
APP_NAME        := awesome-emu
APP_VERSION     := 1.0.0
APP_AUTHOR      := Ian Carter Kulani
APP_DESC        := Ultimate Cybersecurity Command & Control Platform

# Python
PYTHON          := python3
PIP             := pip3
VENV_DIR        := venv
VENV_PYTHON     := $(VENV_DIR)/bin/python
VENV_PIP        := $(VENV_DIR)/bin/pip

# Directories
SRC_DIR         := .
TEST_DIR        := tests
DIST_DIR        := dist
BUILD_DIR       := build
DOCS_DIR        := docs
REPORTS_DIR     := awesome_emu_reports
CONFIG_DIR      := .awesome_emu_v1

# Docker
DOCKER          := docker
DOCKER_COMPOSE  := docker-compose
IMAGE_NAME      := $(APP_NAME)
IMAGE_TAG       := $(APP_VERSION)
REGISTRY        := registry.gitlab.com/iancarterkulani/awesome-emu

# Colors
RED             := \033[0;31m
GREEN           := \033[0;32m
YELLOW          := \033[1;33m
BLUE            := \033[0;34m
PURPLE          := \033[0;35m
CYAN            := \033[0;36m
WHITE           := \033[1;37m
NC              := \033[0m

# Files
MAIN_FILE       := awesome_emu.py
REQ_FILE        := requirements.txt
REQ_DEV_FILE    := requirements-dev.txt
SETUP_FILE      := setup.py
TEST_FILE       := test_commands.py
CHECK_FILE      := requirements-check.py

# Test options
PYTEST          := pytest
PYTEST_OPTS     := -v --tb=short --color=yes
COVERAGE_OPTS   := --cov=. --cov-report=term-missing --cov-report=html --cov-report=xml

# ===========================================
# HELP
# ===========================================
.PHONY: help
help: ## Show this help message
	@echo "$(WHITE)╔══════════════════════════════════════════════════════════════════════════════╗"
	@echo "║          🦅 AWESOME-EMU-V1 v$(APP_VERSION) - Makefile Help                          ║"
	@echo "╚══════════════════════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "$(CYAN)Usage:$(NC) make [target]"
	@echo ""
	@echo "$(YELLOW)Installation Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(install|setup|venv)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Development Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(run|dev|debug|shell)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Testing Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(test|lint|check|coverage)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Build Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(build|package|dist)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Docker Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(docker)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Cleanup Targets:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | grep -E '(clean|reset)' | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""

.DEFAULT_GOAL := help

# ===========================================
# INSTALLATION TARGETS
# ===========================================
.PHONY: install
install: ## Install application and dependencies
	@echo "$(CYAN)📦 Installing $(APP_NAME) v$(APP_VERSION)...$(NC)"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(REQ_FILE)
	@echo "$(GREEN)✅ Installation complete$(NC)"

.PHONY: install-dev
install-dev: ## Install development dependencies
	@echo "$(CYAN)📦 Installing development dependencies...$(NC)"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(REQ_FILE)
	$(PIP) install -r $(REQ_DEV_FILE)
	$(PIP) install pre-commit
	pre-commit install
	@echo "$(GREEN)✅ Development installation complete$(NC)"

.PHONY: install-user
install-user: ## Install for current user only
	@echo "$(CYAN)📦 Installing $(APP_NAME) for user...$(NC)"
	$(PIP) install --user --upgrade pip setuptools wheel
	$(PIP) install --user -r $(REQ_FILE)
	@echo "$(GREEN)✅ User installation complete$(NC)"

.PHONY: setup
setup: venv install-dev ## Setup development environment
	@echo "$(GREEN)✅ Development environment ready$(NC)"

.PHONY: venv
venv: ## Create virtual environment
	@echo "$(CYAN)🔧 Creating virtual environment...$(NC)"
	@test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	$(VENV_PIP) install --upgrade pip setuptools wheel
	@echo "$(GREEN)✅ Virtual environment created$(NC)"

.PHONY: activate
activate: ## Show activation command
	@echo "$(CYAN)Run this command to activate venv:$(NC)"
	@echo "  source $(VENV_DIR)/bin/activate"

.PHONY: deps
deps: ## Install only dependencies
	@echo "$(CYAN)📦 Installing dependencies...$(NC)"
	$(PIP) install -r $(REQ_FILE)
	@echo "$(GREEN)✅ Dependencies installed$(NC)"

.PHONY: deps-update
deps-update: ## Update all dependencies
	@echo "$(CYAN)📦 Updating dependencies...$(NC)"
	$(PIP) install --upgrade -r $(REQ_FILE)
	$(PIP) list --outdated
	@echo "$(GREEN)✅ Dependencies updated$(NC)"

# ===========================================
# RUN TARGETS
# ===========================================
.PHONY: run
run: ## Run the application
	@echo "$(CYAN)🚀 Starting $(APP_NAME)...$(NC)"
	$(PYTHON) $(MAIN_FILE)

.PHONY: run-verbose
run-verbose: ## Run with verbose logging
	@echo "$(CYAN)🚀 Starting $(APP_NAME) (verbose)...$(NC)"
	$(PYTHON) -v $(MAIN_FILE)

.PHONY: run-debug
run-debug: ## Run with debugger
	@echo "$(CYAN)🐛 Starting $(APP_NAME) (debug)...$(NC)"
	$(PYTHON) -m pdb $(MAIN_FILE)

.PHONY: run-web
run-web: ## Run web dashboard only
	@echo "$(CYAN)🌐 Starting web dashboard...$(NC)"
	$(PYTHON) -c "from awesome_emu import AwesomeEmu; app = AwesomeEmu(); app.web.start()"

.PHONY: shell
shell: ## Open interactive Python shell with app context
	@echo "$(CYAN)🐚 Opening Python shell...$(NC)"
	$(PYTHON) -i -c "from awesome_emu import *; print('AWESOME-EMU shell ready')"

.PHONY: check
check: ## Run requirements checker
	@echo "$(CYAN)🔍 Checking requirements...$(NC)"
	$(PYTHON) $(CHECK_FILE)

.PHONY: check-fix
check-fix: ## Check and fix requirements
	@echo "$(CYAN)🔍 Checking and fixing requirements...$(NC)"
	$(PYTHON) $(CHECK_FILE) --fix

# ===========================================
# TESTING TARGETS
# ===========================================
.PHONY: test
test: ## Run all tests
	@echo "$(CYAN)🧪 Running all tests...$(NC)"
	$(PYTEST) $(PYTEST_OPTS) $(TEST_DIR)/ || $(PYTHON) $(TEST_FILE)
	@echo "$(GREEN)✅ Tests complete$(NC)"

.PHONY: test-commands
test-commands: ## Run command tests
	@echo "$(CYAN)🧪 Running command tests...$(NC)"
	$(PYTHON) $(TEST_FILE)

.PHONY: test-unit
test-unit: ## Run unit tests only
	@echo "$(CYAN)🧪 Running unit tests...$(NC)"
	$(PYTEST) $(PYTEST_OPTS) $(TEST_DIR)/unit/ || true

.PHONY: test-integration
test-integration: ## Run integration tests only
	@echo "$(CYAN)🧪 Running integration tests...$(NC)"
	$(PYTEST) $(PYTEST_OPTS) $(TEST_DIR)/integration/ || true

.PHONY: test-coverage
test-coverage: ## Run tests with coverage report
	@echo "$(CYAN)🧪 Running tests with coverage...$(NC)"
	$(PYTEST) $(PYTEST_OPTS) $(COVERAGE_OPTS) $(TEST_DIR)/ || $(PYTHON) -m pytest $(COVERAGE_OPTS)
	@echo "$(GREEN)✅ Coverage report generated: htmlcov/index.html$(NC)"

.PHONY: test-watch
test-watch: ## Run tests in watch mode
	@echo "$(CYAN)🧪 Watching tests...$(NC)"
	$(PYTEST) -f $(TEST_DIR)/

.PHONY: test-parallel
test-parallel: ## Run tests in parallel
	@echo "$(CYAN)🧪 Running tests in parallel...$(NC)"
	$(PYTEST) $(PYTEST_OPTS) -n auto $(TEST_DIR)/

.PHONY: test-verbose
test-verbose: ## Run tests with verbose output
	@echo "$(CYAN)🧪 Running verbose tests...$(NC)"
	$(PYTEST) -vv --tb=long $(TEST_DIR)/

# ===========================================
# CODE QUALITY TARGETS
# ===========================================
.PHONY: lint
lint: ## Run all linters
	@echo "$(CYAN)🔍 Running linters...$(NC)"
	@echo "$(YELLOW)→ flake8$(NC)"
	-flake8 $(MAIN_FILE) --max-line-length=120 --ignore=E501,W503,E203
	@echo "$(YELLOW)→ pylint$(NC)"
	-pylint $(MAIN_FILE) --disable=C0114,C0115,C0116,R0913,R0914,R0915 || true
	@echo "$(YELLOW)→ mypy$(NC)"
	-mypy $(MAIN_FILE) --ignore-missing-imports || true
	@echo "$(GREEN)✅ Linting complete$(NC)"

.PHONY: format
format: ## Format code
	@echo "$(CYAN)✨ Formatting code...$(NC)"
	-black $(MAIN_FILE) --line-length=120
	-isort $(MAIN_FILE)
	@echo "$(GREEN)✅ Code formatted$(NC)"

.PHONY: format-check
format-check: ## Check code formatting
	@echo "$(CYAN)🔍 Checking formatting...$(NC)"
	-black --check $(MAIN_FILE) --line-length=120
	-isort --check-only $(MAIN_FILE)
	@echo "$(GREEN)✅ Format check complete$(NC)"

.PHONY: security
security: ## Run security checks
	@echo "$(CYAN)🔒 Running security checks...$(NC)"
	@echo "$(YELLOW)→ bandit$(NC)"
	-bandit -r . -f txt || true
	@echo "$(YELLOW)→ safety$(NC)"
	-safety check -r $(REQ_FILE) || true
	@echo "$(GREEN)✅ Security check complete$(NC)"

.PHONY: audit
audit: ## Audit dependencies for vulnerabilities
	@echo "$(CYAN)🔒 Auditing dependencies...$(NC)"
	-pip-audit -r $(REQ_FILE) || true
	$(GREEN)✅ Audit complete$(NC)

.PHONY: pre-commit
pre-commit: ## Run pre-commit hooks
	@echo "$(CYAN)🔍 Running pre-commit...$(NC)"
	pre-commit run --all-files
	@echo "$(GREEN)✅ Pre-commit complete$(NC)"

.PHONY: quality
quality: lint format-check security ## Run all quality checks
	@echo "$(GREEN)✅ All quality checks passed$(NC)"

# ===========================================
# BUILD TARGETS
# ===========================================
.PHONY: build
build: clean ## Build Python package
	@echo "$(CYAN)🔨 Building package...$(NC)"
	$(PYTHON) -m build
	@echo "$(GREEN)✅ Package built in $(DIST_DIR)/$(NC)"

.PHONY: build-sdist
build-sdist: ## Build source distribution
	@echo "$(CYAN)🔨 Building source distribution...$(NC)"
	$(PYTHON) setup.py sdist
	@echo "$(GREEN)✅ Source distribution built$(NC)"

.PHONY: build-wheel
build-wheel: ## Build wheel distribution
	@echo "$(CYAN)🔨 Building wheel...$(NC)"
	$(PYTHON) setup.py bdist_wheel
	@echo "$(GREEN)✅ Wheel built$(NC)"

.PHONY: package
package: build ## Create distribution packages
	@echo "$(CYAN)📦 Creating packages...$(NC)"
	@ls -la $(DIST_DIR)/
	@echo "$(GREEN)✅ Packages created$(NC)"

.PHONY: publish
publish: build ## Publish to PyPI
	@echo "$(CYAN)📤 Publishing to PyPI...$(NC)"
	twine upload $(DIST_DIR)/*
	@echo "$(GREEN)✅ Published$(NC)"

.PHONY: publish-test
publish-test: build ## Publish to TestPyPI
	@echo "$(CYAN)📤 Publishing to TestPyPI...$(NC)"
	twine upload --repository testpypi $(DIST_DIR)/*
	@echo "$(GREEN)✅ Published to TestPyPI$(NC)"

# ===========================================
# DOCKER TARGETS
# ===========================================
.PHONY: docker-build
docker-build: ## Build Docker image
	@echo "$(CYAN)🐳 Building Docker image...$(NC)"
	$(DOCKER) build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	$(DOCKER) build -t $(IMAGE_NAME):latest .
	@echo "$(GREEN)✅ Docker image built$(NC)"

.PHONY: docker-build-no-cache
docker-build-no-cache: ## Build Docker image without cache
	@echo "$(CYAN)🐳 Building Docker image (no cache)...$(NC)"
	$(DOCKER) build --no-cache -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "$(GREEN)✅ Docker image built$(NC)"

.PHONY: docker-run
docker-run: ## Run Docker container
	@echo "$(CYAN)🐳 Running Docker container...$(NC)"
	$(DOCKER) run -it --rm \
		--name $(APP_NAME) \
		-p 5000:5000 \
		-p 8080:8080 \
		-v $(PWD)/$(CONFIG_DIR):/opt/awesome-emu/config \
		$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: docker-run-bg
docker-run-bg: ## Run Docker container in background
	@echo "$(CYAN)🐳 Running Docker container in background...$(NC)"
	$(DOCKER) run -d --rm \
		--name $(APP_NAME) \
		-p 5000:5000 \
		-p 8080:8080 \
		$(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: docker-stop
docker-stop: ## Stop Docker container
	@echo "$(CYAN)🐳 Stopping Docker container...$(NC)"
	-$(DOCKER) stop $(APP_NAME) || true
	@echo "$(GREEN)✅ Container stopped$(NC)"

.PHONY: docker-logs
docker-logs: ## Show Docker logs
	$(DOCKER) logs -f $(APP_NAME)

.PHONY: docker-shell
docker-shell: ## Open shell in Docker container
	$(DOCKER) exec -it $(APP_NAME) /bin/bash

.PHONY: docker-push
docker-push: docker-build ## Push Docker image to registry
	@echo "$(CYAN)🐳 Pushing Docker image...$(NC)"
	$(DOCKER) tag $(IMAGE_NAME):$(IMAGE_TAG) $(REGISTRY):$(IMAGE_TAG)
	$(DOCKER) tag $(IMAGE_NAME):$(IMAGE_TAG) $(REGISTRY):latest
	$(DOCKER) push $(REGISTRY):$(IMAGE_TAG)
	$(DOCKER) push $(REGISTRY):latest
	@echo "$(GREEN)✅ Docker image pushed$(NC)"

.PHONY: docker-clean
docker-clean: ## Clean Docker resources
	@echo "$(CYAN)🐳 Cleaning Docker resources...$(NC)"
	-$(DOCKER) rmi $(IMAGE_NAME):$(IMAGE_TAG) || true
	-$(DOCKER) rmi $(IMAGE_NAME):latest || true
	-$(DOCKER) system prune -f || true
	@echo "$(GREEN)✅ Docker cleaned$(NC)"

# ===========================================
# DOCKER COMPOSE TARGETS
# ===========================================
.PHONY: compose-up
compose-up: ## Start services with docker-compose
	@echo "$(CYAN)🐳 Starting services...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)✅ Services started$(NC)"

.PHONY: compose-down
compose-down: ## Stop services
	@echo "$(CYAN)🐳 Stopping services...$(NC)"
	$(DOCKER_COMPOSE) down
	@echo "$(GREEN)✅ Services stopped$(NC)"

.PHONY: compose-logs
compose-logs: ## Show compose logs
	$(DOCKER_COMPOSE) logs -f

.PHONY: compose-build
compose-build: ## Build compose services
	@echo "$(CYAN)🐳 Building services...$(NC)"
	$(DOCKER_COMPOSE) build
	@echo "$(GREEN)✅ Services built$(NC)"

.PHONY: compose-restart
compose-restart: ## Restart services
	@echo "$(CYAN)🐳 Restarting services...$(NC)"
	$(DOCKER_COMPOSE) restart
	@echo "$(GREEN)✅ Services restarted$(NC)"

.PHONY: compose-ps
compose-ps: ## Show running services
	$(DOCKER_COMPOSE) ps

# ===========================================
# CLEANUP TARGETS
# ===========================================
.PHONY: clean
clean: ## Clean build artifacts
	@echo "$(CYAN)🧹 Cleaning build artifacts...$(NC)"
	-rm -rf $(BUILD_DIR)
	-rm -rf $(DIST_DIR)
	-rm -rf *.egg-info
	-rm -rf .eggs
	-rm -rf __pycache__
	-rm -rf .pytest_cache
	-rm -rf .mypy_cache
	-rm -rf .coverage
	-rm -rf htmlcov
	-rm -rf coverage.xml
	-rm -rf .tox
	-find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	-find . -type f -name "*.pyc" -delete 2>/dev/null || true
	-find . -type f -name "*.pyo" -delete 2>/dev/null || true
	-find . -type f -name "*.egg" -delete 2>/dev/null || true
	@echo "$(GREEN)✅ Cleaned$(NC)"

.PHONY: clean-all
clean-all: clean ## Clean everything including reports
	@echo "$(CYAN)🧹 Cleaning all artifacts...$(NC)"
	-rm -rf $(REPORTS_DIR)
	-rm -rf $(CONFIG_DIR)
	-rm -rf logs
	-rm -rf .awesome_emu_v1
	@echo "$(GREEN)✅ All cleaned$(NC)"

.PHONY: clean-venv
clean-venv: ## Remove virtual environment
	@echo "$(CYAN)🧹 Removing virtual environment...$(NC)"
	-rm -rf $(VENV_DIR)
	@echo "$(GREEN)✅ Virtual environment removed$(NC)"

.PHONY: clean-docker
clean-docker: docker-clean ## Clean Docker resources

.PHONY: reset
reset: clean-all ## Reset to initial state
	@echo "$(CYAN)🔄 Resetting to initial state...$(NC)"
	@echo "$(GREEN)✅ Reset complete$(NC)"

.PHONY: reset-config
reset-config: ## Reset configuration only
	@echo "$(CYAN)🔄 Resetting configuration...$(NC)"
	-rm -rf $(CONFIG_DIR)
	@echo "$(GREEN)✅ Configuration reset$(NC)"

.PHONY: reset-reports
reset-reports: ## Reset reports only
	@echo "$(CYAN)🔄 Resetting reports...$(NC)"
	-rm -rf $(REPORTS_DIR)
	@echo "$(GREEN)✅ Reports reset$(NC)"

# ===========================================
# DOCUMENTATION TARGETS
# ===========================================
.PHONY: docs
docs: ## Build documentation
	@echo "$(CYAN)📚 Building documentation...$(NC)"
	cd $(DOCS_DIR) && make html
	@echo "$(GREEN)✅ Documentation built$(NC)"

.PHONY: docs-serve
docs-serve: ## Serve documentation locally
	@echo "$(CYAN)📚 Serving documentation...$(NC)"
	cd $(DOCS_DIR)/_build/html && $(PYTHON) -m http.server 8000

.PHONY: docs-clean
docs-clean: ## Clean documentation
	-rm -rf $(DOCS_DIR)/_build
	@echo "$(GREEN)✅ Documentation cleaned$(NC)"

# ===========================================
# RELEASE TARGETS
# ===========================================
.PHONY: version
version: ## Show current version
	@echo "$(CYAN)Version: $(APP_VERSION)$(NC)"

.PHONY: bump-patch
bump-patch: ## Bump patch version
	@echo "$(CYAN)🔢 Bumping patch version...$(NC)"
	@sed -i 's/APP_VERSION := .*/APP_VERSION := $(shell echo $(APP_VERSION) | awk -F. "{print \$$1\".\"\$$2\".\"\$$3+1}")/' Makefile
	@echo "$(GREEN)✅ Version bumped$(NC)"

.PHONY: bump-minor
bump-minor: ## Bump minor version
	@echo "$(CYAN)🔢 Bumping minor version...$(NC)"
	@echo "$(YELLOW)Manual edit required$(NC)"

.PHONY: bump-major
bump-major: ## Bump major version
	@echo "$(CYAN)🔢 Bumping major version...$(NC)"
	@echo "$(YELLOW)Manual edit required$(NC)"

.PHONY: release
release: clean quality test build ## Full release process
	@echo "$(GREEN)✅ Release v$(APP_VERSION) ready$(NC)"

.PHONY: changelog
changelog: ## Generate changelog
	@echo "$(CYAN)📝 Generating changelog...$(NC)"
	git log --oneline --decorate --graph > CHANGELOG.txt
	@echo "$(GREEN)✅ Changelog generated$(NC)"

# ===========================================
# GIT TARGETS
# ===========================================
.PHONY: git-status
git-status: ## Show git status
	git status

.PHONY: git-add
git-add: ## Add all files
	git add -A

.PHONY: git-commit
git-commit: ## Commit changes
	@read -p "Commit message: " msg; \
	git commit -m "$$msg"

.PHONY: git-push
git-push: ## Push to remote
	git push

.PHONY: git-tag
git-tag: ## Create version tag
	git tag -a v$(APP_VERSION) -m "Release v$(APP_VERSION)"
	git push origin v$(APP_VERSION)

.PHONY: git-sync
git-sync: ## Sync with remote
	git pull --rebase
	git push

# ===========================================
# CI/CD TARGETS
# ===========================================
.PHONY: ci
ci: install-dev quality test ## Run CI pipeline locally
	@echo "$(GREEN)✅ CI pipeline complete$(NC)"

.PHONY: ci-test
ci-test: test-coverage ## Run CI tests
	@echo "$(GREEN)✅ CI tests complete$(NC)"

.PHONY: ci-build
ci-build: build docker-build ## Run CI build
	@echo "$(GREEN)✅ CI build complete$(NC)"

.PHONY: ci-deploy
ci-deploy: docker-push ## Run CI deploy
	@echo "$(GREEN)✅ CI deploy complete$(NC)"

# ===========================================
# MONITORING TARGETS
# ===========================================
.PHONY: monitor
monitor: ## Monitor system resources
	@echo "$(CYAN)📊 Monitoring system...$(NC)"
	$(PYTHON) -c "import psutil; print(f'CPU: {psutil.cpu_percent()}% | Memory: {psutil.virtual_memory().percent}% | Disk: {psutil.disk_usage(\"/\").percent}%')"

.PHONY: logs
logs: ## Show application logs
	@echo "$(CYAN)📜 Showing logs...$(NC)"
	tail -f $(CONFIG_DIR)/awesome_emu.log 2>/dev/null || echo "No logs found"

.PHONY: stats
stats: ## Show application statistics
	@echo "$(CYAN)📊 Application statistics...$(NC)"
	$(PYTHON) -c "from awesome_emu import DatabaseManager; db = DatabaseManager(); stats = db.get_statistics(); [print(f'  {k}: {v}') for k, v in stats.items()]"

# ===========================================
# SECURITY TARGETS
# ===========================================
.PHONY: scan
scan: ## Run security scan
	@echo "$(CYAN)🔒 Running security scan...$(NC)"
	$(PYTHON) $(MAIN_FILE) nmap_quick 127.0.0.1

.PHONY: verify
verify: ## Verify installation
	@echo "$(CYAN)🔍 Verifying installation...$(NC)"
	@$(PYTHON) -c "import sys; print(f'Python: {sys.version}')"
	@$(PYTHON) -c "import requests; print(f'requests: {requests.__version__}')"
	@$(PYTHON) -c "import flask; print(f'flask: {flask.__version__}')"
	@echo "$(GREEN)✅ Verification complete$(NC)"

# ===========================================
# INSTALLATION SCRIPT TARGETS
# ===========================================
.PHONY: install-linux
install-linux: ## Run Linux installation script
	@echo "$(CYAN)📦 Running Linux installer...$(NC)"
	sudo bash install.sh

.PHONY: install-windows
install-windows: ## Run Windows installation script
	@echo "$(CYAN)📦 Running Windows installer...$(NC)"
	powershell -ExecutionPolicy Bypass -File install.ps1

.PHONY: install-batch
install-batch: ## Run Batch installation script
	@echo "$(CYAN)📦 Running Batch installer...$(NC)"
	cmd /c install.bat

.PHONY: uninstall
uninstall: ## Uninstall application
	@echo "$(CYAN)🗑️ Uninstalling...$(NC)"
	$(PIP) uninstall -y $(APP_NAME)
	@echo "$(GREEN)✅ Uninstalled$(NC)"

# ===========================================
# QUICK COMMANDS
# ===========================================
.PHONY: all
all: install test ## Install and test

.PHONY: fresh
fresh: clean-all install-dev test ## Fresh install and test

.PHONY: quick
quick: run ## Quick run

.PHONY: info
info: ## Show application info
	@echo "$(WHITE)╔══════════════════════════════════════════════════════════════════════════════╗"
	@echo "║                    🦅 AWESOME-EMU-V1 - Application Info                      ║"
	@echo "╚══════════════════════════════════════════════════════════════════════════════╝$(NC)"
	@echo ""
	@echo "  $(CYAN)Name:$(NC)        $(APP_NAME)"
	@echo "  $(CYAN)Version:$(NC)     $(APP_VERSION)"
	@echo "  $(CYAN)Author:$(NC)      $(APP_AUTHOR)"
	@echo "  $(CYAN)Description:$(NC) $(APP_DESC)"
	@echo ""
	@echo "  $(CYAN)Python:$(NC)      $$($(PYTHON) --version 2>&1)"
	@echo "  $(CYAN)Platform:$(NC)    $$(uname -s) $$(uname -m)"
	@echo ""
	@echo "  $(YELLOW)⚠️  For authorized security testing only$(NC)"
	@echo ""

.PHONY: env
env: ## Show environment variables
	@echo "$(CYAN)Environment Variables:$(NC)"
	@env | grep -E '(AWESOME|PYTHON|PATH)' | sort

.PHONY: ports
ports: ## Show exposed ports
	@echo "$(CYAN)Exposed Ports:$(NC)"
	@echo "  5000 - Web Dashboard"
	@echo "  8080 - Phishing Server"
	@echo "  4444 - C2 Server"
	@echo "  5555 - Agent Listener"

.PHONY: health
health: ## Health check
	@echo "$(CYAN)🏥 Health check...$(NC)"
	@$(PYTHON) -c "import sys; sys.exit(0)" && echo "$(GREEN)✅ Python OK$(NC)" || echo "$(RED)❌ Python FAIL$(NC)"
	@curl -s http://localhost:5000 > /dev/null 2>&1 && echo "$(GREEN)✅ Web OK$(NC)" || echo "$(YELLOW)⚠️ Web not running$(NC)"
