import pandas as pd

# read the text file
with open('input.txt', 'r') as f:
    lines = f.readlines()

# remove newline character from each line
lines = [line.strip() for line in lines]

# split each line into columns
data = [line.split(' ') for line in lines]

df_data = {'grass_date':data[0][0]}
print(df_data)

# # create a dataframe from the data
# df = pd.DataFrame(data, columns=['grass_date', 'timestamp', 'message_type', 'name', 'message'])

# # save the dataframe to an Excel file
# df.to_excel('output.xlsx', index=False)