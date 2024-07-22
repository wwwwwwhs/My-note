# for in
sum = 0
for i in [1, 2, 3, 4, 5, 6]:
    sum += i
print(sum)


sum = 0
for i in range(101):
    sum += i
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for i in range(len(L)):
    print('hello,' + L[i] + '!')

# break continue 尽量不用

