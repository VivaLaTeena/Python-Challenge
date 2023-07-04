import csv
import datetime

filename = "/Users/titi/Desktop/Python-challenge/PyBank/Resources/budget_data.csv"

with open(filename, "r") as file:
    csvreader = csv.reader(file)
    next(csvreader)  # Skip the header row

    # Initialize variables
    months = 0
    net_total = 0
    previous_profit = 0
    changes = []
    dates = []

    # Loop through each row in the CSV file
    for row in csvreader:

        # Parse the date and profit/loss values
        date_str = row[0]
        month = date_str.split("-")[1]  # Extract the month
        year = date_str.split("-")[0]   # Extract the year

        # Combine the extracted month and year into a date string
        date = f"{month}-{year}"

        profit = int(row[1])

        # Calculate the total number of months
        months += 1

        # Calculate the net total amount of profit/loss
        net_total += profit

        # Calculate the change in profit/loss from the previous month
        if months > 1:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)

        # Update the previous profit/loss value for the next iteration
        previous_profit = profit

# Calculate the average change in profit/loss
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_index = changes.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

greatest_decrease = min(changes)
greatest_decrease_index = changes.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

# Convert the greatest increase and decrease dates to "10-Jan" format
greatest_increase_month = greatest_increase_date.split("-")[0]
greatest_increase_year = '20' + greatest_increase_date.split("-")[1]  # Add '20' prefix
greatest_increase_date_formatted = f"{greatest_increase_month}-{greatest_increase_year[-2:]}"

greatest_decrease_month = greatest_decrease_date.split("-")[0]
greatest_decrease_year = '20' + greatest_decrease_date.split("-")[1]  # Add '20' prefix
greatest_decrease_date_formatted = f"{greatest_decrease_month}-{greatest_decrease_year[-2:]}"


# Print the results
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date_formatted} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date_formatted} (${greatest_decrease})")

# Specify the file path for saving the analysis results
output_file = "/Users/titi/Desktop/Python-Challenge/PyBank/analysis.txt"

# Open the file in write mode
with open(output_file, "w") as file:

    # Write the results to the file
    file.write("Financial Analysis\n")
    file.write("----------------------------------\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date_formatted} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date_formatted} (${greatest_decrease})\n")

# Print a message indicating the file was saved successfully
print("Results saved to analysis.txt file.")
