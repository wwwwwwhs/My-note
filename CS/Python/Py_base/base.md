# 注释 
单行 \#
多行注释
'''
'''
或者
"""
"""

# 变量
变量命名规则
- 数字字母下划线
- 字母下划线开头
- 不能包含空格但是可以用下划线分隔其中的单词
- 不适用Python关键字和内置函数名用作变量名
- 变量名尽量简短，便于理解
- 
<b>惯例</b>
变量名通常使用小写英文字母,多个单词用下划线进行连接
受保护的变量用单个下划线开头
私有的变量用两个下划线开头

预习 变量时可以复制给值得标签

整形 int
浮点型 float 科学计数法 123.456 == 1.23456 * 15^2 
字符串行 str 'hello' '这合理吗'
布尔型 bool True False

**字符串方法**
.title()  首字母大写
.upper()  全部大写
.lower()  全部小写
.rstrip()  去除右边空格
.lstrip()  去除左边空格
.strip()   去除两边空格

**字符串中使用变量**
``` python
first_name = 'Alice'
last_name = 'Smith'
full_name = first_name +'' + last_name
full_name01 = d"{diear_name} {last_name}"
print(full_name)
print(f'Hello,{full_name01.title()}')
```

数中的下划线
在写很大的数时侯，为了便于阅读，可以用下划线分隔数字，如：
```python
income = 1_234_567_890
print(income)
```

# 常量
常量是指不能被修改的变量，通常用全部大写字母表示，
如PI = 3.141592653589793

# 运算符

\+ - * / % 
\> >= < <=
== !=
// 整除
<< >> 左移 右移
[] 索引
[:] 切片
** 幂
~ + - 按位取反 正号,负号
& 按位与
^ 按位异或
| 按位或

is | is not 身份运算符
in | not in 成员运算符
not or and 逻辑运算符
= += -= *= /= %= //= **= &= |= ^= <<= >== 复制运算符

# 分支结构
if
elif
else
and or 
in not
# 循环结构
for in 循环
rang(101)
while 循环

# 函数
- 定义 def  
- 函数的参数
  - 在python中函数的参数可以有默认值，也支持可变参数例子
  - ```python
    from random import rand

    def roll_dice(n = 2):
        #摇色子
        total = 0
        for _ in range(n)
            total += randint(1,6)
        return total
    
    def add(a = 0, b = 0 c = 0):
        #三个数相加
        return a + B + c
    # 如果没有指定参数那么使用默认值摇两颗色子
    print(roll_dice())
    # 摇三颗色子
    print(roll_dice(3))
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    # 传递参数时可以不按照设定的顺序    进行传递
    print(add(c=50, a=100, b=200))
  - ```python
        def add(*args):
          total = 0
            for val in args:
              total += val
            return total


        # 在调用add函数时可以传入0个或多个参数
        print(add())
        print(add(1))
        print(add(1, 2))
        (add(1, 2, 3))
        print(add(1, 3, 5, 7, 9))
- 函数模块化
  - 可以用global 关键字来表示局部变量如a 来字 全局变量中的a


