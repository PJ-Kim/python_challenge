import os
import csv
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# path for the source csv file.
csvpath = os.path.join("..", "Resources", "PyPoll_election_data.csv")

# with open(cvspath, newline="", encoding='utf-8') as csvfile:
with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#   def unique_names(row):
    unique_names = []
    win = ()
    Khan_ct = 0
    Correy_ct = 0
    Li_ct = 0
    OTooley_ct = 0
    line_count = 0
# don't read header row        
    next(csvreader)
    for row in csvreader:
            #find unique candidates
            if row[2] not in unique_names:            
                unique_names.append(row[2])
                # count the votes
            if (row[2] == unique_names[0]):
                Khan_ct += 1
            else: 
                if (row[2] == unique_names[1]):
                    Correy_ct += 1
                else: 
                    if (row[2] == unique_names[2]):
                        Li_ct += 1
                    else: 
                        if (row[2] == unique_names[3]):
                                OTooley_ct += 1
            # find the winner
            line_count += 1
            if Khan_ct > Correy_ct:
                win = ("Khan")
            else:
                if Correy_ct > Li_ct:
                    Win = ("Correy")
                else:
                    if Li_ct > OTooley_ct:
                        Win = ("Li")
                    else:
                        win = ("O'Tooley")

#print(line_count/Khan_ct)
#print(line_count)
#print(Khan_ct)
#print(Correy_ct)
#print(Li_ct)
#print(OTooley_ct)
#print(win)


print("Election Results")
print(".................................")
print(f"Total Votes: {(line_count)}")
print(".................................")
print((unique_names[0]),'{0:.000%}'.format(Khan_ct/line_count),'({})'.format(Khan_ct))
print((unique_names[1]),'{0:.000%}'.format(Correy_ct/line_count),'({})'.format(Correy_ct))
print((unique_names[2]),'{0:.000%}'.format(Li_ct/line_count),'({})'.format(Li_ct))
print((unique_names[3]),'{0:.000%}'.format(OTooley_ct/line_count),'({})'.format(OTooley_ct))
print(".................................")
print(f"Winner: {win}")
print(".................................")

# output text file
output_file = os.path.join("PyPoll_Results_data.txt")
#Open the output file
with open(output_file, "w", newline="") as text_file:

    print("Election Results", file=text_file)
    print(".................................", file=text_file)
    print(f"Total Votes: {(line_count)}", file=text_file)
    print(".................................", file=text_file)
    print((unique_names[0]),'{0:.000%}'.format(Khan_ct/line_count),'({})'.format(Khan_ct), file=text_file)
    print((unique_names[1]),'{0:.000%}'.format(Correy_ct/line_count),'({})'.format(Correy_ct), file=text_file)
    print((unique_names[2]),'{0:.000%}'.format(Li_ct/line_count),'({})'.format(Li_ct), file=text_file)
    print((unique_names[3]),'{0:.000%}'.format(OTooley_ct/line_count),'({})'.format(OTooley_ct), file=text_file)
    print(".................................", file=text_file)
    print(f"Winner: {win}", file=text_file)
    print(".................................", file=text_file)    