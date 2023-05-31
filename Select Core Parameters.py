# Read the CSV file into a DataFrame
df = pd.read_csv('main_df_1.csv')

# Find all the unique values in the 'CharacteristicName' column
unique_values = df['CharacteristicName'].unique()



# Define the elements needed as a list
elements_needed = ['Alkalinity', 'Boron', 'Chromium', 'Copper', 'Calcium', 'Chloride', 'Fluoride', 'Magnesium', 'Potassium', 'Sodium', 'Dissolved oxygen (DO)', 'pH', 'Escherichia coli', 'Inorganic nitrogen (nitrate and nitrite) as N', 'Lead', 'Mercury', 'Turbidity', 'Conductivity', 'Zinc', 'Arsenic', 'Cadmium', 'Methamphetamine', 'Selenium', 'Iron']

# Filter the DataFrame to include only rows where 'CharacteristicName' is in the list of elements needed
filtered_df = df[df['CharacteristicName'].isin(elements_needed)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('New_filtered.csv')

