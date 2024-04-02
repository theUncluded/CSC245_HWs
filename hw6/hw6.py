import pandas as pd
import matplotlib.pyplot as plt
#Ex 1
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'])
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Total Profit per Month')
plt.show()

#Ex2
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'], linestyle='dotted', color='red', marker='o', markerfacecolor='red', linewidth=3)
plt.xlabel('Month Number')
plt.ylabel('Sold units number')
plt.title('Total Profit per Month')
plt.legend(['Total Profit'], loc='lower right')
plt.show()

#Ex3
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for column in columns:
    plt.plot(data['month_number'], data[column], label=column)
plt.xlabel('Month Number')
plt.ylabel('Sales units')
plt.title('Sales data')
plt.legend()
plt.show()

#Ex4
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
plt.scatter(data['month_number'], data['toothpaste'], color='blue')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Toothpaste Sales data')
plt.grid(linestyle='-')
plt.show()

#Ex5
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
width = 0.4
plt.bar(data['month_number'] - width/2, data['facecream'], width=width, label='Face cream')
plt.bar(data['month_number'] + width/2, data['facewash'], width=width, label='Face wash')
plt.xlabel('Month')
plt.ylabel('Number of units Sold')
plt.title('Facewash and facecream sales data')
plt.legend()
plt.show()

#Ex6
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
plt.bar(data['month_number'], data['bathingsoap'])
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Sales data for Bathing soap')
plt.savefig('bathingsoap_sales_data.png')
plt.show()

#Ex7
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
plt.hist(data['total_profit'])
plt.xlabel('Profit range')
plt.ylabel('Frequency')
plt.title('Profit Range Histogram')
plt.show()

#Ex8
data = pd.read_csv('company_sales_data.csv')
total_units_sold = data.iloc[:, 1:7].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_units_sold, labels=total_units_sold.index, autopct='%1.1f%%')
plt.title('Percentage of units sold for each product')
plt.show()

#Ex9
data = pd.read_csv('company_sales_data.csv')
fig, axs = plt.subplots(1, 2, figsize=(15, 6))

axs[0].plot(data['month_number'], data['bathingsoap'])
axs[0].set_title('Sales data of Bathing soap')
axs[0].set_xlabel('Month Number')
axs[0].set_ylabel('Number of units sold')

axs[1].plot(data['month_number'], data['facewash'])
axs[1].set_title('Sales data of Facewash')
axs[1].set_xlabel('Month Number')
axs[1].set_ylabel('Number of units sold')

plt.tight_layout()
plt.show()

#Ex10
data = pd.read_csv('company_sales_data.csv')
plt.figure(figsize=(10, 6))
columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
plt.stackplot(data['month_number'], data[columns].values.T, labels=columns)
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.title('Sales Data')
plt.legend(loc='upper left')
plt.show()