"""
@author: Faseela Kuttikkattu Karim

"""


def merge_table(df1, df2, col):
    import pandas as pd

    """
    Given two dataframes, and a column, return a dataframe that has been
    left merged by the column.
    
    Parameters
    ----------
    df1 : pandas.core.frame.DataFrame
        The left dataframe to be merged
    df2 : pandas.core.frame.DataFrame
        The right dataframe to be merged
    grouping_col : str
        The column to merge the data on     
        
    Returns
    -------
    pandas.core.frame.DataFrame 
        A merged dataframe.
        
    Raises
    ------
    TypeError
        If the input argument df1 is not of type pandas.core.frame.DataFrame
    TypeError
        If the input argument df2 is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument col is not in the df1 and df2 columns
   
    Examples
    --------
    >>> merge_table(helper_data1,helper_data2, 'id')

    """

    # Checks if a dataframe is the type of object being passed into the df1 argument
    if not isinstance(df1, pd.DataFrame):
        raise TypeError("The data argument is not of type DataFrame")
    # Checks if a dataframe is the type of object being passed into the df1 argument
    if not isinstance(df2, pd.DataFrame):
        raise TypeError("The df2 argument is not of type DataFrame")

    # Tests that the the merge column is in the dataframe df1
    assert col in df1.columns, "The  merge column does not exist in the dataframe df1"

    # Tests that the the merge column is in the dataframe df2
    assert col in df2.columns, "The merge column does not exist in the dataframe df2"

    res = df1.merge(df2, how="left", on=col)

    # convert to a dataframe
    res = pd.DataFrame(res)

    # reset the index
    res = res.reset_index()

    # return the result
    return res
