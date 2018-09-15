



# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

import os 
import csv
import statistics

csv_file = "C:/Users/VWATSON/Desktop/Classwork/Python_Challenge/PyBank/budget_data.csv"

with open(csv_file, "r") as csvfile:
    pl_data = csv.DictReader(csvfile, delimiter = ",")

    count = 0
    
    for x in pl_data:
        count += 1

    print("Total Months: " + str(count))

with open(csv_file, "r") as csvfile:
    pl_data = csv.DictReader(csvfile, delimiter = ",")

    total_amount = 0

    for x in pl_data:
        total_amount += int(x['Profit/Losses'])

    print ("Total: $" + str(total_amount))

with open(csv_file, "r") as csvfile:
    pl_data = csv.DictReader(csvfile, delimiter = ",")

    mthly_data = []
    diff = []

    for x in pl_data:
        mthly_data.append(int(x['Profit/Losses']))

    diff = [mthly_data[i] - mthly_data[i+1] for i in range(len(mthly_data)-1)]

    maxmonth = max(diff)
    minmonth = min(diff)

    mthly_avrg = statistics.mean(diff)

    print("Total Average: $" + str(mthly_avrg))
    print("Greatest Increase: $" + str(maxmonth))
    print("Greatest Decrease: $" + str(minmonth))











