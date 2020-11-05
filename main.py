#importing the class here
import random
from stateClass import State
#using main since i definded classes to use
def main():
    bidenTotalEv = []
    trumpTotalEv = []
    stateList = State()
    numIteration = int(input("Enter the number of times you like to iterate: "))
    for i in range(numIteration):
        finalPredictionList = []
        bidenEvList = []
        trumpEvList = []
        for data in stateList:
            if data[4] == 'Joseph R. Biden Jr.':
                bidenVote = float(data[8])
            if data[4] == 'Donald Trump':
                trumpVote = float(data[8])
            basePrediciton = bidenVote - trumpVote
            randomNoise = random.normalvariate(0.0,1.0)/2.0*3.0
            finalPrediction = basePrediciton + randomNoise
            finalPredictionList.append(finalPrediction)
        for i in finalPredictionList:
            if i > 0:
                bidenEvList.append(float(data[2]))
            else:
                trumpEvList.append(float(data[2]))
        bidenTotalEv.append(sum(bidenEvList))
        trumpTotalEv.append(sum(trumpEvList))
            
    print('Hope it was helpful, Bye!!')
if __name__ == "__main__":
    main()
