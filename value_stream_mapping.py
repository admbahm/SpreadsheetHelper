import os
import pandas as pd

# Define the file path including the filename
file_path = os.path.join('/home/adam/Documents/repositories/SpreadsheetHelper/exports', 'Value_Stream_Mapping.xlsx')

# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Create the DataFrame and save it as an Excel file
df = pd.DataFrame({
    "Process Step": ["Step 1", "Step 2", "Step 3", "Step 4", "Step 5"],
    "Cycle Time (mins)": [10, 15, 20, 25, 30],
    "Queue Time (mins)": [5, 3, 2, 4, 1],
    "Information Flow": ["Manual", "Automated", "Manual", "Automated", "Manual"],
    "Value-Add (Y/N)": ["Y", "N", "Y", "N", "Y"]
})

df.to_excel(file_path, index=False)
