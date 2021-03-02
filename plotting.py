#%%

import numpy as np 
import sys
sys.path.insert(0,'/home/eavesr/Documents/MITgcm')
from Data import Data

iters=[10]
baro_wind_flat_channel = Data(dataDir='./run',iter_list=iters,geom='cartesian',dt=5400,dumpFreq=864000,f0=0.7*10**(-4),beta=2*10**(-11))

baro_wind_flat_channel.plot_bathymetry()

# %%
print(baro_wind_flat_channel.Depth.values)
# %%
