from operator import index

import pandas as pd
import matplotlib.pyplot as plt

products_df = pd.read_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\products.xlsx")
customers_df = pd.read_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\customers.xlsx")
salespersons_df = pd.read_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\salespersons.xlsx")
orders_df = pd.read_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\orders.xlsx")

# 1) inspection

print(products_df.head())
print(customers_df.head())
print(salespersons_df.head())
print(orders_df.head())

# Table dimensions
print(products_df.shape)
print(customers_df.shape)
print(salespersons_df.shape)
print(orders_df.shape)

# General information    # Format checking
products_df.info()
customers_df.info()
salespersons_df.info()
orders_df.info()

# Check for empty data
print(products_df.isnull().sum())
print(customers_df.isnull().sum())
print(salespersons_df.isnull().sum())
print(orders_df.isnull().sum())

# Check for duplicate data #
print(products_df.duplicated().sum())
print(customers_df.duplicated().sum())
print(salespersons_df.duplicated().sum())
print(orders_df.duplicated().sum())

# General statistics
print(products_df.describe(include="all"))
print(customers_df.describe(include="all"))
print(salespersons_df.describe(include="all"))
print(orders_df.describe(include="all"))


# MERGE : The main table contains whole IDs; orders
# merge priority : Always starts with the main tables.
orders_customers_df = orders_df.merge(customers_df, on= "Customer_ID", how="left") # Default format.
#print(orders_customers_df)

orders_customers_products_df = orders_customers_df.merge(products_df, on="Product_ID", how="left")
#print(orders_customers_products_df)

master_df = orders_customers_products_df.merge(salespersons_df, on="Salesperson_ID", how="left")
print(master_df)

print(master_df.shape) # right merge checking, Rows not being added.
print(master_df.head())
print(master_df.info)
print(master_df.isnull().sum())
print(master_df.duplicated().sum())

print(master_df.columns)
#KPIs:
master_df["Profit"] = ((master_df["Unit_Price"]-master_df["Unit_Cost"]) * master_df["Quantity"] * (1 - master_df["Discount"] / 100))
print(master_df.head(10))
print(master_df["Discount"].unique())
print(master_df[["Unit_Cost", "Unit_Price"]].head(10))

# KPI 1) Total Sales Revenue
total_revenue = master_df["Total_Amount"].sum()
print(total_revenue)
# KPI 2) Total profit
total_profit = master_df["Profit"].sum()
print(total_profit)
# KPI 3) Top quantity sold by Product
product_quantity = master_df.groupby("Product")["Quantity"].sum()
product_quantity = product_quantity.sort_values(ascending =False)
print(product_quantity)
print(product_quantity.head(1))

best_selling_product = product_quantity.idxmax()
print(best_selling_product)
best_selling_value = product_quantity.max()
print(best_selling_value)

# KPI 4) Highest Revenue Product
product_revenue = master_df.groupby("Product")["Total_Amount"].sum()
highest_revenue_product = product_revenue.idxmax()
highest_revenue_value = product_revenue.max()
product_revenue_top_three = product_revenue.sort_values(ascending=False).head(3)
print(product_revenue_top_three)
print(highest_revenue_product)
print(highest_revenue_value)

# KPI 5) most profitable product
profit_products = master_df.groupby("Product")["Profit"].sum()
profit_products_top_three = profit_products.sort_values(ascending = False).head(3)
most_profitable_product = profit_products.idxmax()
most_profitable_value = profit_products.max()
print(profit_products_top_three)
print(most_profitable_product)
print(most_profitable_value)

# KPI 6) total quantity
total_quantity = master_df["Quantity"].sum()
print(total_quantity)

## KPI haye Customer:
# KPI 7) top customer by revenue
customer_revenue = master_df.groupby("Customer")["Total_Amount"].sum()
customer_revenue_top_three = customer_revenue.nlargest(3) # = sort_values(ascending = False).head(3)
best_customer_revenue = customer_revenue.idxmax()
best_customer_value = customer_revenue.max()
print(customer_revenue_top_three)
print(best_customer_revenue)
print(best_customer_value)

# Can be used:
def top_kpi(df, group_col, value_col, top_n = 3):
    result = (
        df.groupby(group_col)[value_col]
        .sum()
    )
    print(f"\nTop {top_n} {group_col}:")
    print(result.nlargest(top_n))

    print("\nBest:")
    print(result.idxmax())

    print("\nvalue:")
    print(result.max())

    return result
# Example: ( Using the function )
# Top customer by revenue:
x = top_kpi(master_df,"Customer", "Total_Amount") # Storage for reporting

# KPI 8) Top nCustomer By Profit
customer_profit = master_df.groupby("Customer")["Profit"].sum()
customer_profit_top_three = customer_profit.nlargest(3)
best_customer_profit = customer_profit.idxmax()
best_customer_profit_value = customer_profit.max()
print(customer_profit)
print(customer_profit_top_three)
print(best_customer_profit)
print(best_customer_profit_value)

# KPI 9) Top Salesperson Revenue
salesperson_revenue = master_df.groupby("Salesperson")["Total_Amount"].sum()
salesperson_revenue_top_three = salesperson_revenue.nlargest(3)
best_salesperson_revenue = salesperson_revenue.idxmax()
best_salesperson_revenue_value = salesperson_revenue.max()
print(salesperson_revenue_top_three)
print(best_salesperson_revenue)
print(best_salesperson_revenue_value)

# KPI 10) Average Order Value ( Average value for each order )
average_order_value = master_df["Total_Amount"].mean()
print(average_order_value)

# KPI 11 ) top salesperson by profit
salesperson_profit = master_df.groupby("Salesperson")["Profit"].sum()
salesperson_profit_top_three = salesperson_profit.nlargest(3)
best_salesperson_profit = salesperson_profit.idxmax()
best_salesperson_profit_value = salesperson_profit.max()
print(salesperson_profit_top_three)

# Warehouse KPI - Logistic
# KPI 12) revenue by warehouse
warehouse_revenue = master_df.groupby("Warehouse_ID")["Total_Amount"].sum()
warehouse_revenue_top_three = warehouse_revenue.nlargest(3)
best_warehouse_revenue = warehouse_revenue.idxmax()
best_warehouse_revenue_value = warehouse_revenue.max()

# KPI 13) profit by warehouse
warehouse_profit = master_df.groupby("Warehouse_ID")["Profit"].sum()
warehouse_profit_top_three = warehouse_profit.nlargest(3)
best_warehouse_profit = warehouse_profit.idxmax()
best_warehouse_profit_value = warehouse_profit.max()

# KPI 14) average profit margin by warehouse
master_df["Profit_Margin"] = (master_df["Profit"] / master_df["Total_Amount"]) * 100
print(master_df.head(4))

warehouse_average_profit_margin = master_df.groupby("Warehouse_ID")["Profit_Margin"].mean()

warehouse_average_profit_margin_top_three = warehouse_average_profit_margin.nlargest(3)
best_warehouse_average_profit_margin= warehouse_average_profit_margin.idxmax()
best_warehouse_average_profit_margin_value = warehouse_average_profit_margin.max()
print(warehouse_average_profit_margin_top_three)

# category KPI s:
# KPI 15) revenue by category
category_revenue = master_df.groupby("Category")["Total_Amount"].sum()
category_revenue_top_three = category_revenue.nlargest(3)
best_category_revenue = category_revenue.idxmax()
best_category_revenue_value = category_revenue.max()
print(category_revenue_top_three)

# KPI 16) profit by category
category_profit = master_df.groupby("Category")["Profit"].sum()
category_profit_top_three = category_profit.nlargest(3)
best_category_profit = category_profit.idxmax()
best_category_profit_value = category_profit.max()
print(category_profit_top_three)

# KPI 17) average profit margin by category
category_average_profit_margin = master_df.groupby("Category")["Profit_Margin"].mean()
category_average_profit_margin_top_three = category_average_profit_margin.nlargest(3)
print(category_average_profit_margin_top_three)

# TIME ANALYSIS KPI s:
print(master_df["Order_Date"].head(3))
# Check not to be in STR mood --->
master_df["Order_Date"] = pd.to_datetime(master_df["Order_Date"])
print(master_df.dtypes)

# KPI 18) monthly Revenue

## Displaying the month name:
master_df["Month"] = master_df["Order_Date"].dt.strftime("%B")
print(master_df.head(3))

monthly_revenue = master_df.groupby("Month")["Total_Amount"].sum()
monthly_revenue_top_three = monthly_revenue.nlargest(3)
highest_monthly_revenue = monthly_revenue.idxmax()
highest_monthly_revenue_value = monthly_revenue.max()
print(monthly_revenue_top_three)

# KPI 19) monthly profit
monthly_profit = master_df.groupby("Month")["Profit"].sum()
monthly_profit_top_three = monthly_profit.nlargest(3)
best_monthly_profit = monthly_profit.idxmax()
best_monthly_profit_value = monthly_profit.max()
print(monthly_profit_top_three)

# KPI 20) monthly orders ( Number )
monthly_orders = master_df.groupby("Month")["Order_ID"].nunique()
print(monthly_orders.head(3))
monthly_orders_top_three = monthly_orders.nlargest(3)
best_monthly_orders = monthly_orders.idxmax()
best_monthly_orders_value = monthly_orders.max()
print(monthly_orders_top_three)

# KPI 21) Monthly Quantity Sold (sum)
monthly_quantity_sold = master_df.groupby("Month")["Quantity"].sum()
print(monthly_quantity_sold)
monthly_quantity_sold_top_three = monthly_quantity_sold.nlargest(3)
best_monthly_quantity_sold = monthly_quantity_sold.idxmax()
best_monthly_quantity_sold_value = monthly_quantity_sold.max()
print(monthly_quantity_sold_top_three)

### Visualization ###
# Placing the months in consecutive order
month_order = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

# Monthly Revenue ( line chart ) ---> trend : line
monthly_revenue = monthly_revenue.reindex(month_order).dropna()

plt.figure(figsize=(8,5))
plt.plot(monthly_revenue.index, monthly_revenue.values, marker = "o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\monthly_revenue.png")
#plt.show()

# Monthly Profit ( line chart )
monthly_profit = monthly_profit.reindex(month_order).dropna()

plt.figure(figsize=(8,5))
plt.plot(monthly_profit.index, monthly_profit.values, marker = "o")
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\monthly_profit.png")
#plt.show()

# Revenue by Category : Category comparison; bar chart
plt.figure(figsize = (8,5))
plt.bar(category_revenue.index, category_revenue.values)
plt.title("Revenue By Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\category_revenue.png")
#plt.show()

# Profit By Category
plt.figure(figsize = (8,5))
plt.bar(category_profit.index, category_profit.values)
plt.title("Profit By Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\category_profit.png")
#plt.show()

# Top 5 Products by Revenue  (bar cart)
top5_products_revenue = product_revenue.nlargest(5)

plt.figure(figsize=(8,5))
plt.bar(top5_products_revenue.index, top5_products_revenue.values)
plt.title("Top Five Products Revenue")
plt.xlabel("Top Five Products")
plt.ylabel("Revenue")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\top5_products_revenue.png")
#plt.show()

# top 5 Products by Profit (bar chart)
top5_products_profit = profit_products.nlargest(5)

plt.figure(figsize = (8,5))
plt.bar(top5_products_profit.index, top5_products_profit.values)
plt.title("Top Five Profit By Products")
plt.xlabel("Top Five Products")
plt.ylabel("Profit")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\top5_products_profit.png")
#plt.show()

# top 5 customers by revenue
top5_customers_revenue = customer_revenue.nlargest(5)
plt.figure(figsize = (8,5))
plt.bar(top5_customers_revenue.index, top5_customers_revenue.values)
plt.title("Top Five Customers Revenue")
plt.xlabel("Top Five Customers")
plt.ylabel("Revenue")
#plt.show()

# top 5 customers by profit
top5_customers_profit = customer_profit.nlargest(5)
plt.figure(figsize = (8,5))
plt.bar(top5_customers_profit.index, top5_products_profit.values)
plt.title("Top Five Customers Profit")
plt.xlabel("Top Five Customers")
plt.ylabel("Profit")
#plt.show()

# top 5 salespersons by revenue
top5_salespersons_revenue = salesperson_revenue.nlargest(5)
plt.figure(figsize = (8,5))
plt.bar(top5_salespersons_revenue.index, top5_salespersons_revenue.values)
plt.title("Top Five Salespersons Revenue")
plt.xlabel("Top Five Salespersons")
plt.ylabel("Revenue")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\top5_salespersons_revenue.png")
#plt.show()

# top 5 salespersons by profit
top5_salespersons_profit = salesperson_profit.nlargest(5)
plt.figure(figsize = (8,5))
plt.bar(top5_salespersons_profit.index, top5_salespersons_profit.values)
plt.title("Top Five Salespersons Profit")
plt.xlabel("Top Five Salespersons")
plt.ylabel("Profit")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\top5_salespersons_profit.png")
#plt.show()

# Revenue by Warehouse
plt.figure(figsize = (8,5))
plt.bar(warehouse_revenue.index, warehouse_revenue.values)
plt.title("Revenue by Warehouse")
plt.xlabel("Warehouse")
plt.ylabel("Revenue")
#plt.show()

# Profit by Warehouse
plt.figure(figsize = (8,5))
plt.bar(warehouse_profit.index, warehouse_profit.values)
plt.title("Profit by Warehouse")
plt.xlabel("Warehouse")
plt.ylabel("Profit")
#plt.show()

### Business Insights

# Insight 1 _ Revenue vs Profit
top_revenue_product = product_revenue.idxmax()
top_profit_product = profit_products.idxmax()
print("Top Revenue Product:", top_revenue_product)
print("Top Profit Product:", top_profit_product)

# Insight 2 _ Customer
top_revenue_customer = customer_revenue.idxmax()
top_profit_customer = customer_profit.idxmax()
print("Top Revenue Customer:", top_revenue_customer)
print("Top Profit Customer:", top_profit_customer)

# Insight 3 _ Warehouse Performance

print("Top Revenue Warehouse:", best_warehouse_revenue)
print("Top Profit Warehouse:", best_warehouse_profit)

# Insight 4 _ Month Performance
print("Top Revenue Month:", highest_monthly_revenue)
print("Top Profit Month:", best_monthly_profit)

# Insight 5 Discount vs Revenue; Does the biggest discount lead to the biggest sales?
discount_revenue = (master_df.groupby("Discount")["Total_Amount"].sum().sort_index())
print(discount_revenue)

plt.figure(figsize = (8,5))
plt.scatter(
    master_df["Discount"],
    master_df["Total_Amount"]
)
plt.title("Discount va Revenue")
plt.xlabel("Discount (%)")
plt.ylabel("Revenue")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\discount_vs_revenue.png")
#plt.show()

avg_revenue_by_discount = (master_df.groupby("Discount")["Total_Amount"].mean().sort_index())
print(avg_revenue_by_discount)
# --> Orders with zero percent discount had an average of 12.73 revenue points per order.
# Increasing discounts has led to a decrease in revenue.

# Insight 6 Quantity & Profit
plt.figure(figsize = (8,5))

plt.scatter(master_df["Quantity"], master_df["Profit"])
plt.title("Quantity vs Profit")
plt.xlabel("Quantity Sold")
plt.ylabel("Profit")
plt.savefig(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\charts\quantity_vs_profit.png")
#plt.show()
# --> insight report: Orders with high order quantities generally yield higher profits, but the wide dispersion indicates that
# other factors, such as unit_cost, unit_price, discount are also at play.

# Insight 8 Profit margin by Category
category_profit_margin = (category_profit/category_revenue * 100).sort_values(ascending = False)
print(category_profit_margin)
print(category_average_profit_margin) # *

# Average of whole categories ( sum profit / sum revenue )
# ---> Insight Report: The highest profit margin belongs to Honey

# insight 9 : Salespersons Performance ( Revenue & Profit )
print("Top Salesperson Profit:", best_salesperson_profit)
print("Top Salesperson Revenue:", best_salesperson_revenue)
# report : they are same.

# Insight 10 : Best warehouse profit margin <> warehouse revenue
print("Top Warehouse Profit Margin:", best_warehouse_average_profit_margin)
print("Top Revenue Warehouse:", best_warehouse_revenue)

# Insight 11 : Monthly Revenue Growth
monthly_revenue_change = monthly_revenue.pct_change() * 100
print(monthly_revenue_change)

# Sales trend each month
plt.figure(figsize=(8,5))

plt.plot(monthly_revenue_change.index, monthly_revenue_change.values, marker = "o")
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue Change (%)")
plt.xticks(rotation = 45)

plt.axhline(0, linestyle = "--")
#plt.show()
# Insight 11 : Important: Discount <> Profit Margin
discount_profit_margin = (master_df.groupby("Discount")["Profit"].sum()/master_df.groupby("Discount")["Total_Amount"].sum() * 100)
print(discount_profit_margin)
# report : The profit margin is not in increasing trend despite increasing discount.


# General KPIs:

total_orders = master_df["Order_ID"].nunique()
print(total_orders)
print(total_revenue)
print(total_profit)
print(total_quantity)

overall_profit_margin = (total_profit/total_revenue * 100)
print(overall_profit_margin)

# Performance overview

#average_order_value (total_revenue/total_orders)
print(" Average Order Value:", average_order_value)
average_profit_per_order = total_profit/total_orders
print("Average Profit Per Order:", average_profit_per_order)
average_quantity_per_order = total_quantity/ total_orders
print("Average Quantity Per Order:", average_quantity_per_order)
