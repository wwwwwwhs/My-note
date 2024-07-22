# 去除字符串首尾的空格
def trim(s):
    # if len(s) > 0:
    #     i = 0
    #     while s[i] ==' ' and i < len(s):
    #         i += 1
    #     s = s[i:]
    #     j = len(s) - 1
    #     while s[j] == ' ' and  j >i:
    #         j -= 1
    #     s = s[:j+1]
    # return s
# ================================================
    length = len(s)
    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break
        j = length -1
        while s[j] == ' ' and j >= i:
            j -=1
        s = s[i:j+1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

