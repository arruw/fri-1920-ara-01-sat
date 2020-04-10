# Approximation and randomized algorithms - Assignment 01 - SAT 

## Requirements
- Ensure you have installed: `make`, `python3`, `docker`
- Install local virtual env and install pip packages: `make install`

## Dominanting sets
```bash
$ make ds_sat G=input/g1.col K=40   # ~10 minutes to solve
$ make ds_sat G=input/g2.col K=3    # ~1 second to solve
$ make ds_sat G=input/g3.col K=15   # ~2 minutes to solve
$ make ds_sat G=input/g4.col K=
$ make ds_sat G=input/g5.col K=5    # ~2 minutes to solve
```

## Other Commands
```bash
# create local virtual env and install pip packages
$ make install

# solve n-queens problem
$ make nq_sat N=4

# solve k-clique problem
$ make clique_sat G=input/test_rocket.col K=3

# solve vertex cover problem
$ make vc_sat G=input/test_rocket.col K=3

# solve dominanting set problem
$ make ds_sat G=input/test_rocket.col K=2

# find approximate sizes of dominanting sets using networkx
$ make ds_nx_approx 

# run unit tests
$ make test

# clean workspace directory
$ make clean
```