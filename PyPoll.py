# Week 3 Challenge
# import libraries
import os
import csv
import random
import numpy

# 1. Open the data file.
file_to_load = os.path.join("Resources","election_results.csv")

# Use method that uses CSV module for improved reading
with open(file_to_load) as election_data:

    print(election_data)
    
    # CSV reader specifies delimiter and variable that holds contents
    file_reader = csv.reader(election_data, delimiter=',')

    # print each list
    # for row in file_reader:
    #     print(row)
    
    # Read the header row first, store it and print it
    headers = next(file_reader)
    print(f"{headers}")







# # Create filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file
#     txt_file.write("Counties in the Election\n----------\n")
#     txt_file.write("Arapahoe\n")
#     txt_file.write("Denver\n")
#     txt_file.write("Jefferson")






# 2. Write down the names of all the candidates.

# 3. Add a vote count for each candidate.
# 4. Get the total votes for each candidate.
# 5. Get the total votes cast for the election.

#Data needed to retrievie
# total number of votes cast, number of entries?
# list of candidates that received votes
# percentage of votes each candidtate won
# total number of votes each candidate won
# winner of the election based on popular vote
#3.4.1

