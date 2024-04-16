# Simulate the braiding of non-abelian anyons using Fibonacci anyons as an example

import numpy as np
import plotly.graph_objects as go
from matplotlib import cm
from matplotlib.colors import to_hex
from qutip import Qobj, tensor


class FibonacciAnyon:
    def __init__(self, state):
        self.state = Qobj (state)

    def __str__(self):
        return str (self.state)

    def __mul__(self, other):
        return FibonacciAnyon (tensor (self.state, other.state))

    def __add__(self, other):
        return FibonacciAnyon (self.state + other.state)


def braid_anyons(anyons, i, j):
    anyons [i], anyons [j] = anyons [j], anyons [i]
    return anyons


def update_braiding(anyons, i, j):
    U = Qobj ([[1, 0], [0, np.exp (1j * np.pi / 4)]])
    anyons [i].state = U * anyons [i].state
    anyons [j].state = U * anyons [j].state
    return anyons


def initialize_anyons(num_anyons):
    initial_states = [np.array ([1, 0]) for _ in range (num_anyons)]
    return [FibonacciAnyon (state) for state in initial_states]


def plot_braiding(anyons):
    fig = go.Figure ()
    num_points = 100  # Number of points in the path

    for i in range (len (anyons) - 1):
        anyons = braid_anyons (anyons, i, i + 1)
        anyons = update_braiding (anyons, i, i + 1)

        # Generate a circular path for the anyon
        t = np.linspace(0, 2*np.pi, num_points)
        path_x = np.cos(t + i*np.pi/len(anyons))  # Adjust the starting point of the path for each anyon
        path_y = np.sin(t)

        fig.add_trace (
            go.Scatter (x=path_x, y=path_y, mode='lines', line=dict (), name=f'anyon {i + 1} (after braiding)'))

    return fig


def main():
    num_anyons = 5
    anyons = initialize_anyons (num_anyons)
    fig = plot_braiding (anyons)
    fig.show ()


if __name__ == "__main__":
    main ()
