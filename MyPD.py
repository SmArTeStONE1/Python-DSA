import pandas as pd

data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    "Maths": [85, 90, 95],
    "Science": [88, 92, 94],
    "English": [82, 89, 91]
}
MyDF = pd.DataFrame(data)

print(MyDF['Maths'].mean())