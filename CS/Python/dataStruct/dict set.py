# 字典  键-值 dict
d = {'title': 'lover', 'author': 'talor swift'}
d['title'] = 'Cruel Summer'
print(d)
#  判断key存在的方法
print('Style' in d)
print(d.get('Style', -1))
print(d.get('title'))
print(d.get('Style', -1))
# pop() remov
d.pop('author')
print(d)
print('======================"')
# set 没有value
s = set([1,2,3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)
s2 = set([2,3,4])

print(s & s2)
print(s | s2)