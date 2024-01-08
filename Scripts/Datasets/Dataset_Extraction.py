import os
import numpy as np
import pandas as pd
from qutip import basis, tensor, ket2dm
from qutip.qip.operations import hadamard_transform, cnot
import matplotlib.pyplot as plt
import os

# Get environment variable
data_dir = os.getenv('DATA_DIR')

# Use `data_dir` in your code
df.to_csv(os.path.join(data_dir, 'data.csv'), index=False)
