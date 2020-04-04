SHELL 	:= /bin/bash
VERB  	:= 0
THREADS := 1
PYTHONPATH=$(shell pwd)

.EXPORT_ALL_VARIABLES:
.PHONY: all

nq_sat: N=4
nq_sat:
	python3 src/nq_sat.py $(N) > output/sat_nq.cnf
	cat output/sat_nq.cnf | docker run --rm -i msoos/cryptominisat --verb $(VERB) --threads $(THREADS) ||:

test:
	python3 -m unittest discover --verbose

clean: are-you-sure
	git clean -fXd

are-you-sure:
  echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
