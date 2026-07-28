
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

def create_ghz_circuit(alice_basis, bob_basis, charlie_basis, eve_interferes=False):
    """
    Creates a 3-qubit GHZ state and measures it based on chosen bases.
    Bases: 'Z' = Standard measurement, 'X' = Diagonal measurement
    """
    # Define three qubits for Alice, Bob, and Charlie
    q = cirq.NamedQubit.range(3, prefix='q')
    circuit = cirq.Circuit()

    # 1. State Preparation: Create the entangled GHZ State (|000> + |111>) / sqrt(2)
    circuit.append([
        cirq.H(q[0]),          # Put Alice in superposition
        cirq.CNOT(q[0], q[1]),    # Entangle Bob with Alice
        cirq.CNOT(q[1], q[2])     # Entangle Charlie with Bob
    ])

    # 2. Optional Eavesdropping Simulation
    if eve_interferes:
        # Eve secretly measures Bob's qubit in the Z-basis
        circuit.append(cirq.measure(q[1], key='eve_measurement'))

        # if a Z-basis measurement is chosen by Alice, Bob, and Charlie.
        circuit.append(cirq.X(q[1])) # Apply X gate (bit flip)

    # 3. Measurement Basis Changes
    # If a party chooses the X-basis, we apply a Hadamard gate before measuring
    if alice_basis == 'X': circuit.append(cirq.H(q[0]))
    if bob_basis == 'X': circuit.append(cirq.H(q[1]))
    if charlie_basis == 'X': circuit.append(cirq.H(q[2]))

    # 4. Final Measurement
    circuit.append([
        cirq.measure(q[0], key='Alice'),
        cirq.measure(q[1], key='Bob'),
        cirq.measure(q[2], key='Charlie')
    ])

    return circuit

def run_simulation(num_bits=20, eavesdropped=False):
    simulator = cirq.Simulator()

    final_alice_key = []
    final_bob_key = []
    final_charlie_key = []

    #print(f"\n--- Running GHZ QKD Simulation ({'WITH Eavesdropper' if eavesdropped else 'SECURE'}) ---")
    #print(f"{'Basis (A,B,C)':<15} | {'Raw Outcome (A,B,C)':<20} | Status")
    #print("-" * 60)

    for _ in range(num_bits):
        # Randomly choose Z or X basis for all three parties
        a_basis = random.choice(['Z', 'X'])
        b_basis = random.choice(['Z', 'X'])
        c_basis = random.choice(['Z', 'X'])

        # Build and simulate the circuit for this single bit
        circuit = create_ghz_circuit(a_basis, b_basis, c_basis, eve_interferes=eavesdropped)
        result = simulator.run(circuit, repetitions=1)

        # Extract the results (0 or 1)
        a_res = result.measurements['Alice'][0][0]
        b_res = result.measurements['Bob'][0][0]
        c_res = result.measurements['Charlie'][0][0]

        basis_str = f"({a_basis},{b_basis},{c_basis})"
        outcome_str = f"({a_res},{b_res},{c_res})"

        # Sifting Step: Keep keys ONLY if everyone chose the secure 'Z' basis
        if a_basis == 'Z' and b_basis == 'Z' and c_basis == 'Z':
            final_alice_key.append(a_res)
            final_bob_key.append(b_res)
            final_charlie_key.append(c_res)
            #print(f"{basis_str:<15} | {outcome_str:<20} | [KEPT]")
        #else:
            #print(f"{basis_str:<15} | {outcome_str:<20} | Discarded")

    # Display results and verify security
    #print("\n--- Final Results ---")
    #print(f"Alice's Key:   {final_alice_key}")
    #print(f"Bob's Key:     {final_bob_key}")
    #print(f"Charlie's Key: {final_charlie_key}")

    # Check if keys match perfectly
    if final_alice_key == final_bob_key == final_charlie_key:
        #print("[+] SUCCESS: All keys match perfectly! Channel is secure.")
        shared_secure_key = [int(key) for key in final_alice_key]
        print(f"Shared Secure Key: {shared_secure_key}")
    else:
        print("[!] ALERT: Keys do not match! Eavesdropper detected on the network.")
    print(shared_secure_key)
    return final_alice_key, final_bob_key, final_charlie_key

# --- Execute both scenarios ---

