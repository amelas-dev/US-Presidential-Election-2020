import csv
#setting the class name 
class States:
   #setting a constractor to get the file name from the input in the main program
   def __init__(self, filename):
      self.filename = filename
   #function to read and run calculations on the data.
   def reading(self):
      finallist = []
      #opening the file for reading 
      with open("/Users/gabrielwersebe/Desktop/Coding/Group/US-Presidential-Election-2020/main.py") as csv_file:
          reader = csv.reader(csv_file)
          #skipping the headers 
          csv_file.__next__()
          #getting all the data in the file into a list and looping throught it
          datalist = list(reader)
          #loop to get the data in the file and add it to the list
          for row in datalist:
            eachrow = []
            for column in range(0,14):
                if row[0] == '10/06/20' and row[4] == 'Joseph R. Biden Jr.' or row[4] =='Donald Trump' and row[2] != 'US':
                    eachrow.appendrow[column]
            finallist.append(eachrow)

            for i in finallist:
               print(finallist[i])
      return finallist


