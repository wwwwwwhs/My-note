# 迭代 字典
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

# 迭代字典的value 和 同时迭代
    
for value in d.values():
    print(value)

for k, v in d.items():
    print(k+":")
    print(v)

# 遍历字符串 
for ch in 'abcdef':
    print(ch)

print("==============================")

# 判断对象是否可以迭代 collections.abc 模块的 Iterable判断
from _collections_abc import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))
print(isinstance(123.23,Iterable))
