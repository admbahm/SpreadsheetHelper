import pandas as pd

# Define the 5S steps and example audit items
data = {
    '5S Step': [
        'Sort', 'Sort',
        'Set in Order', 'Set in Order',
        'Shine', 'Shine',
        'Standardize', 'Standardize',
        'Sustain', 'Sustain'
    ],
    'Audit Item': [
        'Remove unnecessary items', 'Organize work area',
        'Label storage locations', 'Arrange tools for easy access',
        'Clean workspaces regularly', 'Inspect equipment for cleanliness',
        'Develop standard operating procedures', 'Document best practices',
        'Conduct regular 5S audits', 'Provide ongoing training'
    ],
    'Rating': ['', '', '', '', '', '', '', '', '', ''],
    'Comments': ['', '', '', '', '', '', '', '', '', '']
}

# Create a DataFrame with the example audit items
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = '5s_audit_checklist.xlsx'
df.to_excel(output_file, index=False)

print(f"5S Audit Checklist template created and saved as {output_file}")
