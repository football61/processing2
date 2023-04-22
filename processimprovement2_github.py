import os
import pandas as pd
import datetime

today = datetime.date.today()

# Format the date as an underscore-separated string
date_string = today.strftime("%Y %m %d")

print(date_string[0:4])

#2023_04_22


# Define the folder path where the text files are located
folder_path = "C:\\Users\\Paul\\Documents\\filing"

# Define the matching substrings for the first set of text files
matching_substrings_excel = ["string1", "string2", "string3"]

# Define the matching substrings for the second set of text files
matching_substrings_csv = ["string1", "string2"]

# Create the "archive" folder if it doesn't exist
archive_folder_path = os.path.join(folder_path, "archive")
if not os.path.exists(archive_folder_path):
    os.makedirs(archive_folder_path)

# Read the first set of text files into Excel files
for file in os.listdir(folder_path):
    if file.endswith(".txt") and any(substring in file for substring in matching_substrings_excel):
        # Read the text file into a pandas dataframe
        df = pd.read_csv(os.path.join(folder_path, file), delimiter="\t")
        # Write the dataframe to an Excel file in the archive folder
        excel_file_name = os.path.splitext(file)[0] + ".xlsx"
        with pd.ExcelWriter(os.path.join(archive_folder_path, excel_file_name)) as writer:
            df.to_excel(writer, sheet_name="Sheet1", index=False)

# Read the second set of text files into CSV files
for file in os.listdir(folder_path):
    if file.endswith(".txt") and any(substring in file for substring in matching_substrings_csv):
        # Read the text file into a pandas dataframe
        df = pd.read_csv(os.path.join(folder_path, file), delimiter="\t")
        # Write the dataframe to a CSV file in the archive folder
        csv_file_name = os.path.splitext(file)[0] + ".csv"
        df.to_csv(os.path.join(archive_folder_path, csv_file_name), index=False)
