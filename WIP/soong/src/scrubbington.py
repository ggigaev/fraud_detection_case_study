import numpy as np
import pandas as pd



#####################################################################
#  Step 1: create 'fraud_no_fraud'
#####################################################################
def scrub_fraud_no_fraud(df):
    '''
        Input : pass in a dataframe
        Output: returns a series of Booleans based on 'acct_type'
    '''
    df['fraud_no_fraud'] = df['acct_type'].astype(str).str[:5] == 'fraud'
    return df['fraud_no_fraud']



#####################################################################
#  Step 2: update time based columns to datetime
#####################################################################
def scrub_datetime(df):
    '''
        Input : pass in a dataframe
        Output: returns a new dataframe with updated datetime
    '''
    df['approx_payout_date']=df['approx_payout_date'].astype("datetime64[s]")
    df['event_created']=df['event_created'].astype("datetime64[s]")
    df['event_end']=df['event_end'].astype("datetime64[s]")
    df['event_published']=df['event_published'].astype("datetime64[s]")
    df['event_start']=df['event_start'].astype("datetime64[s]")
    df['user_created']=df['user_created'].astype("datetime64[s]")
    return df

#####################################################################
#  Step 3: Create column for events with no organization name
#####################################################################

def add_bool_name(df):
    '''
    Input: DataFram df
    Output: DataFrame df with boolean column attached
    '''
    length = len(df['org_name'])
    L_flag = []
    for i in range(length):
        flag = len(df['org_name'][i]) == 0
        L_flag.append(flag)

    df['org_name_bool'] = L_flag

    return df



#####################################################################
#  SCRUB EVERYTHING
#####################################################################
def scrub_everything(df, feature_names):
    '''
        Input : pass in a dataframe, and a list of wanted feature names
        Output: tuple of 3 items
            1. returns a new dataframe with all scrubbing steps done
            2. returns 'y' --> target column
            3. returns 'X' --> Feature Matrix
    '''
    df['fraud_no_fraud'] = scrub_fraud_no_fraud(df)
    df2 = scrub_datetime(df)
    df3 = add_bool_name(df2)
    X = df3[feature_names].values
    y = df3['fraud_no_fraud'].values
    return (df, y, X)
