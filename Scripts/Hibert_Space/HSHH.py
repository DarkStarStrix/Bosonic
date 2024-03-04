import plotly.graph_objects as go
import numpy as np


def visualize_atoms(atom_data):
    # Extract the atom vectors from the atom data
    atom_vectors = [data ['vector'] for data in atom_data]

    # Calculate the center of the space
    center = np.mean (atom_vectors, axis=0)

    # Create a central node at the center of the space
    central_node = go.Scatter3d (
        x=[center [0]],
        y=[center [1]],
        z=[center [2]],
        mode='markers',
        marker=dict (size=10, color='red'),
        name='Central Node'
    )

    # Create scatter plots for other nodes
    node_scatter = go.Scatter3d (
        x=[vector [0] for vector in atom_vectors],
        y=[vector [1] for vector in atom_vectors],
        z=[vector [2] for vector in atom_vectors],
        mode='markers',
        marker=dict (size=8, color='blue'),
        name='Atoms',
        text=['Atom ' + str (i + 1) for i in range (len (atom_vectors))],  # Add hover text
        hoverinfo='text'
    )

    # Create lines connecting the central node to all other nodes
    lines = []
    for i, vector in enumerate (atom_vectors):
        lines.append (go.Scatter3d (
            x=[center [0], vector [0]],
            y=[center [1], vector [1]],
            z=[center [2], vector [2]],
            mode='lines',
            line=dict (width=2, color='blue'),
            opacity=0.5,
            showlegend=False
        ))

    # Create the figure
    fig = go.Figure (data=[central_node, node_scatter] + lines)

    # Set layout
    fig.update_layout (
        scene=dict (
            xaxis=dict (title='X', backgroundcolor="rgb(200, 200, 230)", gridcolor="white", showbackground=True,
                        zerolinecolor="white"),
            yaxis=dict (title='Y', backgroundcolor="rgb(230, 200,230)", gridcolor="white", showbackground=True,
                        zerolinecolor="white"),
            zaxis=dict (title='Z', backgroundcolor="rgb(230, 230,200)", gridcolor="white", showbackground=True,
                        zerolinecolor="white"),
        ),
        margin=dict (l=0, r=0, b=0, t=0),
        showlegend=True,
        legend=dict (
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ),
        title='HSHH Atom Representation',
        hovermode="closest",
        annotations=[
            dict (
                showarrow=False,
                text="Data source: HSHH",
                xref="paper",
                yref="paper",
                x=0,
                y=0)
        ]
    )

    return fig
