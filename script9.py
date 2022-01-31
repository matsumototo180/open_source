import random
import collections

result = [random.randint(1, 6) for i in range(0, 100000)]
count = collections.Counter(result)
print(count)

progress = 0
for i in range(0, 20):
    roll = random.randint(1, 6)
    progress = min([progress + roll, 10])
    print(f'サイコロ：{roll} {progress}マス目' + (' ゴール！' if progress == 10 else ''))
    progress = int(str(progress)[-1])

