import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(
    fname='data/inflammation-01.csv',
    delimiter=','
)
min_inflammation = np.min(
    data,
    axis=0
)
min_plot = plt.plot(min_inflammation)

