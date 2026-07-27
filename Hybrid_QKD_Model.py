try:
  import cirq
except ImportError:
  print ("installing cirq...")
  !pip install --quiet cirq
  print("installed cirq.")
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
import ghz_group_b92_qkd
import qkd_qith_ghz
import quantum_coinflip

for i in range(30):
  if QuantumCoinflip(1) == 0:
    run_B92(1)
  else:
    run_simulation(num_bits = 1, eavesdropped = False)
count = 0
Final = {}
B92 = {run_B92(30)}
QKD = {run_simulation(num_bits = 30, eavesdropped = False)
for i in range(30):
  if B92(i) == 0 and QKD(i) == 0:
    final(count) = 0
    count = count + 1
  elif B92(i) == 1 and QKD(i) == 1:
    final(count) = 1
    count = count + 1
