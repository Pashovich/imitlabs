import random
import matplotlib.pyplot as plt
import numpy as np

a = 11.070

def run(answers):
    A = random.uniform(0, 1)
    k = 0
    for item in answers:
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
    
def calcMathAverege(xList, pList):
    return sum([ x*p for x,p in zip(xList,pList)])

def calcDispersion(xList, pList):
    xListSquared = [item * item for item in xList]
    mathAverege = calcMathAverege(xList,pList)
    dispersion = calcMathAverege(xListSquared,pList) - mathAverege*mathAverege
    return dispersion


def calcX(nList,pList, N):
    return sum([(n*n/(N*p)) for n, p in zip(nList,pList)]) - N

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
    
    frequency = [item/N for item in relust]

    mathAverege = calcMathAverege(y_pos,probabilities)
    dispersion = calcDispersion(y_pos,probabilities)
    mathAveregeE = calcMathAverege(frequency,y_pos)
    dispersionE = calcDispersion(y_pos, frequency)
    mathError = abs(mathAveregeE - mathAverege)
    dispersionError = abs(dispersionE - dispersion)
    print(mathError, dispersionError)
    chi = calcX(relust,probabilities,N)

    message = f"Average : {round(mathAverege,5)}(err = {round(mathError* 100)})\n\
    Variance : {round(dispersion,5)}(err = {round(dispersionError* 100)})\n\
    p-value : {chi} > {a} is {True if chi > a else False}"


    plt.bar(y_pos,frequency, align='center', alpha = 0.5)
    plt.xticks(y_pos, y_pos)
    plt.text(0.4,0.2,message,fontsize = 10)

    

    plt.show()

if __name__ == "__main__":
    main()