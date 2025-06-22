import pandas as pd

dataset = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Ages': [23, 25, 22, 24, 26, 27, 23, 24, 25, 22],
}
MyDF = pd.DataFrame(dataset)
print("Original DataFrame:")
print(MyDF)
print('-------------------')
print('Head of the DataFrame:')
print(MyDF.head())
print('-------------------')
print('Columns in the DataFrame:')
print(MyDF.columns)
print('-------------------')
print('Describe the DataFrame:')
print(MyDF.describe())
print('-------------------')
print(MyDF['Ages'])
print('-------------------')

print(MyDF[MyDF['Ages'] > 23])
print('-------------------')
print(MyDF[MyDF['Ages'] < 23])
print('-------------------')
MyDF['Salary'] = [50000, 60000, 55000, 62000, 58000, 59000, 61000, 63000, 64000, 65000]
print("DataFrame after adding Salary column:")
print(MyDF)
print('-------------------')