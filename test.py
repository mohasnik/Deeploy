import torch
import torch.nn
import numpy as np

x = torch.randn(2, 3, 20, 40)
globalAveragePool = torch.nn.AdaptiveAvgPool2d((1, 1))
y = globalAveragePool(x)

np.savez("x.npz", x=x.detach().cpu().numpy())
np.savez("y.npz", y=y.detach().cpu().numpy())


