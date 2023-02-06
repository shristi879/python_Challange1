# Modules
import os
import csv

# set our Resource path and output file for printing result
find_path = "Resources/Assignment_python_PyBank_Resources_budget_data.csv"
output_file = "Financial Analysis.csv"

# Open the CSV
with open(find_path) as csv_file:
   
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    
    total_months = 0
    total = 0
    second_row = 0
    first_row = 0
    month_change = 0
    total_month_change = []
    date = []

      # Loop through looking for months
    for row in csv_reader:
        
        # The total number of months included in the dataset
        total_months += 1
        
        # The net total amount of "Profit/Losses" over the entire period
        first_row = int(row[1])
        total += int(row[1])
        
        # The average of the changes in "Profit/Losses" over the entire period
        if (total_months==1):
            second_row = first_row
            

    else: 
            month_change = first_row - second_row
            date.append(row[0])
            total_month_change.append(month_change)
            second_row = first_row
    average = round(sum(total_month_change)/(total_months - 1), 2)
    
    # The greatest increase and decrease in profits (date and amount) over the entire period
    greatest_increase = max(total_month_change)
    greatest_decrease = min(total_month_change)
        
    increase_date = date[total_month_change.index(greatest_increase)]
    decrease_date = date[total_month_change.index(greatest_decrease)]
    
    # print the result on terminal
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {increase_date}(${greatest_increase})")
    print(f"Greatest Decrease in Profits: {decrease_date}(${greatest_decrease})")

# open the output file and write the result to the csv
with open(output_file, "w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"----------------------------\n")
    text.write(f"Total Months: {total_months}\n")
    text.write(f"Total: ${total}\n")
    text.write(f"Average Change: ${average}\n")
    text.write(f"Greatest Increase in Profits: {increase_date}(${greatest_increase})\n")
    text.write(f"Greatest Decrease in Profits: {decrease_date}(${greatest_decrease})")