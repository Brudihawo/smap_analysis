import pandas as pd
import h5py
import numpy as np
from cartopy import crs as ccrs
from matplotlib import cm
from matplotlib import pyplot as plt

from util import find_file_with_ending_recurse, get_data_from_folder

def plot_scatter_to_png(data_folder, key, colormap_name, filename, plot_title):
    # get data
    lat, lon, values = get_data_from_folder(data_folder, key)
    # Filter for min and max
    tmp = values.copy()
    tmp = tmp[tmp != -9999.0]
    min_val = tmp.min()
    max_val = tmp.max()

    # mask array for -9999.0 values (no data/ over water)
    m_tmp = np.ma.array(values)
    val_masked = np.ma.masked_where(m_tmp <= min_val, m_tmp)
    print("Data Acquisition Done")

    # Plotting
    plt.clf()
    ax = plt.axes(projection=ccrs.PlateCarree())

    fig = plt.gcf()
    ax.coastlines()
    plt.scatter(lon, lat, c=val_masked, marker=".", linewidths=0, s=0.5, cmap=colormap_name )
    plt.colorbar(orientation="horizontal")
    plt.title(plot_title)
    plt.savefig(filename, dpi=1200)

    print(f"Plotting done. Saved as {filename}.")
