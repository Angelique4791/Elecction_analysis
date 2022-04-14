#The data we need to retrieve
#Import CSV module
import csv
dir(csv)
#Assign variable to the file and load path
file_to_load = 'Resources/election_results.csv'
#Open election results and read file
election_data = open(file_to_load)
#To do: perform analysis

#Close the file
election_data.close()
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each canididate won
#5. The winner of the election based on popular vote
