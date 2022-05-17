"""Helper functions for Dash"""
import pandas as pd


def dash_table_to_dataframe(rows, columns):
    """Create a dataframe from a dash table

    Parameters
    ----------
    rows : iterable
        This is actually the 'data' element of a dash table
    columns : iterable
        The columns element of a dash table

    Returns
    -------
    pd DataFrame
        Table as a dataframe
    """
    return pd.DataFrame(rows, columns=[c["name"] for c in columns])
