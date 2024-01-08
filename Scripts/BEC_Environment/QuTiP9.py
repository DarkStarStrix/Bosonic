import numpy as np
import qutip as qt
import matplotlib.pyplot as plt

# Parameters
N = 5  # A smaller number of qubits for simplicity in visualization
g = 1.0  # Interaction strength (arbitrary units)

# Time points
times = np.linspace(0, 10, 100)

# Define the Hamiltonian for a chain of qubits with nearest-neighbor interactions
H = sum(qt.tensor([qt.sigmax() if i == j or i == j + 1 else qt.qeye(2) for i in range(N)]) for j in range(N - 1))

# Initial state - all qubits in the ground state
initial_state = qt.tensor([qt.basis(2, 0) for _ in range(N)])

# Collapse operators - represent decoherence processes,
# For instance, use a simple dephasing model for each qubit
dephasing_rate = 0.1  # Dephasing rate (arbitrary units)
collapse_operators = [np.sqrt(dephasing_rate) * qt.tensor([qt.sigmaz() if i == j else qt.qeye(2) for i in range(N)]) for j in range(N)]

# Run the simulation with decoherence
result = qt.mesolve(H, initial_state, times, collapse_operators, [])

# Calculate the purity of each state
purity = [(state * state).tr() for state in result.states]

# Plot the purity over time
plt.figure(figsize=(10, 8))
plt.plot(times, purity, label='Purity')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Purity', fontsize=14)
plt.title('Decoherence Over Time (Purity of System)', fontsize=16)
plt.legend()
plt.show()
