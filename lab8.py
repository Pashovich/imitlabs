import random
import numpy as np
import scipy

def generateAnswer():
    return 'yes' if random.uniform(0,1) > 0.5 else 'no'



def makePredictionFromBall():
    answers = [('yes',0.2),('no',0.2),('i dont know',0.2),('could be',0.2), ('might be',0.2)]
    return run(answers)

def run(answers):
    A = random.uniform(0, 1)
    for item in answers:
        A = A - item[1]
        if A <= 0:
            return item[0]

def main():
    print(generateAnswer())
    print(makePredictionFromBall())



if __name__ == "__main__":
    main()