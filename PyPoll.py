# Week 3 Challenge
# import libraries
import os
import csv
# import random
# import numpy

# initialize
total_votes = 0
# new list
candidate_options = []
# new dict
candidate_votes = {} 
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 1. Open the data file.
file_to_load = os.path.join("Resources","election_results.csv")
# Create filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use method that uses CSV module for improved reading
with open(file_to_load) as election_data:

    # print(election_data)
    
    # CSV reader specifies delimiter and variable that holds contents
    file_reader = csv.reader(election_data, delimiter=',')

    # print each list
    # for row in file_reader:
    #     print(row)
    
    # Read the header row first, store it and print it
    headers = next(file_reader)
    # print(f"{headers}")

    # total number of votes cast, number of entries?
    for row in file_reader:
        #count total votes by couting each list
        total_votes = total_votes + 1

        # get candidate from each list, add to output list
        candidate_name = row[2]
        #check if name is not in the output list
        if candidate_name not in candidate_options:
            #if not in list, add to list
            candidate_options.append(candidate_name)
            #if not in list, add candidate name as a dict key and add count
            candidate_votes[candidate_name] = 0
        
        #add vote for candidate dict in row
        candidate_votes[candidate_name] += 1
    
    # Using the with statement open the file as a text file.
    with open(file_to_save, "w") as txt_file:
        # Write header for file
        txt_file.write("Election Results\n----------\n")
        #write total votes
        txt_file.write(f"Total Votes: {total_votes:,}\n----------\n")
        
        # iterate the candidate list
        for candidate_name in candidate_votes:
            #get total votes for a candidate
            votes = candidate_votes[candidate_name]
            #calc the % of total
            vote_percentage = float(votes) / float(total_votes)*100
            #output the name and % of total vote
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # write each candidate results
            txt_file.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


            # Determine if the votes is greater than the winning count.
            # continuous tracking/changing of winner instead of outside for loop
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =
                # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        #summarize winner
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        
        #print win summary to terminal
        print(winning_candidate_summary)
             
        #write the winning summary to file
        txt_file.write(f"{winning_candidate_summary}")

#print(candidate_votes)
#print(total_votes)