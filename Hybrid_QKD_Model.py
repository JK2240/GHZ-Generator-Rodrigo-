import cirq
import cirq_google
import cirq_web
import numpy as np
import math
import scipy
import sympy
import random
import matplotlib.pyplot as plt
import sys
sys.meta_path[:] = [f for f in sys.meta_path if "DaskFinder" not in str(f)]
from math import radians, degrees
from scipy.optimize import minimize
from cirq_web import bloch_sphere
from cirq import Z, PauliSum

import sys
sys.meta_path[:] = [f for f in sys.meta_path if "DaskFinder" not in str(f)]
from B92_qkd import *
from QKD_with_GHZ import *
from quantum_coinflip import *

count = 0
final = []
B92 = []
B92_add = run_B92(30)
for j in range(len(B92_add)):
  B92[j] = B92_add[j]

QKD = [run_simulation(num_bits = len(B92), eavesdropped = False)]
for i in range(30):
  if B92[i] == 0 and QKD[i] == 0:
    final[count] = 0
    count = count + 1
  elif B92[i] == 1 and QKD[i] == 1:
    final[count] = 1
    count = count + 1
print("FINAL KEY:")
print(final)