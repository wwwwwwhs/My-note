<!--
 * @Author: 崩布猪
 * @Date: 2024-04-12 11:27:48
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-12 15:20:55
 * @FilePath: \P_code\Py_base\main.md
 * @Description: 
 * 
-->
# 函数

## 定义函数

```python
def my_function(x):  # 定义函数名为 my_function，参数为 x
    return x + 1  # 函数返回 x+1 的结果
```
## 实参和形参

- 实参（argument）：调用函数时传入的参数。
- 形参（parameter）：函数定义时定义的参数。
- 传递实参：实参的值会被复制到函数的局部变量中，因此函数内对形参的修改不会影响实参的值。
- 位置实参：按照函数定义时的顺序来传递实参。
- 关键字实参：按照参数名来传递实参，关键字实参必须在位置实参之后。
- 默认参数：函数定义时可以指定参数的默认值，当调用函数时，如果没有传入相应的参数，则使用默认值。

## 调用函数 

```python
result = my_function(5)  # 调用函数 my_function，传入参数 5
print(result)  # 输出结果 6
```

## 带有默认参数的函数

```python
def my_function(x, y=10):  # 定义函数名为 my_function，参数为 x 和 y，y 的默认值为 10
    return x + y  # 函数返回 x+y 的结果
```

## 调用带有默认参数的函数

```python
result = my_function(5)  # 调用函数 my_function，传入参数 5
print(result)  # 输出结果 15

result = my_function(5, 20)  # 调用函数 my_function，传入参数 5 和 20
print(result)  # 输出结果 25
```

# 返回值

函数可以返回一个值，这个值可以是任意类型，包括数字、字符串、列表、元组、字典等。

```python
def my_function(x):
    return x + 1       
```

### 让实参变成可选参数，可以让函数更灵活。

### 函数可以返回字典

### 函数可以传递列表

```python
def my_function(lst):
    return lst + [10]


my_list = [1, 2, 3]
result = my_function(my_list)
print(result)  # [1, 2, 3, 10]
```

### 也可可以在函数中修改列表

```python
def my_function(lst):
    lst.append(10)
    return lst

my_list = [1, 2, 3]
result = my_function(my_list)
print(result)  # [1, 2, 3, 10]
```

### 禁止函数修改列表

```python
def my_function(lst):    
    lst = lst + [10]
    return lst

my_list = [1, 2, 3]
result = my_function(my_list)
print(result)  # [1, 2, 3, 10]
print(my_list)  # [1, 2, 3]
``` 

# 将函数储存在模块中

可以将函数储存在模块中，这样可以更方便地调用函数。

```python
# my_module.py

def my_function(x):
    return x + 1
```

# 导入模块

1. 导入整个模块
```python
# 创建模块 pizza.py
def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# 导入模块
# 在同一个目录中 创建了 my_script.py 文件，可以导入 pizza.py 模块。
import pizza

pizza.make_pizza("16", "pepperoni", "mushrooms", "green peppers")
pizza.make_pizza("12", "green peppers", "mushrooms", "green peppers")

```

2. 导入模块中的特定函数
```python
from pizza import make_pizza

make_pizza("16", "pepperoni", "mushrooms", "green peppers")
make_pizza("12", "green peppers", "mushrooms", "green peppers")
```

3. 使用as给模块或函数指定别名

```python
import pizza as p

p.make_pizza("16", "pepperoni", "mushrooms", "green peppers")
p.make_pizza("12", "green peppers", "mushrooms", "green peppers")
```
4. 导入模块中的所有函数

```python
from pizza import *

make_pizza("16", "pepperoni", "mushrooms", "green peppers")
make_pizza("12", "green peppers", "mushrooms", "green peppers")
```

函数编写指北:

- 函数名应该是小写的单词，用下划线连接。
- 函数名应该描述函数的作用。
- 每个函数都应包含简要阐述功能的注释
- 注释紧跟在函数的定义后面并且使用文档字符串的格式。
- 给形参指定默认值的时候等号两边不要有空格
- 函数调用中的关键字实参，也要遵守这种约定