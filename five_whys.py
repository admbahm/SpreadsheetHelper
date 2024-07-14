import pandas as pd

# Define the structure for the 5 Whys Analysis
data = {
    'Section': [
        'Problem Statement', 'Why 1', 'Why 2', 'Why 3', 'Why 4', 'Why 5', 'Root Cause', 'Action Plan'
    ],
    'Description': [
        'Describe the problem here.',
        'Answer to Why 1',
        'Answer to Why 2',
        'Answer to Why 3',
        'Answer to Why 4',
        'Answer to Why 5',
        'Identify the root cause here.',
        'Outline the action plan to address the root cause.'
    ],
    'Details': [
        '', '', '', '', '', '', '', ''
    ]
}

# Create a DataFrame with the structure
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = '5_whys_analysis.xlsx'
df.to_excel(output_file, index=False)

print(f"5 Whys Analysis template created and saved as {output_file}")
