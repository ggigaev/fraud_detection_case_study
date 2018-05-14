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
    X = df2[feature_names].values
    y = df2['fraud_no_fraud'].values
    return (df, y, X)
