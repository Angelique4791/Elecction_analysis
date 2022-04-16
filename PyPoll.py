#The data we need to retrieve
#Dependencies
#Allows us to create file paths across operating systems
import os
#MOdule for reading file
import csv
# Assign a variable for the file to load and the path.
elect_csvpath = os.path.join('Resources', 'election_results.csv')
#print(elect_csvpath)
#Assign variable to save the file to a path
elect_report = os.path.join("analysis","election_analysis.txt")
#print(elect_report)
#Open the path and write to file
open(elect_report,"w")
#TEST PRINT
outfile = open(elect_report,"w")
outfile.write("Hello World!")
outfile.close
#Read file Method1

# Open the election results and read the file.
with open(elect_csvpath) as election_data:
    
    #Read file Method 2
    #Assign variable 


    #Assign variable to the file and load pathheaders = next(file_reader)
    #file_to_load = 'Resources/election_results.csv'
    #Open election results and read file

    #To do: perform analysis
    #Read the file with reader function
    file_reader = csv.reader(election_data)
    #Read and print header row
    headers = next(file_reader)
    print(headers)
    #Print each row of data
    #for row in file_reader:
        #print(row)
    


#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canididate won
#5. The winner of the election based on popular vote
#!TEST!##!REMOVE!#
print("Have a good day!")
