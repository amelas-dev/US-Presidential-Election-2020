import random


class test:
    def __init__(self):
        pass


    statusArr = []

    for i in range(0, 51):
        rand = random.randint(1,2)
        if (rand == 1):
            statusArr.append("red")
        elif (rand == 2):
            statusArr.append("blue")
