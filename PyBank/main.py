import os
import csv
#Use datetime class from datetime module given from this website:https://docs.python.org/3/library/datetime.html
from datetime import datetime

#Path to collect data from the Resource folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#Lists to store data
dates = []
profit_losses = []

#Read CSV file
with open(budget_data, 'r') as csvfile:
    
    #Split data on commas and skip header
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    #Loop through each row
    for row in csvreader:
        #Convert date string into datetime object and profit/loss to float
        date = datetime.strptime(row[0], '%b-%y')
        profit_loss = float(row[1])
        dates.append(date)
        profit_losses.append(profit_loss)
        
#Count rows of Date column
total_dates = len(dates)

#Get sum of Profit/Loss column
net_total = sum(profit_losses)

#Calculate changes in P/L over entire period and finding the average
total_change = profit_losses[-1] - profit_losses[0]
average_change = total_change/len(profit_losses)

#Calculate the changes between each month
changes = [profit_losses[i] - profit_losses[i-1] for i in range(1, len(profit_losses))]

#Find greatest increase and date
greatest_increase = max(changes)
increase_date = dates[changes.index(greatest_increase) + 1]


#Find greatest decrease
greatest_decrease = min(changes)
decrease_date = dates[changes.index(greatest_decrease) + 1]

#Create txt file to export results
output_file_path = os.path.join('analysis', 'financial_analysis.txt')

#Put results into txt file
with open(output_file_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total number of months: {total_dates}\n")
    file.write(f"Net total amount of Profit/Loss: ${net_total:.2f}\n")
    file.write(f"Average change: ${sum(changes)/len(changes):.2f}\n")
    file.write(f"Greatest increase in profits: {increase_date.strftime('%b-%y')} (${greatest_increase:.2f})\n")
    file.write(f"Greatest decrease in profits: {decrease_date.strftime('%b-%y')} (${greatest_decrease:.2f})\n")

#Print file into terminal
with open(output_file_path, 'r') as file:
    print(file.read())

