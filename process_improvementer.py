import pandas as pd

# Define the structure for the Process Improvement Plan
data = {
    'Section': [
        'Current State',
        'Identified Waste',
        'Future State',
        'Action Items'
    ],
    'Description': [
        'Describe the current state of the process.',
        'Identify any waste or inefficiencies in the current process.',
        'Describe the desired future state of the process.',
        'Detail the action items needed to move from the current state to the future state.'
    ],
    'Details': [
        '', '', '', ''
    ],
    'Owner': [
        '', '', '', ''
    ],
    'Deadline': [
        '', '', '', ''
    ],
    'Status': [
        'Not Started', 'Not Started', 'Not Started', 'Not Started'
    ]
}

# Create a DataFrame with the structure
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'process_improvement_plan.xlsx'
df.to_excel(output_file, index=False)

print(f"Process Improvement Plan template created and saved as {output_file}")
