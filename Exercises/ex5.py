import random

a = random.sample(range(20),random.randint(5, 20))
b = random.sample(range(20),random.randint(5, 20))
c = []

size = 0

for i in a:
    if i in b:
        if i not in c:
            c.append(i)
print(a)
print(b)
print(c)
