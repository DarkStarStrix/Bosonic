import numpy as np
import matplotlib.pyplot as plt
from qutip import basis, tensor, wigner
from qutip.qip.operations import hadamard_transform, cnot

# Define the basis states |0> and |1>
state_0 = basis(2, 0)  # |0>
state_1 = basis(2, 1)  # |1>

# Apply the Hadamard gate to the state |0>
state_h = hadamard_transform(1) * state_0

# Create the Bell state
bell_state = cnot() * tensor(state_h, state_1)

# Calculate the Wigner function of the Bell state
x = np.linspace(-5, 5, 50)  # reduced from 100 to 50
y = np.linspace(-5, 5, 50)  # reduced from 100 to 50
W = wigner(bell_state, x, y)

# Create a 2D contour plot
plt.figure(figsize=(6, 6))
plt.contourf(x, y, W, 200, cmap='viridis')  # increased contour levels and changed colormap
plt.title('Wigner function')
plt.xlabel('x')
plt.ylabel('y')

# Add a color with a label
cbar = plt.colorbar()
cbar.set_label('Value')

# Show the plot
plt.show()
