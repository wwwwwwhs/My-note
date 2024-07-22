
"""
Author: 崩布猪
Date: 2024-04-18 20:49:49
LastEditors: 崩布猪
LastEditTime: 2024-04-21 16:13:09
FilePath: \shu_ju_ke_shi_hua\sui_ji_man_bu.py
Description: 随机漫步：每次行走都是完全随机的、没有明确的方向,结果是由一系列随机角色决定的。
定义的 随机漫步类
实例化请看 rw_visual.py
"""

from random import choice


class RandomWalk:
    """生成一个随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步的数据始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """随机选择一个方向并返回一步的坐标"""
        
        # 决定前进方向并计算下一个点
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3])

        step = direction * distance

        # 拒绝原地踏步
        if step == 0:
            return self.get_step()
        # 计算下一个点的坐标
        # next_x = self.x_values[-1] + x_step

        # return next_x
        

        return step

    def fill_walk(self):
        """计算随机漫步的包含的所有点"""
        # 不断漫步直到列表达到指定长度
        while len(self.x_values) < self.num_points:
            x_step = self.x_values[-1] + self.get_step()
            y_step = self.y_values[-1] + self.get_step()
            self.x_values.append(x_step)
            self.y_values.append(y_step)
