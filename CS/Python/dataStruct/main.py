print(abs(100))
# 传入的参数数量或者类型不对 会报 TypeError错误
# 以直接从Python的官方网站查看文档：
# http://docs.python.org/3/library/functions.html#abs
# hex 返回一个16进制的整数



# 定义函数
def my_abs(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return
    else:
        return -x

print(my_abs(-200))

# 空函数 pass 用啦现在还没想好怎么写函数的代码 利用pass先占位的原理 其他语句也可用
def nop():
    pass

# 返回多个坐标

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

# 返回值 是一个 tuple


def quadratic(a, b, c):
    x1 = ( -b + math.sqrt(b * b - 4 * a * c) ) / (2 * a)
    x2 = ( -b - math.sqrt(b * b - 4 * a * c) ) / (2 * a)
    return x1,x2
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


