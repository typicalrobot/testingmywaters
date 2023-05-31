import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv("water_quality_data.csv")

# Set the 'Year' column as the index of the DataFrame
df.set_index("Year", inplace=True)

# Standardize the data (subtract the mean and divide by the standard deviation)
standardized_df = (df - df.mean()) / df.std()

# Calculate the correlation matrix
corrmatrix = standardized_df.corr()

# Visualize the correlation matrix using seaborn
plt.figure(figsize=(12, 12))
sns.heatmap(corrmatrix, annot=True, cmap="CoolWarm", square=True, linewidths=0.5)
plt.title("Water Quality Parameters Correlation Matrix")
plt.show()