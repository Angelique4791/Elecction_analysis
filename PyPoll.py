#The data we need to retrieve
#Dependencies
#Allows us to create file paths across operating systems
from fileinput import close
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
#open(elect_report,"w")
#TEST PRINT
#outfile = open(elect_report,"w")
#outfile.write("Counties in the Election\n--------------------------\n")
#outfile.write("Arapahoe\nDenver\nJefferson\n--------------------------")
#outfile.close

#1. Init a total vote counter
total_votes = 0
#2 candidate options and candidte votes
candidate_options = []
candidate_votes = {}
#Winning candidate and winning vote tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Counties list

#Read file Method1
# Open the election results and read the file.
with open(elect_csvpath) as election_data:
    
    #To do: perform analysis
    #Read the file with reader function
    file_reader = csv.reader(election_data)
    
    #Read and print header row
    headers = next(file_reader)
    
    #print(headers)
    
    #Print each row of data
    for row in file_reader:
    
        #2 Add to the total vote count
        total_votes += 1
    
        #Print candidate name from each row
        candidate_name = row[2]
    
        #Match exisiting candidates to exclude from list
        if candidate_name not in candidate_options:
    
            #1.Add candidate name to candidate list
            candidate_options.append(candidate_name)
    
            #2. Begin tracking candidate votes
            candidate_votes[candidate_name] = 0
    
        #3 Add vote to candidate's vote count
        candidate_votes[candidate_name] += 1
#Save the results to our text file
with open(elect_report, "w") as txt_file:

    #Print the final vote to the terminal
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    
    #Save the final vote vount to the text file
    txt_file.write(election_results)    
    #Determine percentage of the vote count
    #1 Iterate through th candidate list
    for candidate_name in candidate_votes:
    
        #2. Retrieve the vote count for a candidate
        votes = candidate_votes[candidate_name]
    
        #3. Convert the integers to floating point deciaml and calculate the paercenctage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        #Print each cndidate's voter count and percentage to the terminal
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
        #Determine winning vote count and candidate
        #Dertermine is the vote count is greater that the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            #If true: set winning_count = votes and 
            #winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
        
            #Set winning_candidate equal to candidate's name
            winning_candidate = candidate_name
    #Print each candidate's name, vount cote, and percentage of votes
    #Print winning candidate summary
    winning_candidate_summary = (
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")  
    print(winning_candidate_summary)

    #Save the final vote vount to the text file
    txt_file.write(candidate_results)

close

        
#Print candidate list
#print(candidate_options)

#Print total_votes
#print(total_votes)

#Print candidate vote dictionary
#print(candidate_votes)




#!TEST!##!REMOVE!#
#print("Have a good day!")
