import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import sklearn
from sklearn.model_selection import train_test_split
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("PyTorch version: ", torch.__version__)
print("Numpy version: ", np.__version__)
print("Pandas version: ", pd.__version__)
print("Seaborn version: ", sns.__version__)
print("Matplotlib version: ", matplotlib.__version__)
print("Sklearn version: ", sklearn.__version__)

print("success!")
