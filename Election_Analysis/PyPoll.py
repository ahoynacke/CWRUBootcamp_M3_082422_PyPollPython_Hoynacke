# The data we need to retrieve.
# The total number of votes cast 
# The percentage of votes each canidate won
# The total number of votes each canidate won
# The wonner of the election based on populat vote 
    # import csv
    # import os

# Assign a variable for the file to load and the path 
    # file_to_load = os.path.join("Resources","election_results.csv")
# open the election results and read the file 
    # with open(file_to_load) as election_data:
# Read the file object with the reader function.
    # file_reader = csv.reader(election_data)
# Print the file object 
    # print(election_data)
 # Print each row in the CSV file.
    # for row in file_reader:
        # print(row)
# Create a filename variable to a direct or indirect path to the file.
    # file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
    # open(file_to_save, "w")

# Create a filename variable to a direct or indirect path to the file.
    # file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
    # with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
        # txt_file.write("Arapahoe\nDenver\nJefferson")
#____________________________________

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)