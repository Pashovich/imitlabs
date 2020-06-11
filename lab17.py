import random
import math
import time
import numpy as np

N = 10
T = 100
class PrimaryThread:
    
    def __init__(self, lambd):
        self.events = [math.log(random.random())/lambd]
        self.__lambd = lambd
        
    def getNextEventTime(self):
        nextEvent = self.events[-1] - math.log(random.random())/self.__lambd
        self.events.append(nextEvent)
        return nextEvent

    
    def getFullTime(self):
        return max(self.events)





class Modeling():

    def getMetrix(self,lambd, T, N):
        freq = dict()
        for _ in range(N):
            thread = PrimaryThread(lambd)
            while (thread.getFullTime() < T):
                thread.getNextEventTime()
            key = len(thread.events)
            if key not in freq.keys():
                freq.update({key: 1})
            else:
                freq[key] += 1

        return freq

    def __init__(self):
        lambda1 = int(input('lamba1 : '))
        lambda2 = int(input('lamba1 : '))
        self.start(lambda1,lambda2)

    def start(self,lambda1,lambda2):

        metrica1 = self.getMetrix(lambda1, T, N)
        metrica2 = self.getMetrix(lambda2, T, N)

        for key, value in metrica1.items():
            if key not in metrica2.keys():
                metrica2[key] = value
            else:
                metrica2[key] += value
        metrix2 = [i/N for i in metrica2.values()]
        metrica3 = self.getMetrix(lambda1+lambda2, T, N)
        metrica3 = [i/N for i in metrica3.values()]
        print('metrix', metrix2)
        print('metrix sum of lambda', metrica3)


Modeling()