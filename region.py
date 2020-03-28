import pandas as pd 

data = pd.read_csv("region_data/region_data.csv") 
print(data.population[data.name =='europe'])