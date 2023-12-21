import numpy as np
import qutip as qt
import plotly.graph_objects as go

# Define system parameters
N = 10  # Number of two-level systems
g = 0.1  # Interaction strength (arbitrary units)
kB = 1   # Boltzmann constant in natural units (arbitrary units)

# Define your system's Hamiltonian (modify this according to your system)
H = sum(qt.tensor([qt.sigmax() if i == j or i == j + 1 else qt.qeye(2) for i in range(N)]) for j in range(N - 1))

# Calculate the eigenenergies of the Hamiltonian
eigenenergies = H.eigenenergies()

# Define a range of temperatures
temperatures = np.linspace(0.1, 3, 50)  # In units where kB = 1

# Calculate the expected thermal energy at each temperature
thermal_energies = []
for T in temperatures:
    # Calculate the partition function
    Z = sum(np.exp(-eigenenergy / (kB * T)) for eigenenergy in eigenenergies)
    # Calculate the expected thermal energy
    thermal_energy = sum(eigenenergy * np.exp(-eigenenergy / (kB * T)) for eigenenergy in eigenenergies) / Z
    thermal_energies.append(thermal_energy)

# Plotting
fig = go.Figure()

# Plot eigenenergies as horizontal lines (for visual comparison)
for eigenenergy in eigenenergies:
    fig.add_trace(go.Scatter(x=temperatures, y=[eigenenergy] * len(temperatures),
                             mode='lines', name=f'E={eigenenergy:.2f}', line=dict(dash='dash')))

# Plot thermal energies
fig.add_trace(go.Scatter(x=temperatures, y=thermal_energies, mode='lines', name='Thermal Energy'))

# Update the layout
fig.update_layout(title='Thermal Energy vs Eigenenergies',
                  xaxis_title='Temperature',
                  yaxis_title='Energy',
                  width=800, height=600)

# Show the plot
fig.show()

# Save the plot as a PNG image
fig.write_image('Thermal Energy vs Eigenenergies.png')
