import os
import pandas as pd

path = os.getcwd()
# Load the CSV file
file_path = f"{path}/Evaly.csv"  # file path
data = pd.read_csv(file_path)

# Sort the data by 'column name'
sorted_data = data.sort_values(by="P.Name").reset_index(drop=True)

# Save the sorted data to a new CSV file
sorted_data.to_csv("Sorted_Evaly.csv", index=False)

print("The data has been sorted by product name and saved as 'Sorted_Evaly.csv'.")
