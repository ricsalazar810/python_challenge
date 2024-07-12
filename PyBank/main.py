import os
import csv
#Use datetime class from datetime module given from this website:https://docs.python.org/3/library/datetime.html
from datetime import datetime

#Path to collect data from the Resource folder
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

#Lists to store data
dates = []
profit_losses = []

#Read CSV file
with open(budget_data, 'r') as csvfile:
    
    #Split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #Loop through each row
    for row in csvreader:
        #Convert date string into datetime object and profit/loss to float
        date = datetime.strptime(row[0], '%y-%b')
        profit_loss = float(row[1])
        dates.append(date)
        profit_losses.append(profit_loss)
        
#Count rows of Date column

#Get sum of Profit/Loss column

#Calculate changes in P/L over entire period