# Madelung-NaCl-ExpandingCube-Python
Here I implement in python3 a calculation of Madelung constant of NaCl with the method of expanding cubes :

[(Gaio and Silvestrelli, Phys. Rev. B 79, 012102 (2009))](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.79.012102). 

To run the script in a python3 environment, type the following in the terminal:

    python expanding-cube.py N

where $N$ is an input value corresponding to a cube of edge length $2N$.

This script hence calculates $\alpha(N), \alpha(N-1)$ and estimates the Madelung constant via their arithmetic average as described in Eq. (4) of the abovementioned paper. This code excellently reproduces the values of $\alpha_\textrm{NaCl}$ of Table I from that publication.

This work is based on a school project that I first implemented in Wolfram Mathematica in 2020.

Therefore, this python script is probably not so efficient for experienced users.

I am still learning, so I appreciate your kind understanding and guidance.

Thank you very much for visiting this page.
