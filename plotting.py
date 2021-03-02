#%%

import numpy as np 
import sys
sys.path.insert(0,'/home/eavesr/Documents/MITgcm')
from Data import Data

iters=np.linspace(160,58400,365).astype(int)
baro_wind_flat_channel = Data(dataDir='./run',iter_list=iters,geom='cartesian',dt=5400,dumpFreq=864000,f0=0.7*10**(-4),beta=2*10**(-11))

#%%
t = np.linspace(3650,3650,1).astype(int)
baro_wind_flat_channel.plot_streamU(times=t)

# %%

baro_wind_flat_channel.plot_streamV(times=t)

# %%
