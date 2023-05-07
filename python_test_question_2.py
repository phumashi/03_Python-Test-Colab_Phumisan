
# Suppose we have a large chunk of users (1 Million) with their purchase record in last month. The purchase record contains the buyer id, total amount of orders, and the amount of money they spend. 
# We have a prior knowledge that the average order and spend value of this user group has are 3.5 and 25 respectively.

# Now, we want to make an experiment on this group of users. What we have to do is to randomly split this group into two.  
# The first group, which is roughly 95% of the chunk, will receive a free shipping voucher.
# The other group, the rest 5%, will not receive anything (sadly). 
# The challenge is that we have to make sure the two groups behave the same, so that we can benchmark the performance of the voucher easily.
# So we decided to have the orders and the spending of two groups to be equal to be 3.5 and 25, the same as the large chunk.
# Of course, it is impossible to have the exact same numbers, so we allow some room for error of 1% on both metrics.

# That means, if the error of order or spending of the two groups differ from the target values by 1%, we rechoose the group of users. This process repeats untill both metrics differ less than 1%

# The script of randomisation is almost complete. Only the error checking is left unknown to us. Can you help us with that?

import pandas as pd
import numpy as np


def weird_division(n, d):
    if (n == 0 and d == 0) or (d == 0):
        return 1
    return n / d 


df = pd.read_csv('some_data.csv')

#Get list of columns in the dataframe
#The first column is the id of buyer, the rest are the metrics.
cols_name = df.columns.values[1:]
target_value = [3.5,25] 
target_value_dict = dict(zip(cols_name,target_value))


tolerance = [0.01,0.01]
tolerance_dict = dict(zip(cols_name,tolerance))


#set up while loop to random sample until getting within tolerance
i = 0
chosen_average_result_dict = dict(zip(cols_name,np.zeros(cols_name.size)))
therest_difference_dict = dict(zip(cols_name,np.zeros(cols_name.size)))

while True:

    #Initialize parameters
    check = 0

    #obtain random sampling
    df["allocation"] = np.random.choice(["chosen","the rest"], p=[0.05, 0.95], size=df.shape[0])
    #obtain test statistics
    
    for key in cols_name:
        chosen_average_result_dict[key] = df[df["allocation"] == "chosen"][key].mean()
        therest_average_result_dict[key] = df[df["allocation"] == "the rest"][key].mean()


        #Calculate percentage different between each metric of chosen group and the rest
        chosen_difference_dict[key] = abs(weird_division(chosen_average_result_dict[key],target_value_dict[key]) -1)
        therest_difference_dict[key] = abs(weird_division(chosen_average_result_dict[key],target_value_dict[key]) -1)
       
        #If fail then add value to check
    for key in cols_name:
        chosen_average_result_dict[key] = df[df["allocation"] == "chosen"][key].mean()
        therest_average_result_dict[key] = df[df["allocation"] == "the rest"][key].mean()

        # Calculate percentage difference between each metric of chosen group and the rest
        chosen_difference_dict[key] = abs(weird_division(chosen_average_result_dict[key], target_value_dict[key]) - 1)
        therest_difference_dict[key] = abs(weird_division(therest_average_result_dict[key], target_value_dict[key]) - 1)

        # Check if the absolute percentage error exceeds the tolerance level
        if chosen_difference_dict[key] > tolerance_dict[key] or therest_difference_dict[key] > tolerance_dict[key]:
            check = 1
            break




    #If check is 0 then pass
    if check == 0: break

    print(i)
    i = i+1


    
#print final percentage different
for key, value in chosen_difference_dict.items():
    print('chosen  ----' + key + ' absolute percentage error: ' + "{:.2%}".format(value))
for key, value in therest_difference_dict.items():
    print('The rest  ----' + key + ' absolute percentage error: ' + "{:.2%}".format(value))

