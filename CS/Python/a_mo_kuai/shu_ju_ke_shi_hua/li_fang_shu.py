'''
Author: 崩布猪
Date: 2024-04-18 20:36:13
LastEditors: 崩布猪
LastEditTime: 2024-04-18 20:48:18
FilePath: \P_code\shu_ju_ke_shi_hua\li_fang_shu.py
Description: 绘制一个显示前5个整数的立方值 在绘制一个前5000个整数的立方值

'''
import matplotlib.pyplot as plt

x_date = list(range(1,5001))
y_data = [x**3 for x in x_date]

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.style.use('seaborn-v0_8') #设置绘图风格
# plt.plot(x_date, y_data,marker='o',markersize=5,color='r')
plt.scatter(x_date, y_data,c=y_data,cmap=plt.cm.Reds,s=100)
plt.title('前5个整数的立方值')
plt.xlabel('整数')
plt.ylabel('立方值')

plt.show()