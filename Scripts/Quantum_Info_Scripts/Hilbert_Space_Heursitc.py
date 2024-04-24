from qutip import thermal_dm, basis, tensor, sigmax, sigmay, sigmaz, expect, qeye
import plotly.graph_objs as go


def compress_quantum_state(state, max_rank):
    coefficients, kets = state.schmidt_decomposition ()
    if len (coefficients) > max_rank:
        coefficients = coefficients [:max_rank]
        kets = kets [:max_rank]
    compressed_state = sum (coeff * ket for coeff, ket in zip (coefficients, kets))
    return compressed_state


def quantum_algorithm_suite(n, t, b):
    rho = thermal_dm (n, t)
    qubits = [basis (2, 0) for _ in range (n)]
    bec_state = tensor (qubits)
    single_qubit_operator = sigmax ()
    spin_jx = tensor ([single_qubit_operator] + [qeye (2) for _ in range (n - 1)])
    spin_jy = tensor ([sigmay ()] + [qeye (2) for _ in range (n - 1)])
    spin_jz = tensor ([sigmaz ()] + [qeye (2) for _ in range (n - 1)])
    spin_x = expect (spin_jx, rho)
    spin_y = expect (spin_jy, rho)
    spin_z = expect (spin_jz, rho)
    measurement_operator = (spin_jx + b * spin_jz)
    measurement_expectation = expect (measurement_operator, rho)
    eigenvalues, eigenstates = rho.eigenstates ()
    compressed_state = compress_quantum_state (rho, max_rank=10)
    return {
        'bec_state': bec_state,
        'spin': [spin_x, spin_y, spin_z],
        'measurement_expectation': measurement_expectation,
        'eigenstates': [eigenstate.tolist () for eigenstate in eigenstates],
        'eigenvalues': eigenvalues.tolist (),
        'compressed_state': compressed_state
    }


data = quantum_algorithm_suite (n=10, t=0.5, b=1)

# Plot the results
# Plot the eigenvalues
eigenvalues = data ['eigenvalues']
eigenvalues_trace = go.Scatter (
    x=list (range (len (eigenvalues))),
    y=eigenvalues,
    mode='markers',
    name='eigenvalues'
)

# Plot the compressed state
compressed_state = data ['compressed_state']
compressed_state_trace = go.Scatter (
    x=list (range (len (compressed_state))),
    y=compressed_state,
    mode='markers',
    name='compressed state'
)

# Plot the measurement expectation
measurement_expectation = data ['measurement_expectation']
measurement_expectation_trace = go.Scatter (
    x=[0],
    y=[measurement_expectation],
    mode='markers',
    name='measurement expectation'
)

# Plot the spin
spin = data ['spin']
spin_trace = go.Scatter (
    x=[0],
    y=spin,
    mode='markers',
    name='spin'
)

# Plot the BEC state
bec_state = data ['bec_state']
bec_state_trace = go.Scatter (
    x=list (range (len (bec_state))),
    y=bec_state,
    mode='markers',
    name='bec state'
)

# Plot the BEC in 3D
bec_state_3d_trace = go.Scatter3d (
    x=list (range (len (bec_state))),
    y=[0] * len (bec_state),
    z=bec_state,
    mode='markers',
    name='bec state'
)
