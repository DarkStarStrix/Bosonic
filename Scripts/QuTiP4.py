import numpy as np
import qutip as qt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Parameters
N = 10  # Number of atoms
omega = 1.0  # Energy level spacing (arbitrary units)
g = 0.1  # Interaction strength (arbitrary units)
times = np.linspace (0, 10, 100)  # Time points

# Initial state - all atoms in ground state
initial_state = qt.tensor ([qt.basis (2, 0) for _ in range (N)])

# Hamiltonian setup
interaction_terms = [g * qt.tensor ([qt.sigmax () if i == j or i == j + 1 else qt.qeye (2) for i in range (N)]) for j in
                     range (N - 1)]
H = sum (interaction_terms)

# Time evolution
result = qt.mesolve (H, initial_state, times, [], [])

# Calculations
entanglement_entropy = np.zeros (len (times))
fidelity = np.zeros (len (times))
probabilities = np.zeros((10, len(times)))  # Assuming probabilities is a 2D numpy array

for i, state in enumerate (result.states):
    # Entanglement entropy for the first half of the system
    rho_reduced = qt.ptrace (state, list (range (N // 2)))
    entanglement_entropy [i] = qt.entropy_vn (rho_reduced, base=np.e)

    # Fidelity with respect to the initial state
    fidelity [i] = qt.fidelity (initial_state, state)

    # Probabilities
    probabilities[:10, i] = np.abs(state.full()).flatten()[:10]**2

# Visualization with Plotly

# Entanglement Entropy Plot
fig_entropy = go.Figure (data=[go.Scatter (x=times, y=entanglement_entropy, mode='lines', name='Entanglement Entropy')])
fig_entropy.update_layout (title='Entanglement Entropy Over Time',
                           xaxis_title='Time',
                           yaxis_title='Entanglement Entropy',
                           width=800, height=600)

# Fidelity Plot
fig_fidelity = go.Figure (data=[go.Scatter (x=times, y=fidelity, mode='lines', name='Fidelity')])
fig_fidelity.update_layout (title='Fidelity Over Time',
                            xaxis_title='Time',
                            yaxis_title='Fidelity',
                            width=800, height=600)

# Combine the plots into a subplot

fig = make_subplots (rows=2, cols=1)

fig.add_trace (fig_entropy ['data'] [0], row=1, col=1)
fig.add_trace (fig_fidelity ['data'] [0], row=2, col=1)

fig.update_layout (height=1200, title_text="Entanglement and Fidelity Over Time")
fig.show ()
