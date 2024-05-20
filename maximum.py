import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

raws =10
columnName= 'Age'
data = df[columnName]
numbers = data.head(raws)

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number> maximum:
         return maximum

print(find_max(numbers)) 