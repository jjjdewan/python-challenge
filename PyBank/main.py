##################################################################################
#
#   Challenge-1: PyBank
#       By: Jahangir Dewan
#
# The objecrtive of the challenge is to create a Python script for analyzing
#   the financial records for a given dataset of a company to produce following
#   output and write the results to an  output file:
#   1. The total number of months included in the dataset
#   2. The net total amount of "Profit/Losses" over the entire period
#   3. The average of the changes in "Profit/Losses" over the entire period
#   4. The greatest increase in profits (date and amount) over the entire period
#   5. The greatest decrease in losses (date and amount) over the entire period
#
#    Input: csv file to use (as provided by the instructor):
#        Resources/budget_data.csv
#
#    Output file: analysis/financial_analysis.txt
#           The output should look like this:
#           ```text
#           Financial Analysis
#           ----------------------------
#           Total Months: 86
#           Total: $38382578
#           Average  Change: $-2315.12
#           Greatest Increase in Profits: Feb-2012 ($1926159)
#           Greatest Decrease in Profits: Sep-2013 ($-2196167)
#
#     Conclusion and Notes to the marker: I was able to produce exactly the same results as above.
#                 Please feel free to run the scripts and revierw the results
#
##################################################################################
#
# Interface with your operating system and CSV file
# Import os and csv modules
#
import os
import csv

# set the csv file path to Resource/budget_data.csv that contains financial data
# for this analysis
#
my_csvfile = os.path.join("Resources", "budget_data.csv")

# Initialize values: month_counter, total_prifit_loss, profit_loss_value and
# change_in_profit_loss
#
month_counter = 0
total_profit_loss = 0
profit_loss_value = 0
change_in_profit_loss = 0



# Create list to store dates_list and Profit/Losses values
#
dates_list = []
profit_loss_list = []

# Open csv file for reading dataset
#
with open(my_csvfile, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #
    # Now, Using next to the firts row (header) of csv file, discard it and then get ready
    # to iterate through the data from next row
    #
    csvheader = next(csvreader)

    #  Initialize variables with row_one values to begin with
    #  before we loop through the whole dataset
    #
    row_one = next(csvreader)
    month_counter += 1
    total_profit_loss += int(row_one[1])
    profit_loss_value = int(row_one[1])
    
 
# Read through each row of csv file data then do further processing
#   The follwing processing will be done in this section of the for loop:
#   i)      Appened dates_list
#   ii)     Find Chanage in profit-loss
#   iii)    Append profit_loss_list
#   iv)     Update month_counter for total months calculation
#   v)      Update total Profit-loss
#
    for row in csvreader:
        
        ################################
        # Update lists:date_list[], profit_list[] and monthly_changes[]
        #  and
        #
        # Append/update date info to the date_list[] for highest increase or decrease in profit
        #
        dates_list.append(row[0])
    
        #
        # Calculate change_in_profit_loss in profit/loss and update "profit_losses_changes_list"
        #
        change_in_profit_loss = int(row[1])-profit_loss_value
        profit_loss_list.append(change_in_profit_loss)
        profit_loss_value = int(row[1])

        # Increase total mounth counter
        #
        month_counter += 1
        
        #
        # Update total Profit-loss amount now
        
        total_profit_loss = total_profit_loss + int(row[1])
        

    ###################################################################
    #   Final Calculations:
    #   In this section the following processing will be performed
    #   i)      Average changes in profit/losses
    #   ii)     Greatest increase in profits with date and amount
    #   iii)    Greatest decrease in losses with date and amount
    #
    ###################################################################
    
    #
    #  Calculate the average change_in_profit_loss using profit_loss_list
    #
    average_changes_in_profit_loss = sum(profit_loss_list)/len(profit_loss_list)
    
    # Find Greatest increase in profits with date and amount using profit_loss_list
    #
    greatest_increase_profit = max(profit_loss_list)
    greatest_increase_index = profit_loss_list.index(greatest_increase_profit)
    greatest_increase_date = dates_list[greatest_increase_index]

    #   Find Greatest decrease in losses with date and amount using profit_loss_list
    #
    greatest_decrease_in_losses = min(profit_loss_list)
    greatest_loss_index = profit_loss_list.index(greatest_decrease_in_losses)
    greatest_loss_date = dates_list[greatest_loss_index]

    
################################################################
#   Printing Analysis Report on the screen
#
#################################################################
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f"Total Months: {str(month_counter)}")
print(f"Total: ${str(total_profit_loss)}")
print(f"Average change_in_profit_loss: ${str(round(average_changes_in_profit_loss,2))}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase_profit)})")
print(f"Greatest Decrease in Profits: {greatest_loss_date} (${str(greatest_decrease_in_losses)})")

##########################################################################################
#   Writing Results to a file:
#       * Set Path to output folder
#       * Open output file to write
#       * Write results to the file (analysis/Election_Results.txt)
#
##########################################################################################
#
output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, 'w', newline='') as text_file:
    # Write results to the file (analysis/Election_Results.txt)
    #
    text_file.write("----------------------------------------------------------\n")
    text_file.write("  Financial Analysis"+ "\n")
    text_file.write("----------------------------------------------------------\n\n")
    text_file.write("    Total Months: " + str(month_counter) + "\n")
    text_file.write("    Total Profits: " + "$" + str(total_profit_loss) +"\n")
    text_file.write("    Average Change: " + '$' + str(round(average_changes_in_profit_loss,2)) + "\n")
    text_file.write("    Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_profit) + ")\n")
    text_file.write("    Greatest Decrease in Profits: " + str(greatest_loss_date) + " ($" + str(greatest_decrease_in_losses) + ")\n")
    text_file.write("----------------------------------------------------------\n")




