

def split(df):
    """Split a dataframe in to groups of columns for the strings, numbers, contstants 
    and a array of column names for the columns that are completely empty"""
    import matplotlib.pyplot as plt 
    import metapack as mp
    import pandas as pd
    import numpy as np

    o_cols = []
    n_cols = []
    empty = []
    const = [] 

    for cn in df.columns:
        c = df[cn]

        nu = c.nunique()

        if nu == 0:
            empty.append(cn)
        elif nu == 1:
            const.append(cn)
        elif c.dtype == np.dtype('O'):
            o_cols.append(cn)
        else:
            n_cols.append(cn)

    return df[o_cols], df[n_cols], df[const].drop_duplicates(), empty



def scatter_plot():
    
    from pandas.plotting import scatter_matrix
    scatter_matrix(df[n_cols].sample(10000), alpha=0.2, figsize=(12, 12), diagonal='kde');