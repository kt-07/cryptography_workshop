# Measurement of Single State ( 1/2 |0> + sqrt(3)/2 |1> )
import numpy as np # For array
from qiskit import * 
from qiskit.tools.visualization import plot_histogram # For plotting Histogram

qc = QuantumCircuit(1, 1) # Initialize a quantum circuit with 1 quantum and 1 clssical registers (First Parameter for quantum register and other for classical register
qc.initialize([1/2, np.sqrt(3)/2], 0) # Initialize quantum register with [0, 1] that is |1>

qc.measure(0, 0) # Measurement of Quantum Register at 0th Position and storing result in classical register at Oth position
print(qc) # Draw Quantum circuit


aer_sim = Aer.get_backend('aer_simulator') # Get object of quantum simulater
qobj = assemble(qc) # Convert circuit into Quantum Assembly Language

# Run Circuit Multiple Times Times
results = aer_sim.run(qobj, shots=1024).result() # Run Circuit on Quantum Simulator for 1 time (shots give number of times circuit is going to run)
counts = results.get_counts() # Get counts of measuered bits 
plot_histogram(counts) # Plot Histogram