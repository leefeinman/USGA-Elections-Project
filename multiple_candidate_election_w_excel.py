#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import pandas as pd
import openpyxl


# In[3]:

    #                                               #
    #                                               #
    #           INFORMATION GATHERING               #
    #                                               #
    #                                               #

voting_members_on_board = int(input("Voting Members on Board:"))
elections_members = int(input("Number of Elections Committee Members Present:"))
voting_members_present = int(input("Number of Voting Members Present:"))
voting_members = voting_members_on_board - elections_members
quorum = (2/3) * voting_members

if voting_members_present >= quorum:
    print("Quorum is met")
    candidates = int(input("How many people are running?:"))
    open_positions = int(input("How many open positions are there?:"))
else: 
    print("Quorum not met: " + str(math.ceil(quorum - voting_members_present)) + " more member(s) needed")


# In[4]:

    #                                               #
    #                                               #
    #           UNIVERSAL FUNCTIONS                 #
    #                                               #
    #                                               #


class Candidate:
    def __init__(self, ID = None, name = None, Yays = None, Nays = None, Abstensions = None):
        
        self.ID = str(ID)
        
        if not name:
            self.name = str(input('Enter name: '))
        else:
            self.name = name
        
        if not Yays:
            self.Y = input('Enter yays: ')
        else:
            self.Y = Yays
      
        if not Nays:
            self.N = input('Enter nays: ')
        else:
            self.N = Nays
       
        if not Abstensions:
            self.A = input('Enter abstensions: ')
        else:
            self.A = Abstensions

def initial_result(self):
    
        if int(self.A) == voting_members:
            return 'the number of abstenstions cannot equal the number of votes. vote is null.'
        
        elif (int(self.Y) + int(self.N)+ int(self.A)) != voting_members_present:
            return 'votes for ' + self.name + ' are not equal to # of voters'

        elif int(self.Y) / (int(self.Y) + int(self.N)) >= (2/3):
            return self.name + ' met 2/3 threshold'
    
        else:
            return self.name + ' did not meet 2/3 threshold'


    #                                               #
    #                                               #
    #           M.C.E. FUNCTIONS                    #
    #                                               #
    #                                               #


def zip_result(self):
     ### !!! this is the function for the loop that sorts&zips our lists !!! ###
    if int(self.Y) / (int(self.Y) + int(self.N)) < (2/3):
        return 0
    else:
        return  int(self.Y) / (int(self.Y) + int(self.N))


def final_result(self):
    
    if candidate_ID[i].name in winners:
        return "elected"
    else:
        return "not elected"
    


# In[10]:




i = 1
data = []
index = []
tally = []
name = []
winners = []
placeholder = 1
origin_of_replication = candidates - open_positions
candidate_ID = [0] * candidates
candidate_ID_symbol = [0] * candidates

#try:   #remove the try... except to examine errors!
for i in range(0, candidates):

    candidate_ID[i] = Candidate('C' + str(i+1))
    print(initial_result(candidate_ID[i]))
    if initial_result(candidate_ID[i]) == 'the number of abstenstions cannot equal the number of votes. vote is null.' or initial_result(candidate_ID[i]) == 'votes for ' + candidate_ID[i].name + ' are not equal to # of voters':  
        print("please retry. if this problem persists, revote")
        break
    else:
        pass


    # "placeholder" is the position of the "results" column. It will later be modified. 
    data.append([candidate_ID[i].name, candidate_ID[i].Y, candidate_ID[i].N, candidate_ID[i].A, placeholder])

    candidate_ID_symbol[i] = 'C' + str(i+1)
    index.append(candidate_ID_symbol[i])    

    tally.append(zip_result(candidate_ID[i]))
    name.append(candidate_ID[i].name) 

    if i == candidates - 1:
        break
    elif input("Continue to next candidate? (enter 'yes' or 'no')?: ").lower() == "no":
        print("you've chosen to stop entering candidates. an error message will appear which you can disregard.")
        break
    else:
        pass    

    i += 1




tally, name = zip(*sorted(zip(tally, name), reverse=True))

if origin_of_replication > 0:

    for i in range(0, open_positions):

        if tally[i] > 0:
            winners.append(name[i])
        else:
            pass

        i += 1        
else:
    winners = name


for i in range(0, candidates):

    terniary = final_result(candidate_ID[i])
    data[i][4] = terniary
    i+=1


results_dataframe = pd.DataFrame(data, index, columns = ['Name', 'Yays', 'Nays', 'Abstensions', 'Result'])


print(results_dataframe)

results_dataframe.to_excel("/Users/leefeinman/Documents/PYTHON_SNAKE_PSSS/USGA/Python_for_USGA/USGA_Elections_Project/USGA_voting_workbook.xlsx", startrow = 9, startcol = 20,)

## next step is to:
    # 1: close the excel file if it's open and then open it after the data is added (do this with the apple script????
    #           probably a better idea... note — data cannot be added to the file if excel is open)
    # 2: find a way to
    #           - insert new rows for the respective columns so that the data can be added on top of pre-existing data
    #           - remove the column names when the dataframe gets pasted to excel (I'll have my own formatting in excel)
    # 3: running the application through excel?
    #           - the problem is that if I include macros in the excel file, python has a problem writing to it
    #           so I don't know another way around this nonsense. May just need to open the application every time.
    # 4: create a tkinter (or similar) window for inputting and printing information from the program...
    #       I don't want to control this through terminal LOL.
    
    
    
#except:
    #print("\nan error has occured. please retry, revote, or consult the constitution on how to proceed.")

    


# In[ ]:




