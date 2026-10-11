# Sales Analysis Project

## Project Overview

This project analyzes sales data to evaluate business performance and identify patterns in revenue, profitability, products, customers, salespersons, warehouses, categories, discounts, and monthly sales trends.

The analysis was performed using Python, Pandas, NumPy, and Matplotlib, with a focus on practical business insights and data-driven decision making.

The project includes data preparation, KPI analysis, visualization, and business insight generation.

## Key KPIs

    KPI                         VALUE
    Total Revenue               7,125.74          
    Total Profit                1,550.42
    Overall Profit Margin       21.75%
    Total Orders                100
    Total Quantity Sold         1,229
    Average Order Value         71.25
    Average Profit Per Order    15.50
    Average Quantity Per Order  12.29

## Tools & Technologies

* Python
* Pandas — Data Preparation & Analysis
* NumPy — Numerical Operations
* Matplotlib — Data Visualization
* Jupyter / Python Environment — Analysis Workflow

## Key Insights

* Daniel was the top salesperson in both total revenue and total profit.
* W001 generated the highest revenue and achieved the highest profit margin among the warehouses.
* Dried Fruits achieved the highest category profit margin at 30.95%.
* The 15% discount level was associated with the lowest average revenue per order (54.58) and the lowest profit margin (21.10%).
* June was the strongest month in terms of revenue and profit.
* Higher order quantities generally tended to be associated with higher profit, although the relationship showed considerable variation.
* Overall, the business generated a 21.75% profit margin across 100 orders.

## Visualizations

The project includes several visualizations to explore sales trends, profitability, product performance, category performance, and relationships between key business variables.

Selected visualizations include:

* Monthly Revenue & Profit Trends
* Revenue & Profit by Category
* Top Salespersons by Revenue and Profit
* Top Warehouses by Revenue and Profit
* Discount vs. Revenue Analysis
* Quantity vs. Profit Analysis

## Business Recommendations

Based on the analysis, the following actions are recommended:

* Review high discount levels: The 15% discount level was associated with lower revenue per order and lower profit margin. Discount policies should therefore be evaluated carefully, especially at higher discount levels.
* Learn from top performers: Daniel’s strong performance in both revenue and profit can be studied to identify effective sales practices that could be shared across the sales team.
* Prioritize high-margin categories: Dried Fruits achieved the highest profit margin, suggesting an opportunity to further evaluate and develop high-margin product categories.
* Optimize warehouse performance: W001 showed strong revenue and profitability performance. Its operational practices can be reviewed to identify factors contributing to its performance.
* Investigate monthly patterns: June showed the strongest performance in the analyzed period. Understanding the factors behind this performance may help improve planning for weaker months.

## Project Structure

```text
Sales-Analysis/
├── README.md
├── sales_analysis.py
├── analysis_report.md
├── data/
│   ├── orders.xlsx
│   ├── products.xlsx
│   ├── customers.xlsx
│   └── salespersons.xlsx
└── charts/
    ├── monthly_revenue.png
    ├── monthly_profit.png
    ├── category_revenue.png
    ├── category_profit.png
    ├── top5_salespersons_revenue.png
    ├── top5_salespersons_profit.png
    ├── top5_products_revenue.png
    ├── top5_products_profit.png
    ├── discount_vs_revenue.png
    └── quantity_vs_profit.png
```

## How to Run

1. Clone or download the repository.
2. Make sure Python is installed.
3. Install the required libraries:

pip install pandas numpy matplotlib

4. Make sure the dataset files are available in the data/ folder.
5. Run the main Python script:
python sales_analysis.py
The analysis results and visualizations will be generated from the provided sales data.

## Data Disclaimer

This project uses synthetic sales and order data created for educational and portfolio demonstration purposes.

All costumers records, sales persons, orders, results are simulated and do not represent actual business operations.

Real city names may be used for route and geographic analysis, but all associated data and numerical results are fictional. 
