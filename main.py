import xarray as xr
import pprint
import matplotlib.pyplot as plt
def print_hi(name):
    print(f'Hi, {name}')
if __name__ == '__main__':
    print_hi('PyCharm')

data = xr.open_dataset('AQUA_MODIS.20230511T051001.L2.OC.NRT.nc')#文件名，用相对地址
# 获取所有层的名称
layers = data.keys()#Attributes
all_attributes = data.attrs
print(layers)
print("layers above")
print("---------------")
print(all_attributes)
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
