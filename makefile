SHELL 	:= /bin/bash
VENV 		:= .env/bin
VERB  	:= 0
SEED    := 0
THREADS := $(shell nproc)
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
	@echo Reducing to SAT...
	@$(VENV)/python3 src/reduce_nq_sat.py $(N) > output/sat_nq.dimacs
	@echo Solving SAT...
	@docker run --rm -i -v "$(shell pwd)/output/sat_nq.dimacs:/input.dimacs:ro" msoos/cryptominisat --verb $(VERB) --threads $(THREADS) /input.dimacs > output/sat_nq.solution ||:
	@cat output/sat_nq.solution

clique_sat: G=input/g2.col
clique_sat: K=2
clique_sat:
	@echo Reducing to SAT...
	@$(VENV)/python3 src/reduce_clique_sat.py $(G) $(K) > output/sat_clique.dimacs
	@echo Solving SAT...
	@docker run --rm -i -v "$(shell pwd)/output/sat_clique.dimacs:/input.dimacs:ro" msoos/cryptominisat --verb $(VERB) --threads $(THREADS) /input.dimacs > output/sat_clique.solution ||:
	@cat output/sat_clique.solution

vc_sat: G=input/g2.col
vc_sat: K=2
vc_sat:
	@echo Reducing to SAT...
	@$(VENV)/python3 src/reduce_vc_sat.py $(G) $(K) > output/sat_vc.dimacs
	@echo Solving SAT...
	@docker run --rm -i -v "$(shell pwd)/output/sat_vc.dimacs:/input.dimacs:ro" msoos/cryptominisat --verb $(VERB) --threads $(THREADS) /input.dimacs > output/sat_vc.solution ||:
	@cat output/sat_vc.solution

ds_sat: G=input/g2.col
ds_sat: K=2
ds_sat:
	@echo Reducing to SAT...
	@$(VENV)/python3 src/reduce_ds_sat.py $(G) $(K) > output/sat_ds.dimacs
	@echo Solving SAT...
	@docker run --rm -i -v "$(shell pwd)/output/sat_ds.dimacs:/input.dimacs:ro" msoos/cryptominisat --verb $(VERB) --threads $(THREADS) /input.dimacs > output/sat_ds.solution ||:
	@cat output/sat_ds.solution

test:
		$(VENV)/python3 -m unittest discover --verbose

clean: are-you-sure
	git clean -fXd

are-you-sure:
  echo -n "Are you sure? [y/N] " && read ans && [ $${ans:-N} = y ]
