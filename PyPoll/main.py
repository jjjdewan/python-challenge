#################################################################################
# PyPoll Challenge Homework:
#  Submitted by: Jahangir Dewan
#
# Description:
#   In this challenge, we are tasked to help a small, rural town to modernize its vote counting process.
#       Dataset to use : PyPoll/Resources/election_data.csv
#  The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`
#  Our task is to create a Python script that analyzes the votes and display
#  results as per below:
#       1. The total number of votes cast
#       2. A complete list of candidates who received votes
#       3. The percentage of votes each candidate won
#       4. The total number of votes each candidate won
#       5. The winner of the election based on popular vote
#
#   Input: csv file to use (as provided by the instructor):
#           PyPoll/Resources/election_data.csv
#
#   Output file:    analysis/Election_Results.txt
#       The output should look like this:
#
#           The output should look like this:
#
#                   Election Results
#                   -------------------------
#                   Total Votes: 3521001
#                   -------------------------
#                   Khan: 63.000% (2218231)
#                   Correy: 20.000% (704200)
#                   Li: 14.000% (492940)
#                   O'Tooley: 3.000% (105630)
#                   -------------------------
#                   Winner: Khan
#                   -------------------------
#
#     Conclusion and Notes to the marker: I was able to produce exactly the same results as above.
#                 Please feel free to run the scripts and revierw the results
#
#########################################################################################
#
#   Interface with your operating system and CSV file
#   Import os and csv modules
#
import os
import csv

# set the csvpath file to Resource/election_data.csv that contains election data
# for this analysis
#
my_csvpath = os.path.join("Resources", "election_data.csv")

#############################################################
#   Variable declartions and Intitialization
#############################################################
#   Total Vote count
total_votes_count = 0


# Currrent "candidate_name" is set as empty list
candidate_name = ""

# This holds the names of all the candidates
#
list_of_candidates = []

# This is the dictonary holding the key-value pair of each candidate and their votes
#
candidate_votes_dictionary = {}

#############################################################

#############################################################
# Open csv file for reading dataset
# Read csv file to "my_csvreader"
#
with open(my_csvpath, newline = "") as elction_poll_data:
    # Using the the powerful csv dictionary function: csv.DictReader()
    # Ref: https://docs.python.org/2/library/csv.html#csv.DictReader
    #   This is simply an elegant beauty of python object!
    #
    my_csvreader = csv.DictReader(elction_poll_data)


    # Read through each row of csv file data then do further processing
    #
    #   Loop through entire file to update total_votes_count, append names to the list_of_candidates
    #   and condirtional processing as below:
    #
    for row in my_csvreader:

        # Calculate the total votes
        total_votes_count +=  1
        candidate_name = row["Candidate"]
        
        # Conditional processing: If candidate's name is not there then append the list
        # with the current candidate name that is found
        if candidate_name not in list_of_candidates:
            # this is new candidate hence add him in the list of list_of_candidates
            list_of_candidates.append(candidate_name)
            
            # Update candidate's vote count to 1 at the same time when name is found
            candidate_votes_dictionary[candidate_name] = 1
        
        # Othwerise, the candidate is in the list (matched) then update the dictionary with
        #   one more vote for the macthing candidate
        #
        else:
            candidate_votes_dictionary[candidate_name] +=  1
            
#############################################################

    ###################################################################
    #   Calculations and Results:
    #
    #   In this section the following processing will be performed
    #   i)      Calculate the percentage of the total votes for each of the list_of_candidates
    #   ii)     Find out on who is the Winning Candidate
    #   iii)    Print the results as per the given format both on the screen to an output file
    #
    ###################################################################
    
    #
    # Calculate the percentage of the total votes for each of the list_of_candidates
    #
    #
    # print output to the terminal
    print(f"Election Results")
    print("-------------------------------------")
    print(f"Total Votes: {total_votes_count}")
    print("-------------------------------------")
    
    # Iterate through the "candidate_votes_dictionary" that populated earlier then
    # print Name of Candidate,  % of vote and total number of votes for each of the candidates
    # (Using: '%.3f' formatting of the % of Vote to float with 3 decimal points as in the example)
    #
    for candy_name in candidate_votes_dictionary:
        print(candy_name + ": " + str('%.3f'%((candidate_votes_dictionary[candy_name]/total_votes_count)*100)) + "%" + " (" + str(candidate_votes_dictionary[candy_name]) + ")")
    print("-------------------------------------")

    #
    # Using list list(dict.values()) function in python to get values
    # from "candidate_votes_dictionary" in order to find maximum votes
    # for the  winning candidate
    #
    values_candiate_votes = list(candidate_votes_dictionary.values())

    # Print the Winnner name among the candidates using the Keys and Values pair in the
    # "candidate_votes_dictionary" for the Candidate who got maximum votes
    #
    print("Winner: " + str(list(candidate_votes_dictionary.keys())[list(candidate_votes_dictionary.values()).index(max(values_candiate_votes))]))
    
    print("-------------------------------------")

    ##########################################################################################
    #   Writing Results to a file:
    #       * Set Path to output folder
    #       * Open output file to write
    #       * Write results to the file (analysis/Election_Results.txt)
    #
    ##########################################################################################
    output_path = os.path.join("analysis", "Election_Results.txt")
    with open(output_path, 'w', newline='') as text_file:
    
    # Write results to the file (analysis/Election_Results.txt)
    #
        text_file.write("Election Results")
        text_file.write("\n")
        text_file.write("-------------------------------------")
        text_file.write("\n")
        text_file.write("Total Votes: " + str(total_votes_count))
        text_file.write("\n")
        text_file.write("-------------------------------------")
        text_file.write("\n")
        for candy_name in candidate_votes_dictionary:
            text_file.write(candy_name + ": " + str('%.3f'%((candidate_votes_dictionary[candy_name]/total_votes_count)*100)) + "%" + " (" + str(candidate_votes_dictionary[candy_name]) + ")")
            text_file.write("\n")
        text_file.write("-------------------------------------")
        text_file.write("\n")
        text_file.write("Winner: " + str(list(candidate_votes_dictionary.keys())[list(candidate_votes_dictionary.values()).index(max(values_candiate_votes))]))
        text_file.write("\n")
        text_file.write("-------------------------------------")


    
