import random

def numberGen():
	return str(random.randint(1000, 10000))

def validation(randNum, usrNum):
	numOfCow = 0
	numOfBull = 0
	lenOfdigit = 4
	for x in range(0, lenOfdigit):
		for y in range(0, lenOfdigit):
			if((y == x) and (usrNum[y] == randNum[x])):
				numOfCow += 1
			elif((y == x) and (usrNum[y] != randNum[x])):
				numOfBull +=1
	numOfCow = str(numOfCow)
	numOfBull = str(numOfBull)
	return numOfCow, numOfBull


def usrInputAndOutput(randNum, stop):
	while(not stop) :
		print("number generated is " + randNum)
		usrNum = input("Enter a 4 digit number: ")
		numOfCow, numOfBull = validation(randNum, usrNum)
		print(numOfCow + " cows " + numOfBull + " bulls")
		if(int(numOfCow) == 4):
			stop = True
			print("Congrats you won!!!!!!")
# main program:
stop = False
randNum = numberGen()
print("Welcome to the cows and bulls game: ")
usrInputAndOutput(randNum, stop)
input("")