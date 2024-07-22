<!--
 * @Author: 崩布猪
 * @Date: 2024-04-10 20:25:42
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-12 10:51:36
 * @FilePath: \P_code\Py_base\list.md
 * @Description: 本节用来演示 python 中的 数据结构类型
 * 
-->

# 列表 List
why
list 由一系列特定顺序排列的元素组成，可以包含不同类型的数据，可以动态增删元素。

### 列表的创建
list 的创建

```python
# 创建一个空列表
my_list = []

# 创建一个有初始值的列表
my_list = [1, 2, 3, 4, 5]

# 创建一个有初始值的列表，且元素类型为字符串
my_list = ['apple', 'banana', 'orange']
```

### 访问列表中的元素

```python
# 访问列表中的元素
my_list[0]   # 访问索引为 0 的元素
my_list[-1]  # 访问最后一个元素
```

### 修改列表中的元素

```python
# 修改列表中的元素
my_list[0] = 'pear'
```
### list 的操作

```python
# 向列表中末尾添加元素
my_list.append(x)

# 将 iterable 中的元素添加到列表中 / 用可迭代对象的元素扩展列表
list.extend(iterable)   

# 向列表中插入元素
my_list.insert(1, 'grape')

# 从列表中删除元素
my_list.remove('banana')     # 删除第一个 'banana' 元素
my_list.pop([i])              # 删除索引为 i 的元素
del my_list[i]               # 删除索引为 i 的元素
my_list.clear()                 # 清空列表

# 返回列表中第一给值位x的元素的零级索引 没找到出发ValueError异常
my_list.index(x[, start[, end]])    

# 返回列表中元素的个数
len(my_list)

# 就地排列列表中的元素
my_list.sort()

# 反转列表中的元素
my_list.reverse()

# 返回列表的浅浅拷贝
my_list.copy()
``` 


### 列表的遍历
for item in my_list:
    print(item)

### 列表的切片操作
my_list[1:3]   # 切片从索引 1 到 3 的元素
my_list[1:]    # 切片从索引 1 到末尾的元素
my_list[:3]    # 切片从开头到索引 3 的元素

### 遍历切片
``` python
for item in my_list[1:3]:
    print(item)

```
### 复制列表

```python
my_list_copy = my_list.copy()   # 复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
```
### 使用函数range()创建数字列表

```python
my_list = list(range(10))   # 创建一个 0-9 的列表
```
### 数字列表的一些函数
min(my_list)   # 返回列表中的最小值
max(my_list)   # 返回列表中的最大值
sum(my_list)   # 返回列表中的元素之和

### 列表解析

```python
my_list = [x**2 for x in range(10)]   # 创建一个 0-9 的列表，每个元素平方
```
语法：
首先指定一个描述性的列表名，然后使用方括号，然后在方括号中使用表达式来生成列表元素。表达式可以是任何可迭代对象，如 range() 函数，也可以是其他表达式。

# 元组

元组与列表类似，不同之处在于元组的元素不能修改。元组的创建方式与列表相同。

```python
my_tuple = (1, 2, 3, 4, 5)
```

### 元组的操作

```python
# 访问元组中的元素
my_tuple[0]

# 修改元组中的元素
my_tuple[0] = 'pear'   # TypeError: 'tuple' object does not support item assignment
my_tuple = (20, 30, 40) # 可以通过重新给存储元组的变量赋值修改变量

# 元组的遍历
for item in my_tuple:
    print(item)

# 元组的切片操作
my_tuple[1:3]

# 元组的复制
my_tuple_copy = my_tuple.copy()