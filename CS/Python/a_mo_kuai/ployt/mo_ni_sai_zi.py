'''
Author: 崩布猪
Date: 2024-04-21 16:45:04
LastEditors: 崩布猪
LastEditTime: 2024-04-21 16:47:36
FilePath: \P_code\a_mo_kuai\ployt\a.py
Description: Plotly 可以生成交互式图标 需要创建在浏览器中显示的图表的时候 Plotly 非常有用

'''
from random import randint

class Die:
    '''表示一个筛子的类'''
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        '''随机返回一个1到骰子面数之间的数字'''
        return randint(1, self.num_sides)
