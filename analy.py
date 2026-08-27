# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Adidas Dashboard",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* Main title */
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    padding-bottom: 20px;
}

/* KPI labels */
[data-testid="stMetricLabel"] {
    color: #333333 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* KPI values */
[data-testid="stMetricValue"] {
    color: #111111 !important;
    font-size: 32px !important;
    font-weight: 700 !important;
}

/* KPI cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border-radius: 8px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# DASHBOARD TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🏅Adidas_Business_Analytics_Dashboard</div>',
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    df = pd.read_excel("Adidas.xlsx")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Invoice Date
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"],
        errors="coerce"
    )

    # Numeric columns
    numeric_columns = [
        "TotalSales",
        "OperatingProfit",
        "UnitsSold",
        "OperatingMargin",
        "PriceperUnit"
    ]

    # Clean numeric data
    for col in numeric_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace("%", "", regex=False)
            .str.strip()
        )

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # Convert percentage to decimal
    if df["OperatingMargin"].max() > 1:
        df["OperatingMargin"] = (
            df["OperatingMargin"] / 100
        )

    return df


# Load dataset
df = load_data()


# ============================================================
# SIDEBAR FILTERS
# ============================================================
#sidebar logo
st.sidebar.image("adidas-logo.jpg",caption="Adidas_Analytics")

st.sidebar.header("Dashboard Filters")


region = st.sidebar.multiselect(
    "🌍 Select Region",
    options=sorted(df["Region"].dropna().unique()),
    default=sorted(df["Region"].dropna().unique())
)


retailer = st.sidebar.multiselect(
    "🏪 Select Retailer",
    options=sorted(df["Retailer"].dropna().unique()),
    default=sorted(df["Retailer"].dropna().unique())
)


product = st.sidebar.multiselect(
    "📦 Select Product",
    options=sorted(df["Product"].dropna().unique()),
    default=sorted(df["Product"].dropna().unique())
)


method = st.sidebar.multiselect(
    "🛒 Select Sales Method",
    options=sorted(df["SalesMethod"].dropna().unique()),
    default=sorted(df["SalesMethod"].dropna().unique())
)


# ============================================================
# DATE FILTER
# ============================================================

start_date = df["InvoiceDate"].min().date()
end_date = df["InvoiceDate"].max().date()


date_range = st.sidebar.date_input(
    "📅 Select Date Range",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date
)


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Retailer"].isin(retailer)) &
    (df["Product"].isin(product)) &
    (df["SalesMethod"].isin(method))
].copy()


# Apply date filter
if isinstance(date_range, tuple) and len(date_range) == 2:

    start_selected = pd.to_datetime(date_range[0])
    end_selected = pd.to_datetime(date_range[1])

    filtered_df = filtered_df[
        (filtered_df["InvoiceDate"] >= start_selected) &
        (filtered_df["InvoiceDate"] <= end_selected)
    ]


# ============================================================
# CHECK IF DATA EXISTS
# ============================================================

if filtered_df.empty:

    st.warning(
        "No data available for the selected filters."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["TotalSales"].sum()

total_profit = filtered_df["OperatingProfit"].sum()

total_units = filtered_df["UnitsSold"].sum()

avg_margin = filtered_df["OperatingMargin"].mean()

avg_price = filtered_df["PriceperUnit"].mean()

total_retailers = filtered_df["Retailer"].nunique()


# ============================================================
# KPI SECTION
# ============================================================

st.subheader("🔗 Key Performance Indicators")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        label="💰 Total Sales",
        value=f"${total_sales:,.0f}"
    )


with col2:

    st.metric(
        label="📈 Operating Profit",
        value=f"${total_profit:,.0f}"
    )


with col3:

    st.metric(
        label="📦 Units Sold",
        value=f"{total_units:,.0f}"
    )


col4, col5, col6 = st.columns(3)


with col4:

    st.metric(
        label="📊 Average Margin",
        value=f"{avg_margin:.2%}"
    )


with col5:

    st.metric(
        label="💲 Average Price",
        value=f"${avg_price:,.2f}"
    )


with col6:

    st.metric(
        label="🏪 Retailers",
        value=f"{total_retailers}"
    )


# Style KPI cards
style_metric_cards(
    background_color="#FFFFFF",
    border_left_color="#00B4D8",
    border_color="#CCCCCC",
    box_shadow=True
)


st.markdown("---")



# ============================================================
# SALES BY REGION
# ============================================================

col1, col2 = st.columns(2)


with col1:

    region_sales = (
        filtered_df
        .groupby("Region", as_index=False)["TotalSales"]
        .sum()
        .sort_values(
            "TotalSales",
            ascending=False
        )
    )

    fig_region = px.bar(
        region_sales,
        x="Region",
        y="TotalSales",
        title="Total Sales by Region",
        text_auto=".2s",
        template="plotly_white"
    )

    fig_region.update_layout(
        xaxis_title="Region",
        yaxis_title="Total Sales"
    )

    st.plotly_chart(
        fig_region,
        use_container_width=True
    )


# ============================================================
# MONTHLY SALES TREND
# ============================================================

with col2:

    monthly_sales = (
    filtered_df
    .set_index("InvoiceDate")
    .resample("M")["TotalSales"]
    .sum()
    .reset_index()
)

    fig_trend = px.line(
        monthly_sales,
        x="InvoiceDate",
        y="TotalSales",
        title="Monthly Sales Trend",
        markers=True,
        template="plotly_white"
    )

    fig_trend.update_layout(
        xaxis_title="Month",
        yaxis_title="Total Sales"
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )


# ============================================================
# PRODUCT SALES
# ============================================================

col1, col2 = st.columns(2)


with col1:

    product_sales = (
        filtered_df
        .groupby("Product", as_index=False)["TotalSales"]
        .sum()
        .sort_values(
            "TotalSales",
            ascending=False
        )
    )

    fig_product = px.bar(
        product_sales,
        x="TotalSales",
        y="Product",
        orientation="h",
        title="Sales by Product",
        template="plotly_white"
    )

    fig_product.update_layout(
        xaxis_title="Total Sales",
        yaxis_title="Product"
    )

    st.plotly_chart(
        fig_product,
        use_container_width=True
    )


# ============================================================
# PROFIT BY RETAILER
# ============================================================

with col2:

    retailer_profit = (
        filtered_df
        .groupby("Retailer", as_index=False)["OperatingProfit"]
        .sum()
        .sort_values(
            "OperatingProfit",
            ascending=False
        )
    )

    fig_retailer = px.bar(
        retailer_profit,
        x="Retailer",
        y="OperatingProfit",
        title="Operating Profit by Retailer",
        template="plotly_white"
    )

    fig_retailer.update_layout(
        xaxis_title="Retailer",
        yaxis_title="Operating Profit"
    )

    st.plotly_chart(
        fig_retailer,
        use_container_width=True
    )

st.divider()
# ============================================================
# SALES METHOD
# ============================================================

col1, col2 = st.columns(2)


with col1:

    sales_method_data = (
        filtered_df
        .groupby(
            "SalesMethod",
            as_index=False
        )["TotalSales"]
        .sum()
    )

    fig_method = px.pie(
        sales_method_data,
        names="SalesMethod",
        values="TotalSales",
        title="Sales Distribution by Method",
        hole=0.4
    )

    st.plotly_chart(
        fig_method,
        use_container_width=True
    )


# ============================================================
# TOP 10 STATES
# ============================================================

with col2:

    state_sales = (
        filtered_df
        .groupby("State", as_index=False)["TotalSales"]
        .sum()
        .sort_values(
            "TotalSales",
            ascending=False
        )
        .head(10)
    )

    fig_state = px.bar(
        state_sales,
        x="TotalSales",
        y="State",
        orientation="h",
        title="Top 10 States by Sales",
        template="plotly_white"
    )

    fig_state.update_layout(
        xaxis_title="Total Sales",
        yaxis_title="State"
    )

    st.plotly_chart(
        fig_state,
        use_container_width=True
    )


# ============================================================
# FILTERED DATA TABLE
# ============================================================

st.markdown("---")

st.subheader("📋 Filtered Sales Data")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400
)