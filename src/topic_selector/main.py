"""Script to run the Dash app"""

from __init__ import dashapp
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
from dash_bootstrap_components import themes
import pandas as pd
from topic_selector.components.task_table import table_layout
from topic_selector.components.selection import selection_layout

dashapp.layout = html.Div([selection_layout, table_layout])


if __name__ == "__main__":
    dashapp.run_server(
        debug=True,
        host="0.0.0.0",
    )
