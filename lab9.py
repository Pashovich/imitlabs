import random
import matplotlib.pyplot as plt
import numpy as np


def run(answers):
    A = random.uniform(0, 1)
    k = 0
    for _ in answers:
        A = A - answers[k]
        if A <= 0:
            return k
        k+=1

def generateProbasRandom(n):
    tempList = []
    for _ in range(n-1):
        prob = round(random.uniform(0, 1 - sum(tempList)),5)
        tempList.append(prob)
    tempList.append(1-sum(tempList))
    return tempList
def getProbasFile(n):
    with open('probas.txt', 'r') as file:
        lines = file.readlines()
    lines = [float(item) for item in lines] 
    return lines

def main():
    n = 5
    funcs = {
        '1' : getProbasFile,
        '2' : generateProbasRandom
    }

    mode = input('mode : \n1 file \n2 random\n')
    N = int(input('Number of examples :  '))
    probaFunc = funcs.get(mode,0)
    if probaFunc == 0:
        exit(0)
    probabilities = probaFunc(n)
    y_pos = range(1,6)
    relust = np.zeros(n)
    for i in range(N):
        answ = run(probabilities)
        if answ !=-1:
            relust[answ]+=1
    
    relust = [item/N for item in relust]



    plt.bar(y_pos,relust, align='center', alpha = 0.5)
    plt.xticks(y_pos, y_pos)


    plt.show()

if __name__ == "__main__":
    main()