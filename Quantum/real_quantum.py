## For running in real quantum computer

import numpy as np # For array
from qiskit import * 
from qiskit.tools.visualization import plot_histogram # For plotting Histogram
import matplotlib.pyplot as plt
from qiskit.providers.ibmq import least_busy

provider = IBMQ.save_account('INSER_YOUR_API_KEY', overwrite=True) # Goto Account setting for api key
provider = IBMQ.load_account() # loads all the quantum devices

backend = least_busy(provider.backends(filters=lambda x: int(x.configuration().n_qubits) >= 3 and 
                                   not x.configuration().simulator and x.status().operational==True)) # Find the least busy quantum device
print("least busy backend: ", backend)

# Run our circuit on the least busy backend. Monitor the execution of the job in the queue
from qiskit.tools.monitor import job_monitor
transpiled_qc = transpile(qc, backend, optimization_level=3)  # qc is the circuit
job = backend.run(transpiled_qc)
job_monitor(job, interval=2)

# Get the results from the computation
results = job.result()
answer = results.get_counts(qc)
plot_histogram(answer)
