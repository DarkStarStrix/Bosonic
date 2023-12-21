import qutip as qt
import numpy as np
import plotly.graph_objects as go

# Quantum simulation with QuTiP

# Parameters for the simulation
N = 10  # Number of states for simplicity

# Creating a quantum object representing the system's state
initial_state = qt.basis(N, 0)  # Start with the first state

# Hamiltonian of the system (example: simple harmonic oscillator)
H = qt.create(N) * qt.destroy(N)

# Time points at which to evaluate the system
times = np.linspace(0.0, 10.0, 100)

# Running the simulation - evolving the system over time
result = qt.mesolve(H, initial_state, times, [], [])

# Extracting data for visualization
# For this example, let's visualize the occupation probability of each state over time
probabilities = np.zeros((N, len(times)))
for i, state in enumerate(result.states):
    probabilities[:, i] = np.abs(state.full()).flatten()**2

# Plotly for 3D Visualization

# Preparing data for 3D plot
x, y = np.meshgrid(times, range(N))
z = probabilities

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])

# Customizing the layout
fig.update_layout(
    title='Quantum State Probabilities Over Time',
    scene=dict(
        xaxis_title='Time',
        yaxis_title='Quantum State',
        zaxis_title='Probability'
    ),
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=65, r=50, b=65, t=90)
)

# Show the plot
fig.show()
