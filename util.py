import os
import numpy as np
import h5py


def find_file_with_ending_recurse(folder, ending):
    file_list = []
    for entry in os.scandir(folder):
        if entry.is_dir():
            file_list.extend(find_file_with_ending_recurse(entry.path, ending))

        if entry.name.endswith(ending):
            file_list.append(entry.path)
    return file_list

def get_data_from_folder(folder, key):
    lat = np.empty(0)
    lon = np.empty(0)
    val = np.empty(0)
    arrays = [lat, lon, val]
    idents = ["latitude", "longitude", key]
    h5_files = find_file_with_ending_recurse(folder, ".h5")
    print(f"Found {len(h5_files)} .h5 files in folder {folder}")
    for f in h5_files:
        h5_file = h5py.File(f, "r")
        am = h5_file["Soil_Moisture_Retrieval_Data_AM"]
        pm = h5_file["Soil_Moisture_Retrieval_Data_PM"]
        for i in range(3):
            arrays[i] = np.concatenate((arrays[i], np.array(am[idents[i]]).flatten()))
            arrays[i] = np.concatenate((arrays[i], np.array(pm[f"{idents[i]}_pm"]).flatten()))
    return arrays

def get_h5_metadata(file, dataset_name=None):
  if dataset_name: 
    h5data = h5py.File(file, "r")[dataset_name]
  else: 
    h5data = h5py.File(file, "r")

  return h5data.keys()
  
