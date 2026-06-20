import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Region"] = df["Region"].str.strip().str.lower()
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(className="app-container", children=[
    html.Div(className="card", children=[
        html.H1("Soul Foods Pink Morsel Sales Visualiser", className="title"),
        html.P(
            "Explore Pink Morsel sales over time and compare trends before and after the 15 Jan 2021 price increase.",
            className="subtitle"
        ),

        html.Div(className="controls", children=[
            html.Label("Filter by region:", className="control-label"),
            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True,
                className="radio-group",
                inputClassName="radio-input",
                labelClassName="radio-label"
            )
        ]),

        dcc.Graph(id="sales-chart", className="chart")
    ])
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time - {selected_region.title()}",
        labels={"Date": "Date", "Sales": "Sales"},
        markers=True
    )

    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="#d62728")
    fig.add_annotation(
        x="2021-01-15",
        y=daily_sales["Sales"].max() if not daily_sales.empty else 0,
        text="Price increase",
        showarrow=True,
        arrowhead=1,
        bgcolor="white"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#ffffff",
        plot_bgcolor="#f8fafc",
        font=dict(family="Arial, sans-serif", size=14),
        title_font=dict(size=22),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor="#dbe2ea")
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
