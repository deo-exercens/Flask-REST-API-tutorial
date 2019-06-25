GREEN=\033[1;32;40m
RED=\033[1;31;40m
NC=\033[0m # No Color

PIP := $(shell command -v pip 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)

PYLINT = pylint
# W0511: TODO, FIXME
# W0621: pytest.fixture Redefining
# R0903: Too few public method
PYLINTFLAGS = -rn --disable=W0511,W0621,R0903

PYTHONFILES := $(shell find . -name '*.py' | grep -v .venv)

ref:
ifndef PIP
	# https://pip.pypa.io/en/stable/installing/
	$(error "pip이 설치되어 있지 않습니다.")
endif
	@bash -c "echo -e \"${GREEN}pip 설치되어 있음${NC}\""
ifndef PIPENV
	# $(error "direnv가 설치되어 있지 않습니다.")
	pip install pipenv
endif
	@bash -c "echo -e \"${GREEN}pipenv 설치되어 있음${NC}\""

ifndef DIRENV
	# https://github.com/direnv/direnv
	$(error "direnv가 설치되어 있지 않습니다.")
endif
	@bash -c "echo -e \"${GREEN}direnv 설치되어 있음${NC}\""
.PHONY: ref

venv_dir=.venv
venv-dev: 
ifneq "$(wildcard $(venv_dir) )" ""
	@bash -c "echo -e \"${GREEN}Already installation${NC}\""
else
	@bash -c "echo -e \"${GREEN}pipenv install${NC}\""
	export PIPENV_VENV_IN_PROJECT=${PWD}
	pipenv install --dev
endif
.PHONY: venv-dev

pylint: ref venv-dev $(patsubst %.py,%.pylint,$(PYTHONFILES))
.PHONY: pylint

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py

fast-pylint: ref venv-dev
	$(PYLINT) $(PYLINTFLAGS) $(PYTHONFILES)
.PHONY: fast-pylint

test: ref venv-dev
	@bash -c "echo -e \"${GREEN}start test${NC}\""
	@pipenv run python manage.py test
.PHONY: test

mermaid:
	@bash -c "echo -e \"${GREEN}Generate a flow chart${NC}\""
	@mmdc -i flowchart.mmd -o images/flow_chart.png
.PHONY: mermaid