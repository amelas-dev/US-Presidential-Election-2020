import csv


class State:
    def _init_(self, file, date):
        ''' args file name
            create a list for the most recent data.'''
        local = []
        arr = State.open_file(file)
        for data in arr:
            if (data[0] != date):
                continue
            elif ("US" in data):
                continue
            elif ((data[4] == 'Joseph R. Biden Jr.')
                        or (data[4] =='Donald Trump')):
                local.append(data)
        self.most_recent_data = local
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

# data = State._init_(self, "2020-presidential.csv", '10/6/2020')
# # print(data.get_list())
# for i in data.get_list():
#     if (i[1] == "New York"):
#         print (i)
