# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


import os 
import csv
import statistics

csv_file = "C:/Users/VWATSON/Desktop/Classwork/Python_Challenge/PyPoll/election_data.csv"

with open(csv_file, "r") as csvfile:
    election_data = csv.DictReader(csvfile, delimiter = ",")
    header = next(election_data)    
    count = 0
    win_cands = []
    candidate = []
    

    

    for x in election_data:
        
        candidate = x['Candidate']

        count += 1                 

        if candidate not in win_cands:

            win_cands.append(candidate)         
    

    print("Total Votes: " + str(count))
    print(win_cands)
    print()


# A complete list of candidates who received votes
# with open(csv_file, "r") as csvfile:
#     election_data = csv.DictReader(csvfile, delimiter = ",")
    

    # win_cands = set(candidate)  

    # for x in election_data
    #     candidate.append(int(x("candidate")))       


        # set(candidate)
        # print(len("candidate"))
    # print(len(win_cands)

# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# with open(csv_file, "r") as csvfile: