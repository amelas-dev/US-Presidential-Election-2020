import csv
#setting the class name
# class States:
#    #setting a constractor to get the file name from the input in the main program
#    def __init__(self, filename):
#       self.filename = filename
#    #function to read and run calculations on the data.
#    def reading(self):
#       finallist = []
#       #opening the file for reading
#       with open(self.filename,newline='') as csv_file:
#           reader = csv.reader(csv_file)
#           #skipping the headers
#           csv_file.__next__()
#           #getting all the data in the file into a list and looping throught it
#           datalist = list(reader)
#           #loop to get the data in the file and add it to the list
#           for row in datalist:
#             eachrow = []
#             for column in range(0,14):
#                 if row[0] == '10/06/20' and row[4] == 'Joseph R. Biden Jr.' or row[4] =='Donald Trump' and row[2] != 'US':
#                     eachrow.appendrow[column]
#             finallist.append(eachrow)
#       return finallist

class State:
    most_recent_data =[]
    def _init_(self, file, date):
        ''' args list of lists.
            initialize fields with the most recent data.'''
        arr = State.open_file(file)
        for data in arr:
            if (data[0] != date):
                continue
            elif ("US" in data):
                continue
            elif ((data[4] == 'Joseph R. Biden Jr.')
                        or (data[4] =='Donald Trump')):
                self.most_recent_data.append(data)
    @staticmethod
    def open_file (file_name):
        #purpose: open file and return list
        #can't access/modify class state
        ''' args file_name
            return nested list'''
        my_list = []
        try:
            with open(file_name, 'r') as csvfile: #close file after statement execute
                for rows in csv.reader(csvfile): #iterate through data
                    my_list.append(rows)
        except Exception as e: # e-name associated with exception being passed
            print (e)
        return my_list

    def get_list (self):
        return(self.most_recent_data)


# file_data = open_file("2020-presidential.csv")
data = State()
data._init_("2020-presidential.csv", '10/6/2020')

for i in data.get_list():
    print(i)
