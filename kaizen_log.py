import pandas as pd

# Define the structure for the Kaizen Log
data = {
    'Problem Identification': [
        'Describe the problem here.',
        'Example: Long waiting times in the queue.'
    ],
    'Proposed Solution': [
        'Describe the proposed solution here.',
        'Example: Implement a ticketing system to manage queues.'
    ],
    'Implementation Date': [
        '',
        ''
    ],
    'Results': [
        'Describe the results here.',
        'Example: Waiting times reduced by 50%.'
    ],
    'Status': [
        'Status of the implementation (e.g., In Progress, Completed, On Hold).',
        'Example: Completed.'
    ]
}

# Create a DataFrame with the structure
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'kaizen_log.xlsx'
df.to_excel(output_file, index=False)

print(f"Kaizen Log template created and saved as {output_file}")
