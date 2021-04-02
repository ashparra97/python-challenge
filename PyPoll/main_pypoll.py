# import modules 
import os 
import csv 

# determine file path 
pypoll_path = os.path.join("PyPoll", "Resources", "PyPoll.csv")

#read the csv file
with open(pypoll_path) as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter=",")
    #print(pypoll_reader)
    pypoll_header = next(csvfile, None)

# create empty lists 
    candidates = []
    vote_list = [0, 0, 0, 0]
# for loop to tell code to go through every row
    for row in pypoll_reader:
        # get the unique names of the candidates for a complete list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
        # count the votes for Khan
        if row[2] == "Khan":
            vote_list[0] += 1
        # count the votes for Correy
        elif row[2] == "Correy":
            vote_list[1] += 1
        # count the votes for Li
        elif row[2] == "Li":
            vote_list[2] += 1
        # count the votes for O'Tooley
        elif row[2] == "O'Tooley":
            vote_list[3] += 1
    # print out candidate list 
    #print(candidates)
    # print out total number of votes for each candidate
    #print(vote_list)
# total number of votes cast in the election 
    #print(sum(vote_list))

# percentage of votes each candidate won 
    for row in vote_list:
        percent_khan = vote_list[0] / sum(vote_list)
        percent_correy = vote_list[1] / sum(vote_list)
        percent_li = vote_list[2] / sum(vote_list)
        percent_otooley = vote_list[3] / sum(vote_list)
    #print(round(percent_khan * 100))
    #print(round(percent_correy * 100))
    #print(round(percent_li * 100))
    #print(round(percent_otooley * 100))

# winner of the election based on popular vote 
winner = candidates[vote_list.index(max(vote_list))]
#print(winner)

# print table 
print("Election Results")
print("------------------------------")
print(f"Total Votes: {sum(vote_list)}")
print("------------------------------")
print(f"{candidates[0]} {(round(percent_khan * 100))}.000% ({vote_list[0]})")
print(f"{candidates[1]} {(round(percent_correy * 100))}.000% ({vote_list[1]})")
print(f"{candidates[2]} {(round(percent_li * 100))}.000% ({vote_list[2]})")
print(f"{candidates[3]} {(round(percent_otooley * 100))}.000% ({vote_list[3]})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

# text file analysis
pypoll_file = open("/Users/ashleypatricia/Documents/GitHub/python-challenge/PyPoll/Analysis /Election Analysis.txt", "w")
pypoll_file.write("Election Results\n")
pypoll_file.write("------------------------------\n")
pypoll_file.write(f"Total Votes: {sum(vote_list)}\n")
pypoll_file.write("------------------------------")
pypoll_file.write(f"{candidates[0]} {(round(percent_khan * 100))}.000% ({vote_list[0]})\n")
pypoll_file.write(f"{candidates[1]} {(round(percent_correy * 100))}.000% ({vote_list[1]})\n")
pypoll_file.write(f"{candidates[2]} {(round(percent_li * 100))}.000% ({vote_list[2]})\n")
pypoll_file.write(f"{candidates[3]} {(round(percent_otooley * 100))}.000% ({vote_list[3]})\n")
pypoll_file.write("------------------------------\n")
pypoll_file.write(f"Winner: {winner}")
pypoll_file.write("------------------------------\n")
pypoll_file.close()