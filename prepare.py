from env import host, user, password
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


def prep_telco(df):
    # removing the rows with empty values in total_charges
    df.drop(df[df['total_charges'].str.contains(" ")].index, inplace = True)
    # turn total_charges into float instead of object
    df.total_charges = df.total_charges.astype(float)
    # drop columns I felt were unnecessary
    df.drop(columns = ['payment_type_id','contract_type_id','internet_service_type_id','customer_id','online_backup','device_protection','tech_support','streaming_tv','streaming_movies'], inplace = True)
    # encode values
    for column in df.columns:
        if df[column].dtype == np.number:
            continue
        df[column] = LabelEncoder().fit_transform(df[column])
    target = 'churn'
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=123, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=123,
                                       stratify=train_validate[target])
    return train, validate, test

