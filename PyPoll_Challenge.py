#The data we need to retrieve
#Dependencies
#Allows us to create file paths across operating systems
import os
#MOdule for reading file
import csv

location =os.getcwd()
print(location) 
# Assign a variable for the file to load and the path.
elect_csvpath = os.path.join('election_results.csv')

#print(elect_csvpath)
#Assign variable to save the file to a path
elect_report = os.path.join('analysis\election_analysis.txt')
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
#County info
counties_voting = []
county_vote_cast = {}
largest_county_turnout = ""
largest_vote_count = 0

#Read file Method1
# Open the election results and read the file.
with open(elect_csvpath) as election_data:
    
    #To do: perform analysis
    #Read the file with reader function
    file_reader = csv.reader(election_data)
    
    #Read and print header row
    headers = next(file_reader)
 
    
    #print(headers)
    #print(headers)
    
    #Print each row of data
    for row in file_reader:
    
        #2 Add to the total vote count
        total_votes = total_votes+1
    
        #Print candidate name from each row
        candidate_name = row[2]

        #Print the county name from each row
        county_name = row[1]
    
        #Match exisiting candidates to exclude from list
        if candidate_name not in candidate_options:
    
            #1.Add candidate name to candidate list
            candidate_options.append(candidate_name)
    
            #2. Begin tracking candidate votes
            candidate_votes[candidate_name] = 0
    
        #3 Add vote to candidate's vote count
        candidate_votes[candidate_name] += 1

        
        #Match exisiting counties to exclude from list
        if county_name not in counties_voting:
    
            #1.Add county name to county list
            counties_voting.append(county_name)
    
            #2. Begin tracking county votes
            county_vote_cast[county_name] = 0
    
        #3 Add vote to county's vote count
        county_vote_cast[county_name] += 1

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
        print("\n")

        #Save the final vote vount to the text file
        txt_file.write(election_results) 

        #Determine percentage of county votes as percentage of whole
        #1 Iterate through th candidate list
        for county_name in county_vote_cast:
        
            #2. Retrieve the total vote count for a county
            tot_county_vote = county_vote_cast[county_name]
            
        
            #3. Convert the integers to floating point deciaml and calculate the paercenctage of votes
            county_percentage = float(tot_county_vote) / float(total_votes) * 100
            county_results = (f"{county_name}: {county_percentage:.1f}% ({tot_county_vote:,})\n")
            
            #Print each county's voter count and percentage to the terminal
            print(county_results)
            

            #  Save the county results to our text file.
            txt_file.write(county_results)

        print("\n")
        txt_file.write("\n")

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (tot_county_vote > largest_vote_count):
            largest_county_vote = tot_county_vote
            largest_county_turnout = county_name
        #  7: Print the county with the largest turnout to the terminal.
        largest_county_turnout = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"-------------------------\n")
        print(largest_county_turnout)
        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(largest_county_turnout)
        
        #Determine percentage of the vote count
        #1 Iterate through th candidate list
        for candidate_name in candidate_votes:
        
            #2. Retrieve the vote count for a candidate
            votes = candidate_votes.get(candidate_name)
        
            #3. Convert the integers to floating point deciaml and calculate the paercenctage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            #Print each cndidate's voter count and percentage to the terminal
            print(candidate_results)

            

            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)
        print("\n")
        txt_file.write("\n")
  ###############################################0421 Session with Dahoon#############################







        
        
        #Determine winning vote count and candidate
        #Dertermine is the vote count is greater that the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        
            #If true: set winning_count = votes and 
            winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage


        
            #Set winning_candidate equal to candidate's name
            winning_candidate = candidate_name
        
        
        #Print each candidate's name, vount cote, and percentage of votes
        #Print winning candidate summary
        winning_candidate_summary = ("\n"
            f"Winner: {winning_candidate}\n--------------------------"
            f"\nWinning Vote Count: {winning_count:,}\n--------------------------"
            f"\nWinning Percentage: {winning_percentage:.1f}%\n"
            f"--------------------------\n")  
        print(winning_candidate_summary)

        #Save the final vote vount to the text file
        txt_file.write(winning_candidate_summary)
        


        
#Print candidate list
#print(candidate_options)

#Print total_votes
#print(total_votes)

#Print candidate vote dictionary
#print(candidate_votes)




    #!TEST!##!REMOVE!#
    #print("Have a good day!")
