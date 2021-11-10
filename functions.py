import random

c1 = random.normalvariate(9, 3)
c2 = random.normalvariate(7, 5)
c3 = random.normalvariate(11, 7)

def exploreonly() -> int:
    result = 0
    for i in range(100):
        result += c1
        result += c2
        result += c3
    return int(result)

print(exploreonly())