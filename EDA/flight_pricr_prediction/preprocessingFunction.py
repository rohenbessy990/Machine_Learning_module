import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def impute_nan(data,fill_value,fill_types,columns,dataframe_name):

    print("missing value before removal in",dataframe_name,"data")
    display(data.isnull().sum())

    for column in columns:
        if "random_sample_fill" in fill_types:
            data[column+"_random"]=data[column]
            ##It will have the random sample to fill the na
            random_sample = data[column].dropna().sample(data[column].isnull().sum(),random_state=0,replace=True)
            ##pandas need to have same index in order to merge the dataset
            random_sample.index=data[data[column].isnull()].index
            data.loc[data[column].isnull(),column+'_random']=random_sample
            data[column]=data[column+"_random"]
            data.drop([column+"_random"],axis=1,inplace=True)
        elif "new_feature_fill" in fill_types:
            data[column+"_NAN"]=np.where(data[column].isnull(),1,0)
            data[column].fillna(data[column].median(),inplace=True)
            #fill missing value with median value-----> numerical value
        elif "median_fill" in fill_types:
            data[column].fillna(data[column].median(),inplace=True)
            #fill missing value with mode value-----> categorical value
        elif "mode_fill" in fill_types:
            data[column].fillna(data[column].mode()[0],inplace=True)
            #fill missing value with specific value-----> for categorical value/numerical value
        elif "value_fill" in fill_types:
            data[column].fillna(fill_value,inplace=True)

    print("missing value after removal in",dataframe_name,"data")
    display(data.isnull().sum())                       #display for better output beutification

    return data

