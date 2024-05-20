import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

raws =10
columnName= 'Age'
data = df[columnName]
numbers = data.head(raws)

def check_first(numbers):
    def find_sum(numbers):
        total=0
        for num in numbers:
            tatal= total+ num
        return total

print(find_sum(numbers)) 