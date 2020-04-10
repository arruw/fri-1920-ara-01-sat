# Approximation and randomized algorithms - Assignment 01 - SAT 

https://www.nitt.edu/home/academics/departments/cse/faculty/kvi/NPC%20DOMINATING%20SET.pdf
https://www.cs.umd.edu/class/fall2017/cmsc451-0101/Lects/lect21-np-clique-vc-ds.pdf

## Commands
```bash
# create local virtual env and install pip packages
$ make install

# solve n-queens problem
$ make nq_sat N=4

# solve k-clique problem
$ make clique_sat G=input/g2.col K=2

# solve vertex cover problem
$ make vc_sat G=input/g2.col K=2

# solve dominanting set problem
$ make ds_sat G=input/g2.col K=2

# run unit tests
$ make test

# clean workspace directory
$ make clean
```