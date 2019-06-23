PYLINT = pylint
# W0511: TODO, FIXME
# W0621: pytest.fixture Redefining
# R0903: Too few public method
PYLINTFLAGS = -rn --disable=W0511,W0621,R0903

PYTHONFILES := $(shell find . -name '*.py' | grep -v .venv)

pylint: $(patsubst %.py,%.pylint,$(PYTHONFILES))
.PHONY: pylint

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py

fast-pylint:
	$(PYLINT) $(PYLINTFLAGS) $(PYTHONFILES)
.PHONY: fast-pylint

mermaid:
	@echo "Generate a flow chart"
	@mmdc -i flowchart.mmd -o images/flow_chart.png
.PHONY: mermaid