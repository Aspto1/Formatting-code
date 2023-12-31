import pandas as pd

def fill_missing_with_zero(column):
    # Convert the column to a string and replace missing values
    column_str = column.astype(str)
    column_str = column_str.replace(',,', ',0,')
    while ',,' in column_str:
        column_str = column_str.replace(',,', ',0,')
    return column_str

# Read the CSV file
data = pd.read_csv('C:\\Football_stats\\remove,,.txt')

#Drop columns
data.drop(columns=['-9999'], inplace=True)

#Apply the function to each column
for col in data.columns:
    data[col] = fill_missing_with_zero(data[col])


# Save the modified DataFrame
data.to_csv('C:\\Football_stats\\remove,,.txt', index=False)
