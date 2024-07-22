list1 = ['whs', 'wasd', 'list']
list2 = [1,2,3,4,5,6,7,8]

#可以用+拼接
print(list1 + list2)

#用*重复运算
print(list1 * 3)

#用in或not in 判断元素在不在列表中
print('whs' in list1)
print('whs' not in list1)

#访问列表中多个元素 利用切片运算
#[start:end:stride] stride:跨度
print(list2[0:3:2])

#=====================
# len（）函数
print(len(list1))
# 索引选择元素
print(list1[0])
print(list1[-1])
# append（） 添加元素
list1.append('aa')
# insert() 插入元素
list1.insert(1, 'insert')
print(list1)
# pop() 删除末尾的袁旭
list1.pop()
list1.pop(1)
print(list1)
# remove 删除指定元素
# tuple
t = (1,2)
t = ()
t = (1,)