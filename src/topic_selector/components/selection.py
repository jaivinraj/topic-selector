from __init__ import dashapp
from dash import html
from dash.dependencies import Input, Output, State
from topic_selector.dash_utils import dash_table_to_dataframe
from topic_selector.selection.topic_selection import select_topic


selection_layout = html.Div(
    [
        # output for chosen topic
        html.Div(id="chosen-topic-output", style={"whiteSpace": "pre-line"}),
        # button to trigger topic
        html.Button("Choose topic", id="choose-topic-button", n_clicks=0),
    ]
)


@dashapp.callback(
    Output("chosen-topic-output", "children"),
    Input("choose-topic-button", "n_clicks"),
    Input("task-table", "data"),
    Input("task-table", "columns"),
)
def choose_topic(n_clicks, rows, columns):
    df = dash_table_to_dataframe(rows, columns)
    topic = select_topic(df["Task Name"].values)
    if n_clicks > 0:
        return "Your chosen topic is: {}".format(topic)
