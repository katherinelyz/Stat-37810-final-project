# STAT 37810 Final Project #2: Gibbs Sampling
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import random,math
from math import *
from random import *

def gibbs(T, B, thin):
    M = zeros((T, 3))
    x = uniform(0, B)
    y = uniform(0, B)
    print "Iter  x  y"
    for i in range(T):
        for j in range(thin):
            u = random()
            x = -log(1 - u + u * exp(-B * y)) / y
            v = random()
            y = -log(1 - v + v * exp(-B * x)) / x
        M[i, 0] = i + 1
        M[i, 1] = x
        M[i, 2] = y
    print M
    # histogram of values for x
    plt.hist(M[:,1])
    plt.title("Histogram of values for x with sample size T=%r" % T)
    plt.savefig('gibbs%r.png' % T)
    plt.show()
    # the expectation of X
    print np.mean(M[:,1])

gibbs(T = 500, B = 5, thin = 10)
gibbs(T = 5000, B = 5, thin = 10)
gibbs(T = 50000, B = 5, thin = 10)
