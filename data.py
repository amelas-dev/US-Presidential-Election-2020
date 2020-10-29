# All the state and canidate classes go here
from csv import reader

with open('presidential_data.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    canidateData = list(csv_reader)
canidateDataKeys = canidateData[0]
canidateDataNumbers = canidateData[1:]
