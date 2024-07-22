#将一个色子投N次 统计没用点数出现的次数
import random
counters = [0] * 6
for _ in range(600):
    face = random.randrange(1,7)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
