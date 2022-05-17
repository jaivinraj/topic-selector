from dash import Dash, dash_table, dcc, html
from topic_selector.dummy.dummy_data import df_dummy

cols = ["Task Name", "Description"]

task_table = dash_table.DataTable(
    id="table-editing-simple",
    columns=([{"id": p, "name": p} for p in cols]),
    data=[dict(Model=1, **i) for i in df_dummy.T.to_dict().values()],
    # [dict(Model=i, **{param: 0 for param in cols}) for i in range(1, len(cols) + 1)],
    editable=True,
)
