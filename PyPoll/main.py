import os
import csv

#Path to collect election data
election_data = os.path.join('Resources', 'election_data.csv')

#Lists to store data
ballot_ids = []
counties = []
candidates = []
vote_counts = {}
unique_candidates = set()

#Read CSV file
with open(election_data, 'r') as csvfile:
     
     #Split data by ',' and skip header
     csvreader = csv.reader(csvfile, delimiter=',')
     next(csvreader)

     #Loop through each row
     for row in csvreader:
          ballot_id = float(row[0])
          county = row[1]
          candidate = row[2]
          
          #Add data to each respective list
          ballot_ids.append(ballot_id)
          counties.append(county)
          candidates.append(candidate)

          #Get total number of votes
          total_votes = len(ballot_ids)

          # Add candidate to set of unique candidates
          unique_candidates.add(candidate)


          #Count each vote for each candidate and turn into percentage
          if candidate in vote_counts:
            vote_counts[candidate] += 1
          else:
            vote_counts[candidate] = 1
          #Determine winner by using vote_counts.get to compare values
          winner = max(vote_counts, key=vote_counts.get)
        
#Create .txt file for results
output_file_path = os.path.join('analysis', 'election_analysis.txt')

with open(output_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")

    for candidate, votes in vote_counts.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

#Print file into terminal
with open(output_file_path, 'r') as file:
    print(file.read())
