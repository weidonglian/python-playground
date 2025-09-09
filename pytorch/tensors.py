import torch
import numpy as np

# %% [directly from data]
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x_data = torch.tensor(data)

# %% [directly from numpy]
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
