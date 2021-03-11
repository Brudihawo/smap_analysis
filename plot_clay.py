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

lat, lon, clay_content = get_data_from_folder("data", "clay_fraction")
# %% codecell
# Filter for min and max
tmp = clay_content.copy()
tmp = tmp[tmp != -9999.0]
min_clay = tmp.min()
max_clay = tmp.max()

m_tmp = np.ma.array(clay_content)
clay_masked = np.ma.masked_where(m_tmp <= min_clay, m_tmp)

# %% codecell
cmap = cm.get_cmap("copper", 100)
cmap.set_under(alpha=0)

# %% codecell

plt.clf()
ax = plt.axes(projection=ccrs.PlateCarree())

fig = plt.gcf()
ax.coastlines()
plt.scatter(lon, lat, c=clay_masked, marker=".", linewidths=0, s=0.5)
plt.colorbar(orientation="horizontal")
plt.title("Clay Content 30./31.12.2020")
plt.savefig("out.png", dpi=1200)
# %% codecell
