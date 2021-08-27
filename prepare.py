from env import host, user, password
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import acquire


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
    
    df = telco_db.drop(columns = 'payment_type_id',inplace = True)
    df = telco_db.drop(columns = 'contract_type_id',inplace = True)
    df = telco_db.drop(columns = 'internet_service_type_id',inplace = True)
    df = telco_db.drop(columns = 'customer_id',inplace = True)
    df = telco_db.drop(columns = 'online_backup',inplace = True)
    df = telco_db.drop(columns = 'device_protection',inplace = True)
    df = telco_db.drop(columns = 'tech_support',inplace = True)
    df = telco_db.drop(columns = 'streaming_tv',inplace = True)
    df = telco_db.drop(columns = 'streaming_movies',inplace = True)
    df = telco_db.replace({'gender':{'Male':0,'Female':1}},inplace = True)
    df = telco_db.replace({'partner':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'dependents':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'phone_service':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'paperless_billing':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.replace({'churn':{'No':0,'Yes':1}},inplace = True)
    df = telco_db.rename(columns = {'gender':'gender_is_female'},inplace = True)
    dummy_df = pd.get_dummies(df[['multiple_lines','online_security','internet_service_type','contract_type','payment_type']], dummy_na=False, drop_first=False)
    df = pd.concat([df, dummy_df], axis=1)
    df = df.drop(columns = ['multiple_lines','online_security','internet_service_type','contract_type','payment_type'])

    return df