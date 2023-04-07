# Demonstration of entanglement
import numpy as np # For array
from qiskit import * 
from qiskit.tools.visualization import plot_histogram # For plotting Histogram

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

def firstBellState():
    qc = QuantumCircuit(q,c)

    qc.h(q[0]) # Hadamard gate 
    qc.cx(q[0],q[1]) # CNOT gate
    qc.measure(q,c) # Qubit Measurment

    print(qc)
    
    return qc

qc = firstBellState()

aer_sim = Aer.get_backend('aer_simulator') # Get object of quantum simulater
qobj = assemble(qc) # Convert circuit into Quantum Assembly Language

# Run Circuit Multiple Times Times
results = aer_sim.run(qobj, shots=1024).result() # Run Circuit on Quantum Simulator for 1 time (shots give number of times circuit is going to run)
counts = results.get_counts() # Get counts of measuered bits 
plot_histogram(counts) # Plot Histogram