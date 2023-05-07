import pandas as pd

#1.read the sale data csv file to dataframe
df = pd.read_csv('test_candidate_03.csv')

#2.groupby shop_id then sum the gmv for each shop
gmv_shop = df.groupby('shop_id')['gmv_usd'].sum()

#3.Select the top 10 shop using pandas_sort_values
top_shop = gmv_shop.sort_values(ascending=False).head(10)

#4.Print result
print(top_shop)

#Question
# Find top 10 shops who gain the highest GMV in Apr 2022