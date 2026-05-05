import pandas as pd

path = 'students.csv'

df = pd.read_csv(path)

print(df.shape)

print(df.columns)

print(df.head())

#check null values 
print(df.isna().sum())
#print(df.isna().sum())

# acessing a specific row 
print(df.loc[0])

print(df)

#change defualt rows to be displayed
pd.options.display.max_rows = 6
print(df)

df.info()

#data cleaning 
print(df.shape)

nonempty = df.dropna()

print(nonempty.shape)

copy = df.copy()

copy.dropna(inplace = True)

print(copy.shape)

pd.options.display.max_rows = 50

print(copy.isna().sum())

for col in copy.columns:
    if copy[col].dtype == "object": #string literal 
        copy[col].fillna( copy[col].mode()[0], inplace = True)
    else:
        copy[col].fillna(copy[col].mean(), inplace = True)

print(copy.isna().sum())