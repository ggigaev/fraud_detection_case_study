import numpy as np
import pandas as pd

def add_bool_name(df):
    '''
    Input: DataFram df
    Output: DataFrame df with boolian column attached
    '''
    length = len(df['org_name'])
    L_flag = []
    for i in range(length):
        flag = len(df['org_name'][i]) == 0
        L_flag.append(flag)

    df['org_name_bool'] = L_flag
    return df
