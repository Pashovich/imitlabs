import random
import math
import matplotlib.pyplot as plt


SIGMA = 1.0


class Currency:
    
    def __init__(self, startState, sigma):
        self.prices = [startState]
        self.__sigma = sigma
        self.isRising = False
        self.leftBorder = 0
        self.rightBorder = 5
        
    def modeling(self):
        trend = random.randint(self.leftBorder, self.rightBorder)/10
        new = self.prices[-1]* math.exp(trend - (self.__sigma**2)/2 + self.__sigma*random.random())
        self.prices.append(new)
        return new
    
    def getDots(self):
        return self.prices

    def changeTrand(self):
        if self.isRising == True:
            self.leftBorder = -5
            self.rightBorder = 0
        else:
            self.leftBorder = 0
            self.rightBorder = 5
            
class Modeling():
    def __init__(self):
        daysAmount = int(input("Days : "))
        start = int(input("Start price : "))
        self.start(daysAmount,start)

    def start(self, daysAmount, start):
        currency = Currency(start, SIGMA)
        x = [0]
        y = [currency.modeling()]
        for i in range(daysAmount):
            if i % 2 ==0:
                currency.changeTrand()
            plt.xlim(0, daysAmount -1)
            plt.plot(x, y)
            plt.pause(0.3)
            x.append(i+1)
            y.append(currency.modeling())
        plt.show()


    
Modeling()
