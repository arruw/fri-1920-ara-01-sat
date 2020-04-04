nq_sat:
	python src/reduce_nq_sat.py $(n) | docker run --rm -i msoos/cryptominisat || true