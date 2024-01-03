# calculate the entropy of a system over time
# using the von Neumann entropy

# import the needed libraries
import numpy as np
import matplotlib.pyplot as plt
from qutip import *
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *

# define the parameters
N = 10
a = destroy(N)
H = a.dag() * a
psi0 = basis(N, 5)
tlist = np.linspace(0, 10, 100)

# calculate the entropy over time
result = mesolve(H, psi0, tlist, [], [a.dag() * a])

# plt the results using plotly
init_notebook_mode(connected=True)
trace = Scatter(x=tlist, y=result.expect[0])
data = Data([trace])
plot(data)

# plot the results using matplotlib
plt.plot(tlist, result.expect[0])

# add some labels
plt.xlabel('Time')
plt.ylabel('Entropy')
plt.title('Entropy of a Fock state')
plt.show()
