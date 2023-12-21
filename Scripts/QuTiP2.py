import numpy as np
import qutip as qt
import plotly.graph_objects as go

# Parameters
N = 10  # Number of atoms
omega = 1.0  # Energy level spacing for a hydrogen atom (arbitrary units)
times = np.linspace(0, 10, 100)  # Time points

# Create a list of 10 qubits all in the ground state
initial_state = qt.tensor([qt.basis(2, 0) for _ in range(N)])

# Create a Hamiltonian for the BEC with some interaction
# This is a simple model where each atom interacts with a strength g with its next neighbor
g = 0.1  # Interaction strength (arbitrary units)
interaction_terms = [g * qt.tensor([qt.sigmax() if i == j or i == j + 1 else qt.qeye(2) for i in range(N)]) for j in range(N-1)]
H = sum(interaction_terms)

# Time evolution
result = qt.mesolve(H, initial_state, times, [], [])

# Calculate the entanglement of formation or concurrence as a measure of entanglement
# For simplicity, we'll calculate the concurrence between the first and second qubit over time
concurrence = np.zeros(len(times))
for i, psi in enumerate(result.states):
    # Trace out all qubits except the first two to get their reduced density matrix
    rho = qt.ptrace(psi, [0, 1])
    # Calculate concurrence
    concurrence[i] = qt.concurrence(rho)

# Visualization with Plotly

# Extract probabilities of being in the excited state for each atom
probabilities = np.array([qt.expect(qt.fock_dm(2, 1), qt.ptrace(state, j)) for state in result.states for j in range(N)])
probabilities = probabilities.reshape(len(times), N)

# Create the data for the 3D surface plot
x, y = np.meshgrid(range(N), times)
z = probabilities.T  # Transpose to match dimensions with x and y

# Create 3D surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])
fig.update_layout(title='Hydrogen Gas BEC Excited State Probabilities Over Time',
                  scene=dict(xaxis_title='Atom Index',
                             yaxis_title='Time',
                             zaxis_title='Excited State Probability'),
                  autosize=False,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90))

# Show plot
fig.show()

# Plot the concurrence over time
fig_concurrence = go.Figure(data=[go.Scatter(x=times, y=concurrence, mode='lines')])
fig_concurrence.update_layout(title='Concurrence Over Time',
                              xaxis_title='Time',
                              yaxis_title='Concurrence',
                              width=800, height=600)
fig_concurrence.show()
