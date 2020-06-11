import math
import random
import matplotlib.pyplot as plt
import numpy as np


class Wheather:
        
    peroid = 3
    coefs = [[-0.4, 0.3, 0.1],#sun
                    [0.4, -0.8, 0.4],#cloudy
                    [0.1, 0.4, -0.5]] #somber

    def __init__(self):
        n = 10
        self.array = [0, 0, 0] 
        self.start(n)

    def start(self,days):
        _, axs = plt.subplots(days//5, 5, figsize=(9, 3), sharey=True)
        hour = 0
        for j in range(days):
            hour = 0
            try:
                now = values[-1]
            except :
                now = 0
            values = list()
            while hour<=24:
                values.append(now)
                now = random.choices(range(3), weights=self.coefs[now])[0]
                hour += 1
                axs[j//5][j%5].plot(range(hour), values)
                axs[j//5][j%5].set_title(f'День {j+1}')
            
            for w in range(3):
                self.array[w] += (values.count(w))
        
        plt.show()
        self.array = [i/days/24 for i in self.array]
        print(self.array)


Wheather()
