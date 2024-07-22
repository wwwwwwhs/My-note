<!--
 * @Author: 崩布猪
 * @Date: 2024-04-12 10:58:21
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-12 11:27:31
 * @FilePath: \P_code\Py_base\dictionary.md
 * @Description: 
 * 
-->
# 字典（Dictionary）

字典是另一种可变容器模型，且可存储任意类型对象。字典用键-值（key-value）对存储数据，其中键必须是唯一的。


## 创建字典

创建字典的方法有两种：

1. 使用字典字面量语法：

```python    
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_text = {'color': 'blue', 'age': '27'}
alien_0 = {} # 空字典
```

2. 使用 dict() 函数：

```python
my_dict = dict(key1='value1', key2='value2')
```
较长字典的创建格式

```python
my_dict = {
    'key1': 'value1',  
    'key2': 'value2',
    'key3': 'value3',
    'key4': 'value4',
    }   
```
## 访问字典元素

访问字典元素的方法有两种：

1. 使用键访问：

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])  # 输出 'value1'
```

2. 使用 get() 方法：

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict.get('key1'))  # 输出 'value1'
print(my_dict.get('key3'))  # 输出 None
```

## 修改字典元素

修改字典元素的方法有两种：

1. 使用键赋值：

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict['key1'] = 'new_value1'
print(my_dict)  # 输出 {'key1': 'new_value1', 'key2': 'value2'}
```

2. 使用 update() 方法：


```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update(key1='new_value1')
print(my_dict)  # 输出 {'key1': 'new_value1', 'key2': 'value2'}
```

## 删除字典元素

删除字典元素的方法有两种：

1. 使用 del 语句：


```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict['key1']
print(my_dict)  # 输出 {'key2': 'value2'}
```

2. 使用 pop() 方法：


```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.pop('key1')
print(my_dict)  # 输出 {'key2': 'value2'}
```

## 遍历字典

遍历字典的方法有两种：

1. 使用 for 循环：

```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
for key in my_dict:
    print(key, my_dict[key])
```

2. 使用 items() 方法：


```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
for key, value in my_dict.items():
    print(key, value)
```
## 字典方法

- clear()：清空字典
- copy()：复制字典
- fromkeys()：创建指定键的字典
- get()：获取指定键的值
- items()：获取字典所有键值对
- keys()：获取字典所有键
- pop()：删除指定键的值
- popitem()：随机删除一个键值对
- setdefault()：设置默认值
- update()：更新字典
- values()：获取字典所有值

## 字典函数

- dict()：将序列转换为字典
- len()：获取字典长度
- max()：获取字典中最大值
- min()：获取字典中最小值
- sorted()：对字典排序  
- set(): 创建集合 集合中的每个元素都必须是唯一的

# 嵌套

字典可以嵌套，即一个字典的值可以是另一个字典。

```python   

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Beijing',
    'pets': {
        'dog': 'Rufus',
        'cat': 'Fluffy',
        'fish': 'Nemo'
    }
}

print(my_dict['pets']['dog'])  # 输出 'Rufus'
```

## 字典列表
``` python
alien_0 = {'name': 'Alien-0', 'age': 100, 'city': 'Unknown'}
alien_1 = {'name': 'Alien-0', 'age': 100, 'city': 'Unknown'}
alien_2 = {'name': 'Alien-0', 'age': 100, 'city': 'Unknown'}

aliens = [alinen_0, alinen_1, alinen_2]

for alien in aliens:
    print(alien)
```
## 在字典中存储列表
``` python
my_dict = {'numbers': [1, 2, 3, 4, 5]}
print(my_dict['numbers'])  # 输出 [1, 2, 3, 4, 5]
```