from scipy.stats import expon
import threading
import random
import time


class Client:

	choicesList = ['сервис 1',
			'сервис 2 ',
			'сервис 3',
			'сервис 4',
			'сервис 5']
	def chooseServe(self):
		service = random.randint(0, len(self.choicesList)-1 )
		print('service', self.choicesList[service])
		return service


class  Window():
	
	def __init__(self):
		self.isFree = True

	def proccess(self, client):
		self.isFree = False
		print('start working with client')
		timeOnServe = expon.rvs(client.chooseServe())
		time.sleep(timeOnServe)
		self.isFree = True


class Modeling:
	def __init__(self):
		self.queue = list()
		self.windows = 5
		self.events = 100
		self.__lambda = 7
		self.start()

	def start(self):
		thread = threading.Thread(target = self.generateClientFlow, args = (self.__lambda, ))
		thread.start()
		windows = [Window() for _ in range(self.windows)]
		while True:
			while self.queue:
				print(f'still in queue : {self.queue}')
				free = [i for i in windows if i.isFree]
				if free:
					client = self.queue.pop()
					activeWindow = random.choice(free)
					activeWindow.proccess(client)
		thread.join()

	def generateClientFlow(self,lambd):
		while True:
			flowTimeSleep = expon.rvs(lambd)
			time.sleep(flowTimeSleep)
			self.queue.append(Client())
Modeling()