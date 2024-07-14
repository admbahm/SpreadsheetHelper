import pandas as pd
import matplotlib.pyplot as plt

# Define the structure for the Burndown Chart
data = {
    'Sprint Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
    'Planned Work': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],
    'Actual Work': [100, 85, 75, 65, 55, 45, 35, 25, 15, 5]
}

# Create a DataFrame with the structure
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = 'burndown_chart.xlsx'
df.to_excel(output_file, index=False)

# Plot the Burndown Chart
plt.figure(figsize=(10, 6))
plt.plot(df['Sprint Day'], df['Planned Work'], label='Planned Work', marker='o')
plt.plot(df['Sprint Day'], df['Actual Work'], label='Actual Work', marker='o')
plt.xlabel('Sprint Day')
plt.ylabel('Work Remaining')
plt.title('Burndown Chart')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image
chart_file = 'burndown_chart.png'
plt.savefig(chart_file)

# Inform the user
print(f"Burndown Chart template created and saved as {output_file}")
print(f"Burndown Chart image saved as {chart_file}")
