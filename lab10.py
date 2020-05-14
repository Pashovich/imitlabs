import random

hardMode = [0.1,0.1,0.1,0.2,0.2,0.2]
normalMode = [0.1,0.1,0.1,0.2,0.2,0.3]
answersReplics = {
    'win': 'You won',
    'lose' : 'You lost',
    'hardWin' : "Can't belive you won",
    'draw' : "It's a draw"
}

def run(probas):
    A = random.uniform(0, 1)
    k = 0
    for item in probas:
        A = A - probas[k]
        if A <= 0:
            return k
        k+=1

def main():
    answers = [1,2,3,4,5,6]

    hardModeCheck = {
        'yes' : hardMode,
        'no' : normalMode
    }

    mode = input('hard mode? (yes/no) : \n')

    modeList = hardModeCheck.get(mode,0)
    winAnswer = answersReplics['win'] if mode !=0 else answersReplics['hadWin']

    if modeList == 0:
        exit(1)
    
    player =answers[run(normalMode)]
    oponent = answers[run(modeList)]
    print('your drop', player)
    print('computer drop',oponent )
    if player > oponent:
        print(winAnswer)
    elif player == oponent:
        print(answersReplics['draw'])
    else:
        print(answersReplics['lose'])

    

if __name__ == "__main__":
    main()