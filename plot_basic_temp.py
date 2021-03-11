#!/usr/bin/env python
import pandas as pd
import h5py
from cartopy import crs as ccrs
from matplotlib import pyplot as plt
import numpy as np


f = h5py.File("data/198903253/SMAP_L3_SM_P_E_20201230_R17000_001.h5", "r")
# Got datasets 'Soil_Moisture_Retrieval_Data_AM' and 
#              'Soil_Moisture_Retrieval_Data_PM'

data_am = f['Soil_Moisture_Retrieval_Data_AM']
data_pm = f['Soil_Moisture_Retrieval_Data_PM']

# Get Datasets
lat = np.array(data_am["latitude"]).flatten()
lon = np.array(data_am["longitude"]).flatten()
temperature = np.array(data_am["surface_temperature"]).flatten()

lat2 = np.array(data_pm["latitude_pm"]).flatten()
lon2 = np.array(data_pm["longitude_pm"]).flatten()
temperature2 = np.array(data_pm["surface_temperature_pm"]).flatten()

lat = np.concatenate((lat, lat2))
lon = np.concatenate((lon, lon2))
temperature = np.concatenate((temperature, temperature2))


df = pd.DataFrame(data={"latitude":lat.T, "longitude":lon.T, "temperature":temperature.T})

df = df[df["temperature"] != -9999.0]
df = df.iloc[::5, :]

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

plt.scatter(df["longitude"],df["latitude"], c=df["temperature"])
plt.scavefig("temperature.png")


