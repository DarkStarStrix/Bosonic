import numpy as np
from qutip import *
import plotly.graph_objs as go

# prompt the user for the parameters
N = int (input ("Enter the number of atoms: "))
T = float (input ("Enter the temperature: "))
B = float (input ("Enter the magnetic field: "))

# Create a basis for the Hilbert space
basis = [np.array ([1, 0]), np.array ([0, 1])]

# Define the operations
pauli_x = np.array ([[0, 1], [1, 0]])


def calculate_hilbert_space(basis, operator):
    # Calculate the result of applying the operator to the state |0>
    result = np.dot (operator, basis [0])
    return result


# Calculate the Hilbert space
hilbert_space = calculate_hilbert_space (basis, pauli_x)
print (hilbert_space)


# create a Bose-Einstein Condensate
rho = thermal_dm (N, T)

# create the spin operators
spin_jx = jmat (0.5, 'x')
spin_jy = jmat (0.5, 'y')
spin_jz = jmat (0.5, 'z')

# calculate the spin of the atoms
spin_x = expect (spin_jx, rho)
spin_y = expect (spin_jy, rho)
spin_z = expect (spin_jz, rho)

# create the measurement operator for the global qubit
measurement_operator = (spin_jx + B * spin_jz)

# calculate the expectation value of the measurement operator
measurement_expectation = expect (measurement_operator, rho)

# calculate the eigenvalues and eigenstates of the state
eigenvalues, eigenstates = rho.eigenstates ()

# plot the distribution of the quantum states
fig = go.Figure (data=[go.Histogram (x=np.arange (2 ** N), y=np.real (eigenvalues))])
fig.update_layout (xaxis_title='Eigenstate', yaxis_title='Probability')
fig.show ()

# plot the spin of the atoms
fig = go.Figure ()
fig.add_trace (go.Scatter (x=np.arange (N), y=[spin_x] * N, mode='lines', name='spin x'))
fig.add_trace (go.Scatter (x=np.arange (N), y=[spin_y] * N, mode='lines', name='spin y'))
fig.add_trace (go.Scatter (x=np.arange (N), y=[spin_z] * N, mode='lines', name='spin z'))
fig.update_layout (xaxis_title='Atom', yaxis_title='Spin')
fig.show ()

# plot the measurement expectation
fig = go.Figure (data=[go.Scatter (x=np.arange (N), y=[measurement_expectation] * N, mode='lines')])
fig.update_layout (xaxis_title='Atom', yaxis_title='Measurement Expectation')
fig.show ()

# plot the measurement expectation
fig = go.Figure (data=[go.Scatter (x=np.arange (N), y=[measurement_expectation] * N, mode='lines')])
fig.update_layout (xaxis_title='Atom', yaxis_title='Measurement Expectation')

# plot the eigenstates
fig = go.Figure ()
for i in range (2 ** N):
    fig.add_trace (go.Scatter (x=np.arange (N), y=np.real (eigenstates [i].data.toarray ().flatten ()), mode='lines'))
fig.update_layout (xaxis_title='Atom', yaxis_title='Eigenstate')
fig.show ()

# plot the hilbert space
fig = go.Figure (data=[go.Scatter3d (x=[0, 1], y=[0, 1], z=[0, 0], mode='markers', marker=dict (size=[10, 10], color=['red', 'blue']))])
fig.update_layout (scene=dict (xaxis_title='|0>', yaxis_title='|1>', zaxis_title=''))
fig.show ()
