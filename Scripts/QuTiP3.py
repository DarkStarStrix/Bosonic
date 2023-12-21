import numpy as np
import qutip as qt
import plotly.graph_objects as go

# Parameters
N = 10  # Number of atoms
omega = 1.0  # Energy level spacing (arbitrary units)
g = 0.1  # Interaction strength (arbitrary units)
times = np.linspace(0, 10, 100)  # Time points

# Initial state - all atoms in ground state
initial_state = qt.tensor([qt.basis(2, 0) for _ in range(N)])

# Hamiltonian setup
interaction_terms = [g * qt.tensor([qt.sigmax() if i == j or i == j + 1 else qt.qeye(2) for i in range(N)]) for j in range(N-1)]
H = sum(interaction_terms)

# Time evolution
result = qt.mesolve(H, initial_state, times, [], [])

# Entanglement entropy calculation
entanglement_entropy = np.zeros(len(times))
for i, state in enumerate(result.states):
    # Calculate the reduced density matrix for the first half of the system
    rho_reduced = qt.ptrace(state, list(range(N//2)))
    # Von Neumann entropy of the reduced density matrix
    entanglement_entropy[i] = qt.entropy_vn(rho_reduced, base=np.e)

# Visualization of entanglement entropy over time
fig_entropy = go.Figure(data=[go.Scatter(x=times, y=entanglement_entropy, mode='lines')])
fig_entropy.update_layout(title='Entanglement Entropy Over Time',
                          xaxis_title='Time',
                          yaxis_title='Entanglement Entropy',
                          width=800, height=600)
fig_entropy.show()
