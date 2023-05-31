# Import pandas library
import pandas as pd

# Set pandas options to display all rows and columns
pd.set_option("max_rows", None)
pd.set_option("max_columns", None)

# Read data from the CSV file
df = pd.read_csv('resultphyschem.csv', low_memory=False)

# Calculate the number of missing values in each column
num_missing = df.isna().sum()

# Identify columns with more than 2 million missing values
cols_to_drop = num_missing[num_missing > 2000000].index.tolist()

# Drop columns with more than 2 million missing values
new_df = df.drop(columns=cols_to_drop)

# Calculate the number of missing values in each column of the new DataFrame
num_missing_1 = new_df.isna().sum()

# Specify the column name for filtering
column_name = 'ResultMeasureValue'

# Drop rows with missing values in the specified column
only_results_df = new_df.dropna(subset=[column_name])

# List columns to be dropped
cols_to_drop = [
    'DetectionQuantitationLimitMeasure/MeasureUnitCode', 
    'DetectionQuantitationLimitMeasure/MeasureValue', 
    'DetectionQuantitationLimitTypeName', 
    'ResultDetectionQuantitationLimitUrl', 
    'ResultDetectionConditionText'
]

# Drop specific columns
main_df = only_results_df.drop(columns=cols_to_drop)

# List more columns to be dropped
cols_to_drop = [
    'ResultAnalyticalMethod/MethodIdentifier', 
    'ResultAnalyticalMethod/MethodIdentifierContext',
    'ResultAnalyticalMethod/MethodName',
    'LaboratoryName',
    'AnalysisStartDate',
    'LastUpdated'
]

# Drop the additional columns
main_df = main_df.drop(columns=cols_to_drop)

# Select relevant columns for the final DataFrame
new_df = main_df[
    ['ActivityStartDate', 'MonitoringLocationIdentifier', 'CharacteristicName', 'ResultMeasureValue', 'ResultMeasure/MeasureUnitCode']
]

# Display the first 5 rows of the final DataFrame
new_df.head()

# Save the final DataFrame to a new CSV file
new_df.to_csv('main_df_1.csv')