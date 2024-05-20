import pandas as pd

df = pd.read_csv("C:/Users/Admin/Documents/My Modules/Technical Programing 2/dataset - 2020-09-24.csv")

column= 'Name'
word_list = df[column]
word = input('enter the name')

def search(word_list,word):
    for name in word_list:
        if name == word:
            return True
    return False

print(search(word_list,word))