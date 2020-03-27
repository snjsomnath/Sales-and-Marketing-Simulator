import csv
from pathlib import Path
import os

pathlist = Path("region_data").glob('**/*.csv')
for path in pathlist:
     # because path is object not string
     path_in_str = str(path)
     region = str(os.path.basename(path_in_str)).strip(".csv")
     #print (region)
     #print(path_in_str)

#Would be nice to use the above code to generate
#list of all ".csv" files in path_in_str
#list of all file names with ".csv" dropped
#iterate on these two lists to create all dictionaries for csv files in "region_data"
with open("region_data/region_mena.csv", mode='r') as infile:
    reader = csv.reader(infile)
    region_mena = {rows[0]:rows[1] for rows in reader}
print(region_mena.keys())
