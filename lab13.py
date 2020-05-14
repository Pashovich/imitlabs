import random
import matplotlib.pyplot as plt
import numpy as np

a = 11.070
n = 4
def run(answers):
    A = random.uniform(0, 1)
    k = 0
    for item in answers:
        A = A - answers[k]
        if A <= 0:
            return k
        k+=1

def generateProbasRandom(proba,n):
    probs = [((1-proba)**i)*proba for i in range(n)]
    probs.append(1-sum(probs))
    print(probs)
    return probs
    
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
    p = float(input('p :  '))
    N = int(input('Number of examples :  '))
    probabilities = generateProbasRandom(0.6, n)
    y_pos = range(1,len(probabilities)+1)
    relust = np.zeros(len(probabilities))
    print(len(relust))
    for i in range(N):
        answ = run(probabilities)
        if answ !=-1:
            relust[answ]+=1
    
    frequency = [item/N for item in relust]
    print(len(y_pos), len(frequency))


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
    plt.text(2,0.5,message,fontsize = 10)
    
    plt.show()

if __name__ == "__main__":
    main()