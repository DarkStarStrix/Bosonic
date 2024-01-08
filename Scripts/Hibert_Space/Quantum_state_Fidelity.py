from qutip import basis, tensor, fidelity
from qutip.qip.operations import hadamard_transform, cnot
import matplotlib.pyplot as plt
import numpy as np

# Define the basis states |0> and |1>
state_0 = basis(2, 0)  # |0>
state_1 = basis(2, 1)  # |1>

# Apply the Hadamard gate to the state |0>
state_h = hadamard_transform(1) * state_0

# Create the Bell state
bell_state1 = cnot() * tensor(state_h, state_1)
bell_state2 = cnot() * tensor(state_1, state_h)

# Calculate the fidelity of the two states
fidelity_value = fidelity(bell_state1, bell_state2)

print("Fidelity:", fidelity_value)

# Create a list of phase factors
phases = np.linspace(0, 2*np.pi, 100)

# Calculate the fidelity for each phase factor
fidelities = []  # renamed to avoid conflict with fidelity function
for phase in phases:
    # Create Bell states with a phase factor
    bell_state1 = cnot() * tensor((np.cos(phase)*state_h + np.sin(phase)*state_1).unit(), state_1)
    bell_state2 = cnot() * tensor(state_1, (np.cos(phase)*state_h + np.sin(phase)*state_1).unit())

    # Calculate the fidelity
    fidelities.append(fidelity(bell_state1, bell_state2))

# Plot the fidelity as a function of the phase factor
plt.figure(figsize=(6, 4))
plt.plot(phases, fidelities)  # use the renamed list here
plt.xlabel('Phase')
plt.ylabel('Fidelity')
plt.title('Fidelity as a function of phase')
plt.show()
