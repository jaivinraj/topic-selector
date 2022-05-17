from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from topic_selector.components.task_table import task_table

app = Dash(__name__)

app.layout = html.Div([task_table])


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
    app.run_server(
        debug=True,
        host="0.0.0.0",
    )
