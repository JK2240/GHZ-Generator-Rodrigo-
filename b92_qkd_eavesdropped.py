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

# ADDITION 1: Added 'verbose=True'. It defaults to printing everything normally.
def run_B92(repetitions, eavesdropper_active=False, verbose=True):
  alice_key = []
  bob_key = []
  loops = 0

  while len(alice_key) < repetitions:
    loops += 1
    q = cirq.NamedQubit("q")
    simulator = cirq.Simulator()

    alice_bit = random.choice([0, 1])

    circuit = cirq.Circuit()
    if alice_bit == 1:
      circuit.append(cirq.X(q))
      circuit.append(cirq.H(q))

    # --- Eavesdropper's action ---
    if eavesdropper_active:
      eve_basis = random.choice(['Z', 'X'])
      # Eve measures the qubit in her chosen random basis, collapsing its state.
      if eve_basis == 'Z':
        circuit.append(cirq.measure(q, key='eve_m_z')) # Measure in Z
      else: # eve_basis == 'X'
        circuit.append(cirq.H(q)) # Rotate to X basis
        circuit.append(cirq.measure(q, key='eve_m_x')) # Measure in X
        circuit.append(cirq.H(q)) # Rotate back to Z basis (optional for Eve to hide)

    bob_basis = random.choice(['Z', 'X'])

    # Bob's measurement and key generation for B92
    if bob_basis == 'X' and alice_bit == 0: # Alice sent |0> (Z-basis), Bob measures X-basis
        circuit.append(cirq.H(q)) # Rotate to X basis
        circuit.append(cirq.measure(q, key='mm'))
        result = simulator.run(circuit, repetitions=1)
        measurement = result.measurements['mm'][0][0]
        alice_key.append(alice_bit)
        bob_key.append(measurement)

    elif bob_basis == 'Z' and alice_bit == 1: # Alice sent |+> (X-basis), Bob measures Z-basis
        circuit.append(cirq.measure(q, key = 'mm')) # Already in Z basis
        result = simulator.run(circuit, repetitions=1)
        measurement = result.measurements['mm'][0][0]
        alice_key.append(alice_bit)
        bob_key.append(measurement)

  # ADDITION 2: Indented your exact print block under 'if verbose:'
  if verbose:
      print("B92 Iterations required to generate requested key length:")
      print(loops)
      print(f"\nAlice's generated key ({len(alice_key)} bits):")
      print(alice_key)
      print(f"Bob's generated key ({len(bob_key)} bits):")
      print(bob_key)

      mismatches = sum(1 for a, b in zip(alice_key, bob_key) if a != b)
      if mismatches == 0:
          print("\n[+] SUCCESS: Keys match perfectly!")
          if eavesdropper_active:
              print("No eavesdropper detected (or Eve was extremely lucky/passive). This is unlikely with active eavesdropping.")
          else:
              print("No noise or eavesdropper detected.")
      else:
          print(f"\n[-] FAILURE: {mismatches} mismatches found between Alice's and Bob's keys.")
          print("Eavesdropper detected due to discrepancies in keys!")

  # Left your exact return statement untouched
  return alice_key, bob_key


# --- Scenario: With Eavesdropper, increased repetitions ---
print("\n--- Running B92 Protocol (With Eavesdropper, 100 repetitions) ---")
# Runs normally and prints out your text blocks
alice_key_with_eve_100, bob_key_with_eve_100 = run_B92(repetitions=100, eavesdropper_active=True, verbose=True)


# --- ADDITION 3: The Simulation & Graphing Loop ---
max_key_length = 25 
trials_per_length = 50 

key_lengths = list(range(1, max_key_length + 1))
detection_probabilities = []

print(f"\nRunning graphing simulation ({max_key_length * trials_per_length} total quantum circuits). Please wait...")

for length in key_lengths:
    detections = 0
    for _ in range(trials_per_length):
        # We set verbose=False here so it doesn't print 1,250 times
        a_key, b_key = run_B92(repetitions=length, eavesdropper_active=True, verbose=False)
        
        # Because we kept your original return, we calculate the mismatches here in the loop
        mismatches = sum(1 for a, b in zip(a_key, b_key) if a != b)
        if mismatches > 0:
            detections += 1
            
    prob = detections / trials_per_length
    detection_probabilities.append(prob)

plt.figure(figsize=(10, 6))
plt.plot(key_lengths, detection_probabilities, marker='o', linestyle='-', color='#1f77b4')
plt.title('B92 Protocol: Eavesdropper Detection Probability vs Key Length')
plt.xlabel('Generated Key Length (bits)')
plt.ylabel('Probability of Detecting Eavesdropper')
plt.ylim(-0.05, 1.05)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(y=1.0, color='r', linestyle='--', alpha=0.5, label='100% Detection')
plt.legend()
plt.show()