import xarray as xr
import pprint
import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from mpl_toolkits.basemap import Basemap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ncfilename = 'HadCRUT.5.0.1.0.analysis.anomalies.ensemble_mean.nc'
#xarray读入，xarray库有可能出现不兼容的问题。s
data = xr.open_dataset(ncfilename)#文件名，用相对地址
all_attributes = data.attrs
#netCDF4读入
dataset = nc.Dataset(ncfilename)
print("Dimensions:")
print(dataset.dimensions)
print("\nVariables:")
print(dataset.variables)
print("\nAttributes:")
print(dataset.__dict__)
print("---------------")


output_filename = 'nc_file_info.txt'
with open(output_filename, 'w') as f:
    pprint.pprint(data, stream=f)

print(f"Dataset信息已保存到文件：{output_filename}")
with open('attributes.txt', 'w') as f:
    for key, value in all_attributes.items():
        f.write(f"{key}: {value}\n")

print("属性信息已保存到 attributes.txt 文件中。")
#上面这一部分是打印.nc文件的参数

#地图绘制
#定义数据
lat = dataset.variables['latitude'][:]
lon = dataset.variables['longitude'][:]
temp = dataset.variables['tas_mean'][:, :, :]
time = dataset.variables['time'][:]
#创建地图
plt.figure(figsize=(10, 6))
m = Basemap(projection='cyl', resolution='l', llcrnrlat=lat.min(), urcrnrlat=lat.max(), llcrnrlon=lon.min(), urcrnrlon=lon.max())
m.drawcoastlines()
m.drawcountries()
m.drawparallels(np.arange(lat.min(), lat.max(), 10), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(lon.min(), lon.max(), 20), labels=[0, 0, 0, 1])
#静态图
lons, lats = np.meshgrid(lon, lat)
x, y = m(lons, lats)
clevs = np.linspace(temp.min(), temp.max(), 20)  # 温度等值线间隔
cs = m.contourf(x, y, temp[0, :, :], clevs, cmap='coolwarm')
plt.colorbar(cs, label='Temperature (K)')
plt.title('Spatial Distribution of Temperature')
plt.show()

# GUI
# Get the time variable from the dataset
time_variable = dataset['time']

# Get the size of the time dimension
time_dimension_size = len(time_variable)

# Get the timestamps for each time step
timestamps = nc.num2date(time_variable[:], units=time_variable.units, calendar=time_variable.calendar)

# Create the GUI window
root = tk.Tk()
root.title("Temperature Distribution Visualization")
root.geometry("800x600")

# Create a frame to hold the slider, plot, and timestamp
frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

# Create the slider
slider = ttk.Scale(frame, from_=0, to=time_dimension_size - 1, length=600, orient="horizontal")
slider.pack()

# Create the timestamp label
timestamp_label = ttk.Label(frame, text="")
timestamp_label.pack()

# Create the plot
fig, ax = plt.subplots()
temperature_map = dataset['tas_mean'][0]  # Display the first time step by default
ax.imshow(temperature_map, cmap='jet', origin='lower', extent=(0, 360, -90, 90))
ax.set_title('Temperature Distribution')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')


# Update the plot and timestamp
def update_plot_and_timestamp(time_index):
    #用多了卡得不行，记得清理内存
    ax.clear()

    time_index = int(time_index)
    temperature_map = dataset['tas_mean'][time_index]
    ax.imshow(temperature_map, cmap='jet', origin='lower', extent=(0, 360, -90, 90))
    ax.set_title('Temperature Distribution')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    # Get the timestamp corresponding to the selected time step
    timestamp_value = timestamps[time_index]
    timestamp_label.config(text=f"Timestamp: {timestamp_value}")

    canvas.draw()


# Callback function when the slider is changed
def on_slider_change(value):
    time_index = float(value)
    update_plot_and_timestamp(time_index)


# Bind the callback function to the slider
slider.config(command=on_slider_change)

# Put the plot into the Canvas and display it on the GUI window
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack()


# Main function
def main():
    root.mainloop()


if __name__ == "__main__":
    main()