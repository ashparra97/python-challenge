# import modules 

import os 
import csv 

#determine file path 
pybank_path = os.path.join("PyBank", "Resources", "PyBank.csv")

#read the csv file
with open(pybank_path) as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter=",")
    #print(pybank_reader)

#print out the header names 
    pybank_header = next(csvfile, None)
    #print("Header: " + pybank_header)


# total number of months included in dataset 
    month_list = []
    total_list = []
    for row in pybank_reader:  
        month_list.append(row[0])
        total_list.append(int(row[1]))
         
    #print(month_list)
    #print(len(month_list)) 
    #make sure # of months = number of profits/losses 
    #print(len(total_list))   
    # Net total amount of profits/losses over entire period 
    #print(sum(total_list))
    

# Calculate the changes in "Profit/Losses" over the entire period
# determine empty variable
    totalchanges = []
# for loop tells code to go through all rows
    for i in range(0, len(total_list) - 1):
        #monthly changes (difference between row before i and i)
        monthlychanges = (total_list[i+1] - total_list[i])
        #add each monthly change to one another
        totalchanges.append(monthlychanges)
    #make sure length is correct of total changes
    #print(len(totalchanges))

    # Find the average of those changes over the entire period
    avg_changes = (round(sum(totalchanges) / len(totalchanges),2))
    #print(avg_changes)


    # The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(totalchanges)
    #print(greatest_increase)
    # Find index of max to find date (+1 to account for correct index)
    max_date = month_list[totalchanges.index(max(totalchanges)) + 1]

    # The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(totalchanges)
    #print(greatest_decrease)
    # find index for min date (+1 to account for correct index)
    min_date = month_list[totalchanges.index(min(totalchanges)) + 1]

# Print table 
    print("Financial Analysis")
    print ("-----------------------------------------")
    print(f"Total Months: {len(month_list)}")
    print(f"Total: ${sum(total_list)}")
    print(f"Average Change: ${avg_changes}")
    print(f"Greatest Increase in Profits: {max_date} (${greatest_increase})")
    print(f"Greatest Increase in Profits: {min_date} (${greatest_decrease})")

# save as text file 
pybank_file = open("/Users/ashleypatricia/Documents/GitHub/python-challenge/PyBank/Analysis/Financial Analysis.txt", "w")
pybank_file.write("Financial Analysis\n")
pybank_file.write("-----------------------------------------\n")
pybank_file.write(f"Total Months: {len(month_list)}\n")
pybank_file.write(f"Total: ${sum(total_list)}\n")
pybank_file.write(f"Average Change: ${avg_changes}\n")
pybank_file.write(f"Greatest Increase in Profits: {max_date} (${greatest_increase})\n")
pybank_file.write(f"Greatest Increase in Profits: {min_date} (${greatest_decrease})\n")
pybank_file.close()