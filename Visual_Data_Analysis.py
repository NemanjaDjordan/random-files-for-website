import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = r'C:\Users\Administrator\Desktop\Starter\Sales_Data_Dashboard.xlsx'   # Replace with your file path
df = pd.read_excel(file_path)
# Load the data from the specified Excel file into a pandas DataFrame.
# Ensure the file path is correctly set to where the Excel file is located.

# Display the first few rows of the dataframe
print(df.head())
# Print the first few rows of the DataFrame to get an overview of the data structure and contents.

# Set the style for seaborn plots
sns.set(style="whitegrid")
# Set the aesthetic style of the plots using seaborn. "whitegrid" adds a grid to the background.

# 1. Sales breakup % by Segment
plt.figure(figsize=(10, 6))
# Create a new figure with a specific size for the plot.
segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()
# Group the data by 'Segment' and calculate the total sales for each segment.
segment_sales['Sales (%)'] = 100 * segment_sales['Sales'] / segment_sales['Sales'].sum()
# Calculate the percentage of total sales for each segment.
sns.barplot(x='Segment', y='Sales (%)', data=segment_sales, palette='viridis')
# Create a bar plot of sales percentages by segment using the 'viridis' color palette.
plt.title('Sales Breakup (%) by Segment')
plt.xlabel('Segment')
plt.ylabel('Sales (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, rotate x-axis labels for better readability, adjust layout, and display the plot.

# 2. Sales (%) by Country
plt.figure(figsize=(12, 8))
# Create a new figure with a specific size for the plot.
country_sales = df.groupby('Country')['Sales'].sum().reset_index()
# Group the data by 'Country' and calculate the total sales for each country.
country_sales['Sales (%)'] = 100 * country_sales['Sales'] / country_sales['Sales'].sum()
# Calculate the percentage of total sales for each country.
sns.barplot(x='Country', y='Sales (%)', data=country_sales, palette='coolwarm')
# Create a bar plot of sales percentages by country using the 'coolwarm' color palette.
plt.title('Sales (%) by Country')
plt.xlabel('Country')
plt.ylabel('Sales (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, rotate x-axis labels for better readability, adjust layout, and display the plot.

# 3. Sales (€) generated by customers
plt.figure(figsize=(12, 8))
# Create a new figure with a specific size for the plot.
customer_sales = df.groupby('Customer_Name')['Sales'].sum().reset_index()
# Group the data by 'Customer_Name' and calculate the total sales for each customer.
customer_sales = customer_sales.sort_values(by='Sales', ascending=False)
# Sort the customers by total sales in descending order.
sns.barplot(x='Sales', y='Customer_Name', data=customer_sales, palette='rocket')
# Create a horizontal bar plot of sales by customer using the 'rocket' color palette.
plt.title('Sales (€) Generated by Customers')
plt.xlabel('Sales (€)')
plt.ylabel('Customer Name')
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, adjust layout, and display the plot.

# 4. Monthly Generated Profit (€)
plt.figure(figsize=(12, 8))
# Create a new figure with a specific size for the plot.
monthly_profit = df.groupby('Month')['Profit'].sum().reset_index()
# Group the data by 'Month' and calculate the total profit for each month.
sns.lineplot(x='Month', y='Profit', data=monthly_profit, marker='o', color='teal')
# Create a line plot of monthly profit with markers and a specified color.
plt.title('Monthly Generated Profit (€)')
plt.xlabel('Month')
plt.ylabel('Profit (€)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, rotate x-axis labels for better readability, adjust layout, and display the plot.

# 5. Units Sold Split (%)
plt.figure(figsize=(10, 6))
# Create a new figure with a specific size for the plot.
units_sold_split = df.groupby('Segment')['Units Sold'].sum().reset_index()
# Group the data by 'Segment' and calculate the total units sold for each segment.
units_sold_split['Units Sold (%)'] = 100 * units_sold_split['Units Sold'] / units_sold_split['Units Sold'].sum()
# Calculate the percentage of total units sold for each segment.
sns.barplot(x='Segment', y='Units Sold (%)', data=units_sold_split, palette='magma')
# Create a bar plot of units sold percentages by segment using the 'magma' color palette.
plt.title('Units Sold Split (%) by Segment')
plt.xlabel('Segment')
plt.ylabel('Units Sold (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, rotate x-axis labels for better readability, adjust layout, and display the plot.

# 6. Top Sold Product
plt.figure(figsize=(12, 8))
# Create a new figure with a specific size for the plot.
top_product = df.groupby('Product_Name')['Units Sold'].sum().reset_index()
# Group the data by 'Product_Name' and calculate the total units sold for each product.
top_product = top_product.sort_values(by='Units Sold', ascending=False)
# Sort the products by total units sold in descending order.
sns.barplot(x='Units Sold', y='Product_Name', data=top_product, palette='plasma')
# Create a horizontal bar plot of units sold by product using the 'plasma' color palette.
plt.title('Top Sold Products')
plt.xlabel('Units Sold')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()
# Set the plot title, x and y labels, adjust layout, and display the plot.