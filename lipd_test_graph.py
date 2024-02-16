import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
# file_path = 'path_to_your_downloaded_file/Cleaned_LipidTestsAndVisitToDoctor.xlsx'  # Update this to the actual path where you saved the file
data = pd.read_excel('cleaned_data.xlsx')

# Convert 'Date' to datetime format, if it's not already
data['Date'] = pd.to_datetime(data['Date'])

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(data['Date'], data['Total Cholesterol'], label='Total Cholesterol', marker='o')
plt.plot(data['Date'], data['HDL'], label='HDL', marker='x')
plt.plot(data['Date'], data['Triglycerides'], label='Triglycerides', marker='^')
plt.plot(data['Date'], data['LDL (estimated formula)'], label='LDL (estimated formula)', marker='s')
plt.plot(data['Date'], data['LDL (estimated website)'], label='LDL (estimated website)', marker='d')

# Enhancing the plot
plt.title('Lipid Measurements Over Time')
plt.xlabel('Date')
plt.ylabel('Measurement')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()
