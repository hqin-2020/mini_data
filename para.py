import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
import time
batch_n = np.random.randint(1,1000)
np.set_printoptions(suppress = True)
from Minimization import minimization
from concurrent.futures import ProcessPoolExecutor
obs_series = np.genfromtxt('obs_series.csv', delimiter=',')

start_trials = 14*10

obs_series = [obs_series for _ in range(start_trials)] 

if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        results = pool.map(minimization, obs_series)
    results = [r for r in results]

with open('data_'+str(batch_n)+'.pkl', 'wb') as f:
       pickle.dump(results, f)