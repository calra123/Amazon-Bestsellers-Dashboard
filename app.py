import pandas as pd
import numpy as np
import csv
import json
import plotly.graph_objects as go
import plotly.express as px
import matplotlib
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

#number of amazon revies by year
bestsellers = pd.read_csv("bestsellers with categories.csv")
df1 = bestsellers.groupby(["Year"])["Reviews", "User Rating"].mean().reset_index()
fig1 = px.scatter(df1, x="Year", y="Reviews", color="User Rating",
                 title="Number of Amazon Reviews by Year with Average User Rating")

#5 most reviewed authors
df2 = bestsellers[["Author", "Reviews"]]
df2 = df2.groupby(["Author"]).sum(["Reviews"]).reset_index()
df2 = df2.sort_values(by=['Reviews'], ascending=False)
df2 = df2.head(5)
fig2 = px.bar(df2, x='Author', y='Reviews', title="Number of Reviews of 5 Most Reviewed Authors")

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])


app.run_server(debug=True)
