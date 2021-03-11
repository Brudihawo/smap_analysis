# %% codecell
%matplotlib notebook
import pandas as pd
import h5py
import numpy as np
from cartopy import crs as ccrs
from matplotlib import cm
from matplotlib import pyplot as plt

from util import find_file_with_ending_recurse, get_data_from_folder



# %% codecell

lat, lon, temperature = get_data_from_folder("data", "surface_temperature")

print(lat.shape)

# %% codecell
# Get minimum temperature

tmp = temperature.copy()
tmp = tmp[tmp != -9999.0]
min_tmp = tmp.min()
max_tmp = tmp.max()

print(f"Minimum Temperature [K]: {min_tmp}\nMaximum Temperature [K]: {max_tmp}")
# %% codecell
# Mask array
m_tmp = np.ma.array(temperature)
tmp_masked = np.ma.masked_where(m_tmp <= min_tmp, m_tmp)
# Shift to °C
tmp_masked = tmp_masked - 273.15

# %% codecell
viridis = cm.get_cmap("viridis", 100)
viridis.set_under(alpha=0)


# %% codecell
plt.clf()
ax = plt.axes(projection=ccrs.PlateCarree())
fig = plt.gcf()
ax.coastlines()
#plt.tricontourf(df["longitude"], df["latitude"], np.clip(df["temperature"], min_tmp, max_tmp), cmap=viridis, vmin=min_tmp, vmax=max_tmp)
plt.scatter(lon, lat, c=tmp_masked, marker=".", linewidths=0, s=1)
plt.colorbar(orientation="horizontal")
plt.title("Temperatur in °C 30. / 31. 12. 2020")
plt.savefig("temperature.png", dpi=1200)
# %% codecell
