import numpy as np
import pandas as pd
import util
from matplotlib import pyplot as plt
from cartopy import crs as ccrs
import matplotlib as mpl

mpl.rcParams['agg.path.chunksize'] = 100000000

lat, lon, time = util.get_data_from_folder("data", "tb_time_seconds")

df = pd.DataFrame()
df["latitude"] = lat
df["longitude"] = lon
df["time"] = time
df = df[::1000] 
df.set_index("time")
df.sort_index(inplace=True)
print(f"Collected Data of size {df.size}")

print("Plotting...")
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

plt.plot(df["longitude"], df["latitude"])
plt.savefig("journey.png", dpi=1200)
