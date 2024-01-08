from qutip import Bloch, basis, tensor
from qutip.qip.operations import hadamard_transform, cnot

# Define the basis states |0> and |1>
state_0 = basis(2, 0)  # |0>
state_1 = basis(2, 1)  # |1>

# Apply the Hadamard gate to the state |0>
state_h = hadamard_transform(1) * state_0

# Create the Bell states for two atoms
bell_state1 = cnot() * tensor(state_h, state_1)
bell_state2 = cnot() * tensor(state_1, state_h)

# Create a Bloch sphere
b = Bloch()

# Add the states to the Bloch sphere
b.add_states(bell_state1.ptrace(0))
b.add_states(bell_state2.ptrace(0))

# Show the Bloch sphere
b.show()
