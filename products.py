import pandas as pd 

data = pd.read_csv("product_data/product_data.csv") 
print(data.product_p[data.product_name =='Ted Baker'])
