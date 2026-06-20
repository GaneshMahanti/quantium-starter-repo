import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("pink_morsel_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Region"] = df["Region"].astype(str).str.strip().str.lower()
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "background": "linear-gradient(135deg, #eef2ff 0%, #f8fafc 100%)",
        "padding": "40px 20px",
        "fontFamily": "Arial, sans-serif",
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1100px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "18px",
                "boxShadow": "0 10px 30px rgba(0,0,0,0.08)",
            },
            children=[
                html.H1(
                    "Soul Foods Pink Morsel Sales Visualiser",
                    id="app-header",
                    style={
                        "textAlign": "center",
                        "color": "#111827",
                        "marginBottom": "10px",
                    },
                ),
                html.P(
                    "Explore Pink Morsel sales over time and filter by region to compare trends before and after the 15 January 2021 price increase.",
                    style={
                        "textAlign": "center",
                        "color": "#4b5563",
                        "fontSize": "16px",
                        "marginBottom": "30px",
                    },
                ),
                html.Div(
                    style={
                        "backgroundColor": "#f8fafc",
                        "border": "1px solid #e5e7eb",
                        "borderRadius": "12px",
                        "padding": "18px 20px",
                        "marginBottom": "24px",
                    },
                    children=[
                        html.Label(
                            "Select region:",
                            style={
                                "display": "block",
                                "fontWeight": "bold",
                                "marginBottom": "12px",
                                "color": "#1f2937",
                            },
                        ),
                        dcc.RadioItems(
                            id="region-picker",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True,
                            style={"display": "flex", "gap": "18px", "flexWrap": "wrap"},
                            labelStyle={
                                "display": "inline-flex",
                                "alignItems": "center",
                                "marginRight": "14px",
                                "fontSize": "15px",
                                "color": "#374151",
                                "cursor": "pointer",
                            },
                            inputStyle={"marginRight": "6px"},
                        ),
                    ],
                ),
                dcc.Graph(id="sales-chart")
            ],
        )
    ],
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-picker", "value"),
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["Region"] == selected_region]

    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    chart_title = (
        "Pink Morsel Sales Over Time - All Regions"
        if selected_region == "all"
        else f"Pink Morsel Sales Over Time - {selected_region.title()}"
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=chart_title,
        labels={"Date": "Date", "Sales": "Sales"},
        markers=True,
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        line_width=2,
    )

    if not daily_sales.empty:
        fig.add_annotation(
            x="2021-01-15",
            y=daily_sales["Sales"].max(),
            text="Price Increase",
            showarrow=True,
            arrowhead=2,
            ay=-40,
            bgcolor="white",
        )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="#f8fafc",
        font=dict(family="Arial, sans-serif", size=14, color="#111827"),
        title_font=dict(size=22),
        margin=dict(l=40, r=40, t=70, b=40),
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="#dbe2ea")

    return fig

if __name__ == "__main__":
    app.run(debug=True)
