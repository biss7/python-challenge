#assume the data is in order
#data isn't in date order when you look at it in Excel
#changing data to date order would change almost all analysis results

#import the os module so the operating system funcionality can be used
import os

#import the csv module so the DictReader class can be used
import csv

#initialize variables, dictionaries, and list
lncount=0
lntotal=0
tempdict_1={}
tempdict0={}
changes=[]

#determine the location of the csv file
csvloc=os.path.join(os.getcwd(),"Resources","budget_data.csv")

#read the csv file as a list of dictionaries, recognizing file headers
with open(csvloc,"r") as rfile:
    reader=csv.DictReader(rfile)

    #for every dictionary in the list
    for row in reader:

        #save the current row's information in a temporary dictionary
        tempdict0={"DATE":row["Date"],"PL":row["Profit/Losses"]}

        #increase the count for the number of dictionaries in the list
        lncount=lncount+1

        #add the current dictionary's profit/losses to the running total of profit/losses
        lntotal=lntotal+int(tempdict0["PL"])

        #if the previous temporary dictionary is not empty, calculate the differences in profit/losses and append the information to the changes list
        #if the previous temporary dictionary is empty (looking at first row of data in Excel), do nothing
        if tempdict_1:
            change=int(tempdict0["PL"])-int(tempdict_1["PL"])
            changes.append({"DATE":row["Date"],"CHANGE":change})
        
        #override the previous temporary dictionary with the current row's information
        tempdict_1=tempdict0

#calculate the average of the changes in the changes list
chcount=len(changes)
chsum=sum(day["CHANGE"] for day in changes)
chave=round(chsum/chcount,2)

#find the max and min changes in the changes list
chmax=max(changes, key=lambda x:x["CHANGE"])
chmin=min(changes, key=lambda x:x["CHANGE"])

#determine the location to save the txt file
txtloc=os.path.join(os.getcwd(),"analysis","results.txt")

#print the analysis results to a txt file
with open(txtloc,"w") as wfile:
    wfile.write("Financial Analysis\n")
    wfile.write("----------------------------\n")
    wfile.write(f"Total Months: {lncount}\n")
    wfile.write(f"Total: ${lntotal}\n")
    wfile.write(f"Average Change: ${chave}\n")
    wfile.write(f"Greatest Increase in Profits: {chmax['DATE']} (${chmax['CHANGE']})\n")
    wfile.write(f"Greatest Decrease in Profits: {chmin['DATE']} (${chmin['CHANGE']})\n")

#print the analysis results to the terminal
with open(txtloc,"r") as analysis:
    print(analysis.read())