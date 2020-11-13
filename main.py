# #importing the class here
# import random
# from stateClass import State
# #using main since i definded classes to use

# def getVote (data):
#     #gets a nested list of all the current state data
#     #returnsa list with calculated basePredicitons
#     votes = []; bidenVote = []; trumpVote = []
#     for i in data:
#         if i[4] == 'Joseph R. Biden Jr.':
#             bidenVote.append(i[8])
#         if i[4] == 'Donald Trump':
#             trumpVote.append(i[8])
#     #calculate difference betwen biden and trump data
#     for index in range(len(bidenVote)):
#         b = float(bidenVote[index])
#         t = float (trumpVote[index])
#         votes.append(b -t) #append to votes
#     return votes

# def main(votes, stateList):
#     bidenTotalEv = []
#     trumpTotalEv = []
#     finalPredictionList = []
#     bidenEvList = []
#     trumpEvList = []
#     numIteration  = input("Enter the number of times you like to iterate: ")
#     #check if user entered valid data (int)
#     try:
#         numIteration = int(numIteration)
#     except Exception as e: # e-name associated with exception being passed
#             print (e)
#     else:
#         #if input = int
#         for i in range(numIteration):
#             for i in range( len (votes)):
#                 basePrediciton = votes[i]
#                 randomNoise = random.normalvariate(0.0,1.0)/2.0*3.0
#                 finalPrediction = basePrediciton + randomNoise
#                 finalPredictionList.append(finalPrediction)
                
#             for data in stateList:
#                 for i in finalPredictionList:
#                     if i > 0:
#                         bidenEvList.append(float(data[2]))
#                     else:
#                         trumpEvList.append(float(data[2]))
#         bidenTotalEv.append(sum(bidenEvList))
#         trumpTotalEv.append(sum(trumpEvList))
#         print (bidenTotalEv)
#         print (trumpTotalEv)

#     print('Hope it was helpful, Bye!!')
# if __name__ == "__main__":
#     state= State()
#     state._init_("2020-presidential.csv", '10/6/2020')
#     stateList = state.get_list()
#     votes = getVote(stateList)
#     main (votes, stateList)
