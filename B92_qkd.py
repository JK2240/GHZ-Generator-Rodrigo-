
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

def run_B92(repetitions):
  alice_key = []
  bob_key = []
  my_qubits = []
  for i in range (repetitions):
    q = cirq.NamedQubit("q")
    simulator = cirq.Simulator()

    alice_bit = random.choice([0, 1])

    circuit = cirq.Circuit()
    if alice_bit == 1:
      circuit.append(cirq.X(q))
      circuit.append(cirq.H(q))
  
    bob_basis = random.choice(['Z', 'X'])

    if bob_basis == 'X' and alice_bit == 0:
        circuit.append(cirq.measure(q, key='mm'))
        result = simulator.run(circuit, repetitions=1)
        measurement = result.measurements['mm'][0][0]
        if measurement == 0:
          alice_key.append(alice_bit)
          bob_key.append(measurement)

         # print(circuit)
         # print(result)
          my_qubits.append(result)
          #print(f"Alice's Secret Bit: {alice_bit}")
          #print(f"Bob's Chosen Basis: {bob_basis}, measured {measurement}")
          #print("-" * 30)

    elif bob_basis == 'Z' and alice_bit == 1:
        circuit.append(cirq.H(q))
        circuit.append(cirq.measure(q, key = 'mm'))
        result = simulator.run(circuit, repetitions=1)
        measurement = result.measurements['mm'][0][0]
        if measurement == 1:
          alice_key.append(alice_bit)
          bob_key.append(measurement)

          #print(circuit)
          #print(result)
          my_qubits.append(result)
          #print(f"Alice's Secret Bit: {alice_bit}")
          #print(f"Bob's Chosen Basis: {bob_basis}, measured {measurement}")
          #print("-" * 30)
    #else:
          #print("Discard")
          #print("-" * 30)

    # Display results and verify security
    #print("\n--- Final Results ---")
    #print(f"Alice's Key:   {alice_key}")
    #print(f"Bob's Key:     {bob_key}")

    # Check if keys match perfectly
    if alice_key == bob_key:
        #print("[+] SUCCESS: All keys match perfectly! Channel is secure.")
        shared_key = [int(key) for key in alice_key]
        #print(f"Shared Key: {shared_key}")

  print(shared_key)
  return shared_key
