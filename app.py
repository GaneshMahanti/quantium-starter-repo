import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales"
    }
)

fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
fig.add_annotation(
    x="2021-01-15",
    y=daily_sales["Sales"].max(),
    text="Price increase",
    showarrow=True,
    arrowhead=1
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
