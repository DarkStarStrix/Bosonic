import plotly.graph_objects as go
import numpy as np

# Create a random network of nodes (atoms) and vectors
np.random.seed(42)
num_nodes = 10
node_colors = np.random.choice(['white', 'purple', 'green', 'orange', 'blue'], size=num_nodes)
node_positions = np.random.rand(num_nodes, 3)  # Random 3D positions

# Create a central node
central_node = go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode='markers',
    marker=dict(size=10, color='red'),
    name='Central Node'
)

# Create scatter plots for other nodes
node_scatter = go.Scatter3d(
    x=node_positions[:, 0],
    y=node_positions[:, 1],
    z=node_positions[:, 2],
    mode='markers',
    marker=dict(size=8, color=node_colors),
    name='Atoms'
)

# Create lines connecting nodes
lines = []
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        lines.append(go.Scatter3d(
            x=[node_positions[i, 0], node_positions[j, 0]],
            y=[node_positions[i, 1], node_positions[j, 1]],
            z=[node_positions[i, 2], node_positions[j, 2]],
            mode='lines',
            line=dict(width=2, color=node_colors[i]),
            opacity=0.5,
            showlegend=False
        ))

# Create the figure
fig = go.Figure(data=[central_node, node_scatter] + lines)

# Set layout
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=False,
    title='HSHH Atom Representation',
)

# Show the plot
fig.show()
