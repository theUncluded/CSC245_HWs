import pandas as pd

# Read the Titanic dataset
titanic_df = pd.read_csv('titanic.csv')

# 1. Print a concise summary of the dataset
print("Concise summary of the dataset:")
print(titanic_df.info())

# 2. Extract the column labels, shape, and data types of the dataset
print("Column labels:")
print(titanic_df.columns)
print("Shape of the dataset:")
print(titanic_df.shape)
print("Data types of the dataset:")
print(titanic_df.dtypes)

# 3. Create a Pivot table with multiple indexes
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass'], values=['Survived'], aggfunc='mean')
print("Pivot table with multiple indexes:")
print(pivot_table)

# 4. Find survival rate by gender on various classes
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass'], values=['Survived'], aggfunc='mean')
print("Survival rate by gender on various classes:")
print(pivot_table)

# 5. Find survival rate by gender
pivot_table = pd.pivot_table(titanic_df, index=['Sex'], values=['Survived'], aggfunc='mean')
print("Survival rate by gender:")
print(pivot_table)

# 6. Find survival rate by gender, age-wise of various classes
titanic_df['AgeGroup'] = pd.cut(titanic_df['Age'], bins=[0, 10, 30, 60, 80])
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass', 'AgeGroup'], values=['Survived'], aggfunc='mean')
print("Survival rate by gender, age-wise of various classes:")
print(pivot_table)

# 7. Partition each of the passengers into four age categories
titanic_df['AgeCategory'] = pd.cut(titanic_df['Age'], bins=[0, 10, 30, 60, 80], labels=['Child', 'Young Adult', 'Adult', 'Senior'])
print("Passengers partitioned into age categories:")
print(titanic_df[['Age', 'AgeCategory']])

# 8. Count survival by gender, age categories-wise of various classes
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass', 'AgeCategory'], values=['Survived'], aggfunc='sum')
print("Survival count by gender, age categories-wise of various classes:")
print(pivot_table)

# 9. Find survival rate by gender, age of the different categories of various classes
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass', 'AgeCategory'], values=['Survived'], aggfunc='mean')
print("Survival rate by gender, age of the different categories of various classes:")
print(pivot_table)

# 10. Find survival rate by gender, age of the different categories of various classes, with fare as a dimension of columns
titanic_df['FareCategory'] = pd.qcut(titanic_df['Fare'], q=2, labels=['Low', 'High'])
pivot_table = pd.pivot_table(titanic_df, index=['Sex', 'Pclass', 'AgeCategory'], columns=['FareCategory'], values=['Survived'], aggfunc='mean')
print("Survival rate by gender, age of the different categories of various classes, with fare as a dimension of columns:")
print(pivot_table)