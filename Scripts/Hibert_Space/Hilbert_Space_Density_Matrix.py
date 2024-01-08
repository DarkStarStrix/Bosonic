from qutip import basis, tensor, ket2dm
from qutip.qip.operations import hadamard_transform, cnot
import matplotlib.pyplot as plt
import numpy as np

# Define the basis states |0> and |1>
state_0 = basis(2, 0)  # |0>
state_1 = basis(2, 1)  # |1>

# Apply the Hadamard gate to the state |0>
state_h = hadamard_transform(1) * state_0

# Create the Bell states for two atoms
bell_state1 = cnot() * tensor(state_h, state_1)
bell_state2 = cnot() * tensor(state_1, state_h)

# Convert the Bell states to density matrices
rho1 = ket2dm(bell_state1)
rho2 = ket2dm(bell_state2)

# Calculate the partial trace to get the reduced density matrices
rho1_reduced = rho1.ptrace(0)
rho2_reduced = rho2.ptrace(0)

# Print the reduced density matrices
print("Reduced density matrix for the first atom:")
print(rho1_reduced)

print("Reduced density matrix for the second atom:")
print(rho2_reduced)

# Calculate the purity of the reduced density matrices
purity1 = rho1_reduced.purity()
purity2 = rho2_reduced.purity()

# Plot the purity using matplotlib
plt.figure(figsize=(6, 4))
plt.bar([1, 2], [purity1, purity2])
plt.xticks([1, 2], ['First atom', 'Second atom'])
plt.ylabel('Purity')
plt.show()

# Get the data from the density matrices
rho1_data = rho1_reduced.full()
rho2_data = rho2_reduced.full()

# Create a figure with subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# Plot the real part of the density matrices
axs[0, 0].imshow(np.real(rho1_data), cmap='hot', interpolation='nearest')
axs[0, 0].set_title('Real part of rho1')
axs[1, 0].imshow(np.real(rho2_data), cmap='hot', interpolation='nearest')
axs[1, 0].set_title('Real part of rho2')

# Plot the imaginary part of the density matrices
axs[0, 1].imshow(np.imag(rho1_data), cmap='hot', interpolation='nearest')
axs[0, 1].set_title('Imaginary part of rho1')
axs[1, 1].imshow(np.imag(rho2_data), cmap='hot', interpolation='nearest')
axs[1, 1].set_title('Imaginary part of rho2')

# Plot the absolute value of the density matrices
axs[0, 2].imshow(np.abs(rho1_data), cmap='hot', interpolation='nearest')
axs[0, 2].set_title('Absolute value of rho1')
axs[1, 2].imshow(np.abs(rho2_data), cmap='hot', interpolation='nearest')
axs[1, 2].set_title('Absolute value of rho2')

# Show the plot
plt.show()
