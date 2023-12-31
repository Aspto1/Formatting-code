import pandas as pd
import os

def fill_missing_with_zero(column):
    # Convert the column to a string and replace missing values
    column_str = column.astype(str)
    column_str = column_str.replace(',,', ',0,')
    while ',,' in column_str:
        column_str = column_str.replace(',,', ',0,')
    return column_str

def append_data_with_custom_headers(df, file_path, headers, write_headers):
    # If write_headers is True, write custom headers
    if write_headers:
        with open(file_path, 'a') as file:  # Use append mode
            for header in headers:
                file.write(header + '\n')

    # Append DataFrame data without its default headers
    df.to_csv(file_path, mode='a', index=False, header=False)

# Define your custom headers
# custom_headers = [
#     "",
#     "Arizona Cardinals Roster",
#     "No.,Player,Age,Pos,G,GS,Wt,Ht,Yrs,Drafted (tm/rnd/yr)"]
# custom_headers = [
#     "",
#     "Arizona Cardinals Passing",
#     "No.,Player,Age,Pos,G,GS,QBrec,Cmp,Att,Cmp%,Yds,TD,TD%,Int,Int%,1D,Succ%,Lng,Y/A,AY/A,Y/C,Y/G,Rate,QBR,Sk,Yds,Sk%,NY/A,ANY/A,4QC,GWD"]
# custom_headers = [
# " ",
#     "Arizona Cardinals Rushing & Receiving",
#     "First Section Games,Second Rushing,Third Receiving,Forth Total YDS",
#     "No,Player,Age,Pos,|G,GS|,|Att,Yds,TD,1D,Lng,Y/A,Y/G,A/G|,|Tgt,Rec,Yds,Y/R,TD,1D,Lng,R/G,Y/G,Ctch%,Y/Tgt|,|Touch,Y/Tch,YScm|,RRTD,Fmb"]
custom_headers = [
"",
        "Arizona Cardinals Defense & Fumbles",
        "First Section Games,Second Def Interception,Third Fumbles,Forth Tackles",
       "No.,Player,Age,Pos,|G,GS|,|Int,Yds,TD,Lng,PD|,|FF,Fmb,FR,Yds,TD,Sk|,|Comb,Solo,Ast,TFL,QBHits|,Sfty"]
# Read the CSV file
data = pd.read_csv('C:\\Football_stats\\Python_Codes\\remove_,,.txt')

# Drop columns as needed
#data.drop(columns=['College/Univ', 'AV', 'Player-additional', 'BirthDate'], inplace=True)
data.drop(columns=['-9999'], inplace=True)
#data.drop(columns=['Player-additional'], inplace=True)
# Apply the function to each column
for col in data.columns:
    data[col] = fill_missing_with_zero(data[col])

# Append the data to the file with custom headers
# Change write_headers to True or False as needed
append_data_with_custom_headers(data, 'C:\\Football_stats\\All NFL Teams Roster and stats(Part 2).txt', custom_headers, write_headers=True)
