from dash import Dash, dash_table, dcc, html
from topic_selector.dummy.dummy_data import df_dummy
from dash.dependencies import Input, Output, State
from __init__ import dashapp

cols = ["Task Name", "Description"]

task_table = dash_table.DataTable(
    id="task-table",
    columns=([{"id": p, "name": p} for p in cols]),
    data=[dict(**i) for i in df_dummy.T.to_dict().values()],
    # [dict(Model=i, **{param: 0 for param in cols}) for i in range(1, len(cols) + 1)],
    editable=True,
    row_deletable=True,
)


rowadd_button = html.Button("Add Row", id="editing-rows-button", n_clicks=0)

table_layout = html.Div([task_table, rowadd_button])


@dashapp.callback(
    Output("task-table", "data"),
    Input("editing-rows-button", "n_clicks"),
    State("task-table", "data"),
    State("task-table", "columns"),
)
def add_row(n_clicks, rows, columns):
    if n_clicks > 0:
        rows.append({c["id"]: "" for c in columns})
    return rows
