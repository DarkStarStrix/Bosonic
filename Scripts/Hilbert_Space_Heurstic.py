import numpy as np
import plotly.graph_objects as go

# Define the dimension of the Hilbert space
N = 2  # for a single qubit

# Create a basis for the Hilbert space
basis = [np.array([1, 0]), np.array([0, 1])]

# Define the operations
pauli_x = np.array([[0, 1], [1, 0]])

# Calculate the result of applying the Pauli-X gate to the state |0>
result = np.dot(pauli_x, basis[0])

print(result)

# Calculate the result of applying the Pauli-X gate to the state |1>
result = np.dot(pauli_x, basis[1])

print(result)

# visualize the hilbert space save the plot to C:\Users\kunya\PycharmProjects\ QuTiP Simulation\Plots folder
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 0], mode='lines', name='|0>'))
fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='|1>'))
fig.update_layout(xaxis_title='Real', yaxis_title='Imaginary')
fig.show()

# Define the dimension of the Hilbert space
N = 2  # for a single qubit

# Create a basis for the Hilbert space
basis = [np.array([1, 0]), np.array([0, 1])]
print(basis)

# Define the operations
pauli_x = np.array([[0, 1], [1, 0]])

# Calculate the result of applying the Pauli-X gate to the state |0>
result = np.dot(pauli_x, basis[0])
print(result)
