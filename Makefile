
.default: help

.PHONY: help
help:
	@echo "usage:"
	@echo "dev | install-dev"
	@echo "   setup development environment"
	@echo ""
	@echo "test | run-all-tests"
	@echo "   run all tests"
	@echo ""
	@echo "run-doc-tests"
	@echo "   run all tests"
	@echo ""
	@echo "run-all-tests-w-coverage"
	@echo "   run all tests with coverage collection"
	@echo ""
	@echo "lint"
	@echo "   lint the code"
	@echo ""
	@echo "type-check"
	@echo "   check types"
	@echo ""
	@echo "fmt"
	@echo "   run formatter(s)"
	@echo ""
	@echo "check-fmt"
	@echo "   check formatting"
	@echo ""

PLATFORM := ${shell uname -o}
PROJECT := sparv_kb_ner

ifeq (${VIRTUAL_ENV},)
  VENV_NAME = .venv
  INVENV = poetry run
else
  VENV_NAME = ${VIRTUAL_ENV}
  INVENV =
endif

${info Platform: ${PLATFORM}}

dev: install-dev
install-dev:
	poetry install

.PHONY: test
test: run-all-tests
.PHONY: run-all-tests
run-all-tests:
	${INVENV} pytest -vv tests

.PHONY: run-doc-tests
run-doc-tests:
	${INVENV} python -m doctest -v karp_lex/value_objects/unique_id.py

.PHONY: run-all-tests-w-coverage
run-all-tests-w-coverage:
	${INVENV} pytest -vv --cov=${PROJECT}  --cov-report=xml tests

.PHONY: type-check
type-check:
	${INVENV} mypy ${PROJECT}

.PHONY: lint
lint:
	${INVENV} pylint --rcfile=.pylintrc ${PROJECT} tests

.PHONY: lint-refactorings
lint-refactorings:
	${INVENV} pylint --disable=C,W,E --enable=R ${PROJECT} tests

bumpversion-major:
	${INVENV} bump2version major

bumpversion-minor:
	${INVENV} bump2version minor

bumpversion:
	${INVENV} bump2version patch

.PHONY: fmt
fmt:
	${INVENV} black ${PROJECT} tests

.PHONY: check-fmt
check-fmt:
	${INVENV} black --check ${PROJECT} tests
