import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Generate Sample Data
np.random.seed(42)  # For reproducibility
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
product_A_sales = np.random.randint(500, 1000, size=12)
product_B_sales = np.random.randint(300, 800, size=12)
profit = np.round(np.random.uniform(5, 20, size=12), 2)  # Profit in %

# Create a DataFrame
data = pd.DataFrame({
    "Month": months,
    "Product A Sales": product_A_sales,
    "Product B Sales": product_B_sales,
    "Profit %": profit
})

# Step 2: Interactive Visualization using Plotly
# Scatter Plot for Sales of Product A and B
fig_scatter = px.scatter(
    data_frame=data,
    x="Product A Sales",
    y="Product B Sales",
    size="Profit %",  # Bubble size depends on profit percentage
    color="Profit %",
    hover_name="Month",
    title="Interactive Scatter Plot: Product A vs Product B Sales",
    labels={"Product A Sales": "Sales of Product A ($)", "Product B Sales": "Sales of Product B ($)"},
    template="plotly_dark"
)

# Line Chart for Sales Over Months
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(
    x=data["Month"], y=data["Product A Sales"],
    mode="lines+markers", name="Product A Sales",
    line=dict(color="cyan", width=3),
    marker=dict(size=8, symbol="circle")
))
fig_line.add_trace(go.Scatter(
    x=data["Month"], y=data["Product B Sales"],
    mode="lines+markers", name="Product B Sales",
    line=dict(color="magenta", width=3),
    marker=dict(size=8, symbol="square")
))

# Customize the layout
fig_line.update_layout(
    title="Sales Trend of Product A and Product B Over the Year",
    xaxis_title="Months",
    yaxis_title="Sales ($)",
    template="plotly_dark",
    hovermode="x unified"
)

# Step 3: Display the Figures
fig_scatter.show()  # Shows the interactive scatter plot
fig_line.show()     # Shows the interactive line chart
