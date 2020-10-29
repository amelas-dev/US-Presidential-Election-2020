import csv
#setting the class name 
class States:
   #setting a constractor to get the file name from the input in the main program
   def __init__(self, filename):
      self.filename = filename
   #function to read and run calculations on the data.
   def reading(self):
      #[n][0] is n'th state name, [n][1] is state abbreviation, [n][2] is overall avg, [n][3] is average rise, [n][4] is prediction from last year, [n][5] is prediction based on avg
      finallist = []
      #using a list of state abbreviations to have the user use NY or New York.
      #opening the file for reading 
      with open(self.filename,newline='') as csv_file:
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
      return finallist
