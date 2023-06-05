
"""

@author: Faseela Kuttikkattu Karim

This function creates a helper data to test the table_merge created for 
the sample solution to the Python Programmign for Data Science project.
"""

from table_merge import merge_table
import pandas as pd

def test_merge_table():

    # Create helper data and write tests for the function
    raw = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
           'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
                    'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
                    'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
                    'Evergreen Oak'], 
            'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
                              'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
                              'West end','Kitsilano', 'Arbutus-ridge']}
    raw1 = {'id': [1873, 4913, 4801, 4540, 3581,
                   4534, 1934, 4944, 1983, 1266], 
            'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
                     'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
            'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
                         6.5, 12.0, 18.0, 8.5, 23.0]}


    helper_data1 = pd.DataFrame.from_dict(raw)
    helper_data2=  pd.DataFrame.from_dict(raw1)

    res = merge_table(helper_data1,helper_data2,'id')
    
     # Checks if the output of function is a dataframe
    if not isinstance(res, pd.DataFrame): 
        raise TypeError("The data output is not of type DataFrame")
    # Checks the size of result dataframe generated
    assert res.shape == (10,6)
   