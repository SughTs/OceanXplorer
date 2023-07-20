# OceanXplorer项目（制作中）

欢迎来到OceanXplorer项目！这是一个用于处理和分析海洋数据（近海岸带水体叶绿素浓度分析）的Python项目。该项目使用xarray库来处理NetCDF格式的海洋数据文件，并提供了一些功能来可视化和分析这些数据。


此分支是一个气温分布展示图测试，数据来源https://crudata.uea.ac.uk/cru/data/temperature/#datdow  
因为数据清晰度太低，所以效果并不好


## 前置介绍

从数学上来说，netcdf(.nc)存储的数据就是一个多自变量的单值函数。用公式来说就是f(x,y,z,...)=value，函数的自变量x,y,z等在netcdf中叫做维(dimension)或坐标轴(axis)，函数值value在netcdf中叫做变量(Variables)。而自变量和函数值在物理学上的一些性质，比如计量单位(量纲)、物理学名称等等在netcdf中就叫属性(Attributes)。

## 安装要求

- Python 3.x
- xarray
- matplotlib

可以使用以下命令安装所需的依赖项(e.g.)：

```bash
pip install xarray matplotlib
```

## 如何使用

1. 克隆项目到本地：

```bash
git clone https://github.com/XXX
cd XXXX
```

2. 运行主程序：

```bash
python main.py
```

3. 按照程序提示输入要处理的数据文件路径。

4. 程序将读取数据文件，并根据用户选择进行数据处理和可视化。

## 功能

- 读取和处理NetCDF格式的海洋数据文件
- 可视化海洋数据，包括经纬度分布散点图、时间序列图等
- 分析海洋数据的统计信息

## 文件结构

```
项目/
    ├── main.py       # 主程序
    ├── ocean_data.nc # 示例海洋数据文件
    ├── utils.py      # 工具函数
    ├── requirements.txt  # 依赖项列表
    └── README.md     # 项目说明文档
```

## 数据来源

NASA Goddard Space Flight Center, Ocean Ecology Laboratory, Ocean Biology Processing Group

## 版权信息

本项目使用 [MIT](LICENSE) 许可证，详情请参阅LICENSE文件。

## 贡献

欢迎贡献代码和提出问题！请提交问题和建议到项目的ISSUE。如果您希望贡献代码，请提交Pull请求。

如果您对项目有任何疑问，请随时联系我们(邮箱请自行搜索)。

**感谢您的支持和参与！**
