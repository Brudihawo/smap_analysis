# %% codecell
import h5py
import os

# %% codecell
h5 = h5py.File("./data/198903253/SMAP_L3_SM_P_E_20201230_R17000_001.h5", "r")

# %% codecell
list(h5.keys())

# %% codecell
print("DATA KEYS")
print("======================")
for key in list(h5["Soil_Moisture_Retrieval_Data_PM"].keys()):
  print(key)
# %% codecell

print("METADATA KEYS")
print("======================")
for key in list(h5["Metadata"].keys()):
  print(key)

