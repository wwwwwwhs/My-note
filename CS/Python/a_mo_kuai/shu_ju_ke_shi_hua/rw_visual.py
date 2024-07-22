'''
Author: 崩布猪
Date: 2024-04-18 20:58:31
LastEditors: 崩布猪
LastEditTime: 2024-04-21 16:40:50
FilePath: \shu_ju_ke_shi_hua\rw_visual.py
Description: 随机漫步的实例化图标

'''
import matplotlib.pyplot as plt
from sui_ji_man_bu import RandomWalk

# 创建一个RandomWalk实例
""" rw = RandomWalk()
rw.fill_walk()

# 绘制随机漫步的路径
plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values,rw.y_values,s=15,c=rw.y_values,cmap=plt.cm.gray)
plt.show() """

# 模拟多次随机漫步
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig,ax = plt.subplots(figsize=(16,10),dpi = 128) # 设置画布大小 单位英寸 但是可以通dpi 传递分辨率

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # 绘制随机漫步的路径 并且很具先后顺序颜色映射
    point_numbers = range(rw.num_points)
    
    # 15-3
    # ax.plot(rw.x_values,rw.y_values,c='gray',lw=1)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    # ax.plot(rw.x_values,rw.y_values,c='gray',lw=1)
    # # 突出起点和终点
    # ax.scatter(0,0,c='green',edgecolors='none',s=100)
    # ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.show()

   

    # 询问是否继续随机漫步
    # keep_running = input("Make another walk? (y/n): ")
    # if keep_running == 'n':
    break