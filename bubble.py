import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

raws =10
columnName= 'Age'
data = df[columnName]
numbers = data.head(raws)

def bubble_sort(numbers):
    n =len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

    print(bubble_sort(numbers)) 