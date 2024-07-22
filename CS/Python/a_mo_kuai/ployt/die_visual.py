'''
Author: 崩布猪
Date: 2024-04-21 16:50:22
LastEditors: 崩布猪
LastEditTime: 2024-04-21 20:18:27
FilePath: \P_code\a_mo_kuai\ployt\die_visual.py
Description: 模拟色子

'''
from mo_ni_sai_zi import Die

from plotly.graph_objects import Bar,Layout
from plotly import offline


die = Die()

results = []

for roll in range(100):

    results.append(die.roll())

print(results)

# 分析结果
Frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    Frequencies.append(frequency)

# 对结果进行可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=Frequencies)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}

My_Layout = Layout(title ='投掷一个色子1000次的结果', xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': My_Layout},filename='d6.html')