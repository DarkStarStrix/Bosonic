import qutip as qt
import numpy as np
import plotly.graph_objects as go
import os

# Parameters
N = 10  # Number of qubits

# Define your system's Hamiltonian
# Note: Adjust the Hamiltonian as needed for your simulation.
H = sum (qt.tensor ([qt.sigmax () if i == j or i == j + 1 else qt.qeye (2) for i in range (N)]) for j in range (N - 1))

# Initial state - tensor product of ground states for all qubits
initial_state = qt.tensor ([qt.basis (2, 0) for _ in range (N)])

# Time points for which the evolution is solved
tlist = np.linspace (0, 10, 100)  # Time points

# Solving for the time evolution using mesolve
# No collapse operators ([]) since we're not considering dissipation
result = qt.mesolve (H, initial_state, tlist, [])

# Define the Pauli operators for the entire system
operators = [qt.tensor ([qt.sigmax () if i == j else qt.qeye (2) for i in range (N)]) for j in range (N)]
operators += [qt.tensor ([qt.sigmay () if i == j else qt.qeye (2) for i in range (N)]) for j in range (N)]
operators += [qt.tensor ([qt.sigmaz () if i == j else qt.qeye (2) for i in range (N)]) for j in range (N)]

# Calculate the expectation values for each operator at each time point
expectation_values = [[qt.expect (operator, state) for state in result.states] for operator in operators]

# Perform Fourier transform on the expectation values
fft_expectation_values = [np.fft.fft(values) for values in expectation_values]

# Plotting
fig = go.Figure ()

# Plotting the Fourier transformed expectation values
for i, values in enumerate (fft_expectation_values):
    fig.add_trace (go.Scatter (x=np.fft.fftfreq(len(tlist), tlist[1]-tlist[0]), y=np.abs(values), mode='lines', name=f'Operator {i + 1}'))

# Update the layout
fig.update_layout (title='Fourier Transform of Expectation Values of Pauli Operators',
                   xaxis_title='Frequency',
                   yaxis_title='Magnitude',
                   width=800, height=600)

# Show the plot
fig.show()
