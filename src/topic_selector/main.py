from __init__ import dashapp
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
from dash_bootstrap_components import themes
import pandas as pd
from topic_selector.components.task_table import task_table
from topic_selector.components.selection import selection_layout

# app = Dash(
#     __name__,
#     external_stylesheets=[
#         themes.BOOTSTRAP,
#         "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
#     ],
# )

dashapp.layout = html.Div([selection_layout, task_table])

# @app.callback(
#     Output("table-editing-simple-output", "figure"),
#     Input("table-editing-simple", "data"),
#     Input("table-editing-simple", "columns"),
# )
# def display_output(rows, columns):
#     df = pd.DataFrame(rows, columns=[c["name"] for c in columns])
#     return {
#         "data": [
#             {
#                 "type": "parcoords",
#                 "dimensions": [
#                     {"label": col["name"], "values": df[col["id"]]} for col in columns
#                 ],
#             }
#         ]
#     }


if __name__ == "__main__":
    dashapp.run_server(
        debug=True,
        host="0.0.0.0",
    )
