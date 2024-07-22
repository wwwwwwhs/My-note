age = 20
if age >= 6:
    print('你还是个小屁孩')
elif age >= 18:
    print('成年人')
# 也会有类似于c语言短路状况

# input 返回str类型数据 int（） 转换

#  C 的switch结构 
#  python中 用match
ag = 10
match ag:
    case x if x < 10:
        print(f'<10 years old : {x}')
    case 10:
        print('10 years old')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 :
        print('11~18 years old.')
    case 19:
        print('19 years old')
    case _:
        print('not sure.')
#  复杂匹配
print('-- match list --')

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
    