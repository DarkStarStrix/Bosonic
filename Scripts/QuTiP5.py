import numpy as np
import qutip as qt
import plotly.graph_objects as go

# Parameters for the BEC simulation
N = 10  # Number of atoms
temps = np.linspace (0.1, 3, 100)  # Range of temperatures

# Initial state
initial_state = qt.tensor([qt.basis(2, 0) for _ in range(N)])

# Hamiltonian: Example using a collective spin model
Jx = qt.jmat (0.5, 'x')
Jy = qt.jmat (0.5, 'y')
Jz = qt.jmat (0.5, 'z')
H = qt.tensor([Jx for _ in range(N)]) + qt.tensor([Jy for _ in range(N)]) + qt.tensor([Jz for _ in range(N)])

# Time evolution
final_time = 10
result = qt.mesolve (H, initial_state, [0, final_time], [], [])

# Final state at last time point
final_state_dm = qt.ket2dm (result.states [-1])

# Calculate thermal state at different temperatures and compare with final state
fidelity_with_thermal = []
for T in temps:
    # Thermal state for the composite system
    thermal_state = qt.thermal_dm (2, T)
    for n in range (1, N):
        thermal_state = qt.tensor (thermal_state, qt.thermal_dm (2, T))

    # Calculate fidelity
    fidelity_with_thermal.append (qt.fidelity (final_state_dm, thermal_state))

# Plotting
fig = go.Figure ()
fig.add_trace (go.Scatter (x=temps, y=fidelity_with_thermal, mode='lines'))
fig.update_layout (title='Fidelity with Thermal State at Different Temperatures',
                   xaxis_title='Temperature',
                   yaxis_title='Fidelity',
                   width=800, height=600)
fig.show ()
