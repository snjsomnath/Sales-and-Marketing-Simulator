#creates a dictionary for products to be included in the game
#each product has a low med high ranking, corresponding to the target group it belongs to
import csv
from pathlib import Path
import os

product_data = []
input_file = csv.DictReader(open("product_data/product_data.csv"))
for row in input_file:
    product_data.append(row)

print(product_data[0])