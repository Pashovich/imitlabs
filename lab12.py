
import random, math

class Team:
    def __init__(self, name):
        self.name = name
        self.playing = True
    def lose(self):
        self.playing = False
class Game:
    inten = 2 
    teamList = []


    def __init__(self,commands):
        self.makeTeams(commands)
        self.play()
    def makeTeams(self,amount):
        for i in range(amount):
            self.teamList.append(Team(str(i+1)))

    def randomScore(self):
        M = 0
        S = 0
        alfa = random.uniform(0,1)
        S+= math.log(alfa)
        M+=1
        while S>= self.inten * -1:
            alfa = random.uniform(0,1)
            S+= math.log(alfa)
            M+=1
        return M
    def penaltySeries(self):
        return random.randint(1,5)
    def eliminateTeams(self):
        temp = []
        for item in self.teamList:
            if item.playing == True:
                temp.append(item)
        return temp

    def play(self):
        for i in range(len(self.teamList)):
            if (i+1) % 2 == 0:
                firstTeamScore = self.randomScore()
                secondTeamScore = self.randomScore()
                print(f"Team {self.teamList[i-1].name} Team {self.teamList[i].name} \nscore {firstTeamScore} :  score {secondTeamScore}")
                if firstTeamScore > secondTeamScore:
                    self.teamList[i].lose()
                elif firstTeamScore == secondTeamScore:
                    pen1 = self.penaltySeries()
                    pen2 = self.penaltySeries()
                    while pen1 == pen2:
                        pen1 = self.penaltySeries()
                        pen2 = self.penaltySeries()
                    print()
                    print(f"Team {self.teamList[i-1].name} : Team {self.teamList[i].name} \nPenalty score {pen1} :  Penalty score {pen2}")
                    if pen1 >= pen2:
                        self.teamList[i].lose()
                    else:
                        self.teamList[i-1].lose()
                else:
                    self.teamList[i-1].lose()
                print()
        self.teamList = self.eliminateTeams()
        if len(self.teamList) == 1:
            print(f"Team {self.teamList[0].name} won")
            return
        self.play()


Game(8)