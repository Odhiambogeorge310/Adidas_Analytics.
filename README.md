# Adidas Sales Analytics Dashboard

An interactive Streamlit dashboard for analyzing Adidas sales
performance across regions, retailers, products, and time.

## Project Overview

The **Adidas Sales Analytics Dashboard** provides a visual overview of
sales and profitability using business performance data. It allows users
to filter the analysis and quickly monitor key performance indicators
(KPIs), regional performance, and monthly sales trends.

The dashboard is designed to support data-driven business analysis by
turning sales data into clear and interactive visual insights.

## Dashboard Preview

The dashboard includes:

-   Adidas branding and dashboard title
-   Interactive filters for Region, Retailer, and Product
-   Key Performance Indicators
-   Total Sales by Region
-   Monthly Sales Trend
-   Sales and profitability analysis

## Key Performance Indicators

The dashboard displays the following KPIs:

  KPI                Description
  ------------------ ------------------------------------------------------
  Total Sales        Total revenue generated from the selected data
  Operating Profit   Total operating profit
  Units Sold         Total number of units sold
  Average Margin     Average operating margin
  Average Price      Average selling price per unit
  Retailers          Number of retailers represented in the selected data

The KPI values update according to the selected filters.

## Interactive Filters

Users can filter the dashboard by:

### Region

Examples include:

-   Midwest
-   Northeast
-   South
-   Southeast
-   West

### Retailer

Examples include:

-   Amazon
-   Foot Locker
-   Kohl's
-   Sports Direct
-   Walmart
-   West Gear

### Product

The product filter can be used to analyze individual Adidas product
categories.

## Visualizations

### 1. Total Sales by Region

A regional comparison showing how total sales are distributed across
different geographic regions.

This helps identify:

-   Highest-performing regions
-   Lower-performing regions
-   Regional sales differences
-   Opportunities for targeted sales strategies

### 2. Monthly Sales Trend

A time-series visualization showing changes in sales over the selected
period.

This can be used to identify:

-   Sales growth or decline
-   Seasonal patterns
-   High-performing months
-   Periods requiring further investigation

## Technology Stack

This project is built using Python and the following libraries:

-   **Python**
-   **Pandas** for data manipulation
-   **NumPy** for numerical operations
-   **Plotly** for interactive visualizations
-   **Streamlit** for the dashboard interface
-   **streamlit-extras** for enhanced dashboard components

## Project Structure

A typical project structure is:

``` text
Adidas_Analytics/
│
├── Adidas_Analytics.py
├── Adidas.xlsx
├── adidas_logo.png
├── README.md
└── requirements.txt
```

## Installation

Clone the project repository:

``` bash
git clone <your-github-repository-url>
cd Adidas_Analytics
```

Create and activate a virtual environment if required:

``` bash
python -m venv venv
```

On Windows:

``` bash
venv\Scripts\activate
```

Install the required packages:

``` bash
pip install pandas numpy streamlit plotly streamlit-extras openpyxl
```

Alternatively, if a `requirements.txt` file is included:

``` bash
pip install -r requirements.txt
```

## Running the Dashboard

Start the Streamlit application with:

``` bash
streamlit run Adidas_Analytics.py
```

Streamlit will open the dashboard in your web browser.

## Data

The dashboard uses an Excel dataset containing Adidas sales information.

Typical fields used for analysis include:

-   Invoice Date
-   Region
-   Retailer
-   Product
-   Total Sales
-   Operating Profit
-   Units Sold
-   Operating Margin
-   Price per Unit

Before analysis, numerical fields should be converted to appropriate
numeric data types and date fields should be converted to datetime
format.

## Example Business Questions

The dashboard can help answer questions such as:

1.  Which region generates the highest total sales?
2.  Which retailer contributes the most sales?
3.  Which Adidas products have the strongest performance?
4.  What is the overall operating profit?
5.  What is the average operating margin?
6.  How many units have been sold?
7.  What is the average selling price?
8.  How do sales change from month to month?
9.  Which regions or retailers may require additional attention?
10. How does product performance change when different filters are
    applied?

## Business Insights

The dashboard can be used by management and analysts to:

-   Monitor overall sales performance
-   Compare regional performance
-   Evaluate retailer contribution
-   Analyze product performance
-   Track profitability
-   Identify sales trends
-   Support business planning and decision-making

## Future Improvements

Potential improvements include:

-   Sales forecasting using machine learning
-   Profitability comparison by product
-   Retailer ranking
-   Year-over-year sales analysis
-   Regional maps
-   Monthly and quarterly performance comparisons
-   Downloadable filtered reports
-   Automated data refresh
-   Advanced predictive analytics

## Author

**George Odhiambo**

Data Analytics \| Python \| Streamlit \| Data Visualization

## License

This project is intended for educational, portfolio, and data analytics
demonstration purposes.
