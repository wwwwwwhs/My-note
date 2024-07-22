'''
Author: 崩布猪
Date: 2024-04-16 10:23:52
LastEditors: 崩布猪
LastEditTime: 2024-04-18 20:42:14
FilePath: \P_code\shu_ju_ke_shi_hua\mpl_squares.py
Description: 

'''
import matplotlib.pyplot as plt # 导入matplotlib.pyplot模块并重命名为plt
""" 
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来设置图表显示中文标签的字体为SimHei
plt.rcParams['axes.unicode_minus'] = False # 用来设置图表显示负号

x = [1,2,3,4,5]  # 定义x轴数据
xEnd = [1, 4, 9, 16, 25] # 定义x轴结束位置

# 内置样式 创建之前设置  参考https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('ggplot')  # 设置图表样式为ggplot

fig,ax = plt.subplots()  # 创建一个图表和一组子图

ax.plot(x,xEnd,color='r',linewidth=3)  # 在子图上绘制x的平方图像，设置线宽为3

# 设置图标标题 并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)  # 设置图表标题为"平方数"，字体大小为24
ax.set_xlabel("数值",fontsize=14)  # 设置x轴标签为"数值"，字体大小为14
ax.set_ylabel("平方",fontsize=14)  # 设置y轴标签为"平方"，字体大小为14

#设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)  # 设置刻度标记的大小为14

plt.show()  # 显示图表 
 """
"""使用scatter方法绘制散点图"""
""" plt.style.use('seaborn-v0_8')  # 设置图表样式为seaborn)
# print(plt.style.available) # 查看可用的样式
fig,ax=plt.subplots()  # 创建一个图表和一组子图
ax.scatter(2,4)

plt.show()  # 显示图表
"""

# # 绘制一系列点
plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来设置图表显示中文标签的字体为SimHei
plt.rcParams['axes.unicode_minus'] = False # 用来设置图表显示负号

# 自动计算数据
x_data = list(range(1,1001))
y_data = [x**2 for x in x_data]
plt.style.use('seaborn-v0_8')

# 内置样式 创建之前设置  参考https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# plt.style.use('ggplot')  # 设置图表样式为ggplot

fig,ax = plt.subplots()  # 创建一个图表和一组子图

# ax.plot(x_data,y_data,c=(0,0.3,0.5),linewidth=3)  # 在子图上绘制x的平方图像，设置线宽为3 颜色为红 red 或者rgb（0,0,0）
# 颜色映射：https://matplotlib.org/stable/tutorials/colors/colormaps.html 颜色用于突出数据的规律
ax.scatter(x_data,y_data,c=y_data,cmap=plt.cm.Blues,s=10)  # 在子图上绘制散点图，颜色映射为蓝色，大小为10

# 设置图标标题 并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)  # 设置图表标题为"平方数"，字体大小为24
ax.set_xlabel("数值",fontsize=14)  # 设置x轴标签为"数值"，字体大小为14
ax.set_ylabel("平方",fontsize=14)  # 设置y轴标签为"平方"，字体大小为14
ax.tick_params(axis='both', labelsize=14)  # 设置刻度标记的大小为14
ax.axis([0,1100,0,1100000])
plt.show()  # 显示图表 

plt.savefig("squares.png",bbox_inches='tight')  # 保存图片 并将图标多余的空白区域减裁掉
