SHELL 	:= /bin/bash
VENV 		:= .env/bin
VERB  	:= 0
THREADS := 1
PYTHONPATH=$(shell pwd)

.EXPORT_ALL_VARIABLES:
.PHONY: all

install:
	( \
		python3 -m venv .env; \
		source .env/bin/activate; \
		pip install -r requirements.txt; \
	)

nq_sat: N=4
nq_sat:
	$(VENV)/python3 src/nq_sat.py $(N) > output/sat_nq.dimacs
	cat output/sat_nq.dimacs | docker run --rm -i msoos/cryptominisat --verb $(VERB) --threads $(THREADS) ||:

test:
		$(VENV)/python3 -m unittest discover --verbose

clean: are-you-sure
	git clean -fXd

are-you-sure:
  echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
