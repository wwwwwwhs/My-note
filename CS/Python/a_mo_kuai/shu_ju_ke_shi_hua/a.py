'''
Author: 崩布猪
Date: 2024-04-21 16:29:05
LastEditors: 崩布猪
LastEditTime: 2024-04-21 16:40:20
FilePath: \shu_ju_ke_shi_hua\a.py
Description: 

'''
import matplotlib.pyplot as plt
from sui_ji_man_bu import RandomWalk


# 创建随机漫步实例
rw = RandomWalk(50000)
rw.fill_walk()

# 绘制随机漫步
plt.style.use('classic')
number = range(rw.num_points)
# plt.plot(rw.x_values, rw.y_values, linewidth=0)
plt.scatter(rw.x_values, rw.y_values, c=number, cmap =plt.cm.Blues, edgecolors='none', s=10)


# 设置图表标题并给坐标轴加上标签
plt.title("Random Walk")
plt.xlabel("Steps")
plt.ylabel("Distance")


# 显示图表
plt.show()