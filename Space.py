import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

raws =10
columnName= 'Age'
data = df[columnName]
numbers = data.head(raws)

def duplicate_array(numbers):
    new_arr = numbers[:]
    return new_arr

print(duplicate_array(numbers))