'''
Author: 崩布猪
Date: 2024-04-21 16:50:22
LastEditors: 崩布猪
LastEditTime: 2024-04-21 20:29:18
FilePath: \P_code\a_mo_kuai\ployt\dice_visual.py
Description: 模拟两个色子

'''
from mo_ni_sai_zi import Die

from plotly.graph_objects import Bar,Layout
from plotly import offline


die_1 = Die()
die_2 = Die(10)

# 投n此筛子 并将结果存储在一个列表中
results = []
for roll_num in range(1000):

    results.append(die_1.roll() + die_2.roll())

# 分析结果
Frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    Frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=Frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}

My_Layout = Layout(title ='投掷两个色子1000次的结果', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': My_Layout},filename='d6.html')