import csv

# Initialize variables
total_votes = 0
candidate_list = []
vote_count = {}

# Open the CSV file
with open('/Users/titi/Desktop/Python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # Save the header row
    header = next(csv_reader)

    # Process the remaining rows
    for row in csv_reader:
        # Increment total vote count
        total_votes += 1

        # Extract candidate name from the row
        candidate_name = row[2]   

        # Check if candidate is already in the list
        if candidate_name not in candidate_list:
            # Add candidate to the list and initialize their vote count to zero
            candidate_list.append(candidate_name)
            vote_count[candidate_name] = 0

        # Increment the vote count for the candidate
        vote_count[candidate_name] += 1

# Create a dictionary to store the percentage of votes
percentage_votes = {}

# Iterate over the candidate dictionary and calculate the percentage of votes
for candidate, votes in vote_count.items():
    percentage = (votes / total_votes) * 100
    percentage_votes[candidate] = percentage

# Determine the winner based on the popular vote
winner = ""
winning_votes = 0

# Iterate over the candidate dictionary and compare the vote count
for candidate, votes in vote_count.items():
    if votes > winning_votes:
        winner = candidate
        winning_votes = votes

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in vote_count.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



        





    
