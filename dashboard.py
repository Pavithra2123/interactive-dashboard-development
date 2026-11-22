
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Create sample sales dataset
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May",
              "Jun", "Jul", "Aug", "Sep", "Oct"],
    "Sales": [12000, 15000, 18000, 14000, 20000,
              22000, 19000, 25000, 28000, 30000],
    "Profit": [3000, 4000, 5000, 3500, 6000,
               7000, 5500, 8000, 9000, 10000],
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South"]
}

df = pd.DataFrame(data)

print("INTERACTIVE DASHBOARD DATA")
print(df)

print("\nTOTAL SALES:", df["Sales"].sum())
print("TOTAL PROFIT:", df["Profit"].sum())
print("AVERAGE SALES:", df["Sales"].mean())

# Monthly sales chart
fig = px.bar(
    df,
    x="Month",
    y="Sales",
    color="Region",
    title="Monthly Sales Dashboard",
    labels={"Sales": "Sales Amount"}
)

fig.show()

# Profit analysis
fig2 = px.line(
    df,
    x="Month",
    y="Profit",
    markers=True,
    title="Monthly Profit Analysis"
)

fig2.show()

# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig3 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Region-wise Sales Distribution"
)

fig3.show()
