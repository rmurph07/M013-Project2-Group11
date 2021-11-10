# cafeteria 1: average happiness = 9, standard deviation = 3
# cafeteria 2: average happiness = 7, standard deviation = 5
# cafeteria 3: average happiness = 11, standard deviation = 7

import random

def exploreOnly() -> int:
    result = 0
    for i in range(100):
        result += random.normalvariate(9, 3)
        result += random.normalvariate(7, 5)
        result += random.normalvariate(11, 7)
    return int(result)

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

avg_caf1, std_caf1 = 9, 3
avg_caf2, std_caf2 = 7, 5
avg_caf3, std_caf3 = 11, 7
#establish the average happiness and standard deviation

def eGreedy(e: int):
    hap = 0
    ep = (e/100.0)
    caf1 = []
    caf2 = []
    caf3 = []
    #First day Caf 1
    caf1.append(random.normalvariate(avg_caf1, std_caf1))
    #Second day Caf 2
    caf2.append(random.normalvariate(avg_caf2, std_caf2))
    #Third Day Caf 3
    caf3.append(random.normalvariate(avg_caf3, std_caf3))

    #The rest of the days

    for i in range(297):
        r = random.random()

        if r < ep:
            cafpick = random.randint(1,3)

            if cafpick == 1: #if Caf 1 is the best
                caf1.append(random.normalvariate(avg_caf1, std_caf1))
            elif cafpick == 2: #if Caf 2 is the best
                caf2.append(random.normalvariate(avg_caf2, std_caf2))
            else: #if Caf 3 is the best
                caf3.append(random.normalvariate(avg_caf3, std_caf3))
        else:
            caf1avghap = sum(caf1)/len(caf1)
            caf2avghap = sum(caf2)/len(caf2)
            caf3avghap = sum(caf3)/len(caf3)
            if caf1avghap > caf2avghap and caf1avghap > caf3avghap:
                caf1.append(random.normalvariate(avg_caf1, std_caf1))
            elif caf2avghap > caf1avghap and caf2avghap > caf3avghap:
                caf2.append(random.normalvariate(avg_caf2, std_caf2))
            else:
                caf3.append(random.normalvariate(avg_caf3, std_caf3))
            #otherwise choose the best one

    return sum(caf1) + sum(caf2) + sum(caf3)

def Simulation(t:int, e:int):
    c1 = 9
    c2 = 7
    c3 = 11
    evalue = (e/100)
    oh = 3300
    exploretotal = 0
    exploittotal = 0
    egreedytotal = 0
    exploreexpected = 100*c1 + 100*c2 + 100*c3
    exploitexpected = c1 + c2 + c3 + 297*c3
    egreedyexpected = (1-evalue)*300*c3 + (evalue/3)*300*c1 + (evalue/3)*300*c2 + (evalue/3)*300*c3
    expexploreregret = oh - exploreexpected
    expexploitregret = oh - exploitexpected
    expegreedyregret = oh - egreedyexpected
    for i in range(t):
        exploretotal += exploreOnly()
        exploittotal += exploitOnly()
        egreedytotal += eGreedy(e)
    averageexplore = exploretotal/t
    averageexploit = exploittotal/t
    averageegreedy = egreedytotal/t
    avgexploreregret = oh - averageexplore
    avgexploitregret = oh - averageexploit
    avgegreedyregret = oh - averageegreedy
    print("Optimum Happiness:\nCafeteria 1: 2700\nCafeteria 2: 2100\nCafeteria 3: 3300\nOptimium: 3300\n")
    print("Expected Values:\nexploitOnly: Happiness: " + str(exploitexpected) + ", Regret: " + str(expexploitregret))
    print("exploreOnly: Happiness: " + str(exploreexpected) + ", Regret: " + str(expexploreregret))
    print("eGreedy: Happiness: " + str(egreedyexpected) + ", Regret: " + str(expegreedyregret) + "\n")
    print("Average Total Happiness:\nexploitOnly: " + str(averageexploit) + "\nexploreOnly: " + str(averageexplore)+ "\neGreedy: " + str(averageegreedy) + "\n")
    print("Average Regret:\nexploitOnly: " + str(avgexploitregret) + "\nexploreOnly: " + str(avgexploreregret) + "\neGreedy: " + str(avgegreedyregret))

