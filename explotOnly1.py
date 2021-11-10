import random

def exploitOnly():
    # Hx means the average happiness per cafeteria (x)

    h1 = 9
    h2 = 7
    h3 = 11
    std1 = 3
    std2 = 5
    std3 = 7
    happinesstemp=0

    hap1 = random.normalvariate(h1, std1)
    hap2 = random.normalvariate(h2, std2)
    hap3 = random.normalvariate(h3, std3)

    if hap1 > hap2 and hap1 > hap3:
        for i in range(296):
            happinesstemp += random.normalvariate(h1, std1)
        happiness = happinesstemp + hap2 + hap3 + hap1
        return happiness
    elif hap2 > hap1 and hap2 > hap3:
        for i in range(296):
            happinesstemp += random.normalvariate(h2, std2)
        happiness = happinesstemp + hap2 + hap3 + hap1
        return happiness
    elif hap3 > hap1 and hap3 > hap2:
        for i in range(296):
            happinesstemp += random.normalvariate(h3, std3)
        happiness = happinesstemp + hap2 + hap3 + hap1
        return happiness
  
  
