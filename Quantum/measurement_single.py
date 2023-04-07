# Measurement of Single Qubit in Superposition by using Hadamard Gate for one time
import numpy as np # For array
from qiskit import * 
from qiskit.tools.visualization import plot_histogram # For plotting Histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1) # Initialize a quantum circuit with 1 quantum and 1 clssical registers (First Parameter for quantum register and other for classical register
qc.initialize([0, 1], 0) # Initialize quantum register with [0, 1] that is |1>
qc.h(0) # For Hadamard gate  
qc.measure(0, 0) # Measurement of Quantum Register at 0th Position and storing result in classical register at Oth position
print(qc) # Draw Quantum circuit

aer_sim = Aer.get_backend('aer_simulator') # Get object of quantum simulater
qobj = assemble(qc) # Convert circuit into Quantum Assembly Language

# Run Circuit Single Time
results1 = aer_sim.run(qobj, shots=1).result() # Run Circuit on Quantum Simulator for 1 time (shots give number of times circuit is going to run)
counts1 = results1.get_counts() # Get counts of measuered bits 
hist1 = plot_histogram(counts1) # Plot Histogram

hist1 
