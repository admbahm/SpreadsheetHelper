import pandas as pd

# Define the columns for the Kanban board
columns = ['Backlog', 'To Do', 'In Progress', 'Testing', 'Done']

# Example tasks for each column
data = {
    'Backlog': ['Task 1', 'Task 2'],
    'To Do': ['Task 3'],
    'In Progress': ['Task 4'],
    'Testing': ['Task 5'],
    'Done': ['Task 6']
}

# Create a DataFrame with the example tasks
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

# Save the DataFrame to an Excel file
output_file = 'kanban_board.xlsx'
df.to_excel(output_file, index=False)

print(f"Kanban board template created and saved as {output_file}")
