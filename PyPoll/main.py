#import the os module so the operating system funcionality can be used
import os

#import the csv module so the DictReader class can be used
import csv

#initialize dictionary and total votes variable
votes={}
total=0

#determine the location of the csv file
csvloc=os.path.join(os.getcwd(),"Resources","election_data.csv")

#read the csv file as a list of dictionaries, recognizing file headers
with open(csvloc,"r") as rfile:
    reader=csv.DictReader(rfile)

    #for every dictionary in the list
    for row in reader:

        #pull the name of the candidate that received the vote
        name=row["Candidate"]

        #if the candidate is in the list of keys of the initialized dictionary (votes), then increase the count in the votes dictionary for that candidate
        if name in votes:
            count=votes[name]+1
            votes.update({name:count})

        #if the candidate isn't in the list of keys of the votes dictionary, add the name as a key and the count as 1
        else:
            votes[name]=1
        
        #increase the count for the running total number of votes
        total=total+1

#determine the candidate that has the highest number of votes in the votes dictionary
winner=max(votes, key=lambda key:votes[key])

#determine the location to save the txt file
txtloc=os.path.join(os.getcwd(),"analysis","results.txt")

#print the analysis results to a txt file
with open(txtloc,"w") as wfile:
    wfile.write("Election Results\n")
    wfile.write("-------------------------\n")
    wfile.write(f"Total Votes: {total}\n")
    wfile.write("-------------------------\n")
    for candidate in votes:
        perc=round(100*votes[candidate]/total,3)
        wfile.write(f"{candidate}: {perc}% ({votes[candidate]})\n")  
    wfile.write("-------------------------\n")
    wfile.write(f"Winner: {winner}\n")
    wfile.write("-------------------------\n")

#print the analysis results to the terminal
with open(txtloc,"r") as analysis:
    print(analysis.read())