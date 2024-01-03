import numpy as np
import qutip as qt
import matplotlib.pyplot as plt

# System parameters
N = 10  # Number of qubits in the BEC
g = 0.1  # Interaction strength (arbitrary units)

# Define the Hamiltonian for the system
# As an example, using a chain of qubits with nearest-neighbor interactions
H = sum(qt.tensor([qt.sigmax() if i == j or i == j + 1 else qt.qeye(2) for i in range(N)]) for j in range(N - 1))


# Initial state: a product state with all qubits in the ground state
initial_state = qt.tensor([qt.basis(2, 0) for _ in range(N)])

# Time points
times = np.linspace(0, 50, 500)  # Simulate from t=0 to t=50

# Observables: let's track the expected value of the sigma_z operator for each qubit
observables = [qt.tensor([qt.sigmaz() if i == j else qt.qeye(2) for i in range(N)]) for j in range(N)]

# Time evolution
result = qt.mesolve(H, initial_state, times, [], observables)

# Analyze the results
# Plot the expected value of sigma_z for each qubit over time
plt.figure(figsize=(10, 8))
for i, obs in enumerate(observables):
    plt.plot(times, result.expect[i], label=f'Qubit {i+1}')

plt.xlabel('Time', fontsize=14)
plt.ylabel('Expectation value', fontsize=14)
plt.title('Time Evolution of Expectation Values', fontsize=16)
plt.legend()
plt.show()

# Calculate and plot the entropy of each qubit over time
entropy = [[qt.entropy_vn(qt.ptrace(state, [i])) for state in result.states] for i in range(N)]

plt.figure(figsize=(10, 8))
for i, ent in enumerate(entropy):
    plt.plot(times, ent, label=f'Qubit {i+1} Entropy')
plt.xlabel('Time', fontsize=14)
plt.ylabel('Entropy', fontsize=14)
plt.title('Time Evolution of Entropy for Each Qubit', fontsize=16)
plt.legend()
plt.show()
