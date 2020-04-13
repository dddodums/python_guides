# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:51:40 2020

@author: wb305167
"""

import pandas as pd
import numpy as np

# Creates a new dataframe with a list named data and with the field name
# field_name. the rows of the field field_name will be populated by the values
# in the list named data
# usage 
# df = create_dataframe(Country_Codes, 'Country_Code')
#
def create_dataframe(data, field_name):
    df = pd.DataFrame(data, columns = [field_name])   
    return(df)

# Creates a new field with the default values if provided else 
# blanks will be filled
# usage 
# df = gen(df, 'Revenue Shock')
# df = gen(df, 'Revenue Shock', 1.0)
#
def gen(df, field_name, data=None, default_value=None):
    if field_name in df.columns.values:
        print('Field : ', field_name, ' already exists')
    else:
        if default_value is None:        
            field_name_values = ['']*len(df)
        else:
            if data is None:
                field_name_values = [default_value]*len(df)
            else:
                field_name_values = data
        df[field_name] = field_name_values
    return(df)

# replaces the values of the column replace_field_name with replace_value
# in those rows whereever the condition condition_field_name == condition_field_name_value
# is satisfied
# usage 
# df = replace(df, 'Total_Non_Tax_Revenue', 1.0, 'Country_Code', 'ASM')
#
def replace(df, replace_field_name, replace_value, condition_field_name,
            condition_field_name_value):
    df[replace_field_name] = np.where(df[condition_field_name]==condition_field_name_value, replace_value, df[replace_field_name])      
    return(df)

# returns a list of records from a dataframe satisfying certain conditions
# up to three conditions could be used to select
# usage
# list_if(revenue_df, ['year', 'govt_expenditure', 'Total_Revenue_excl_SC'], 'Country_Code', '=', 'IND', 'year', '>=', 2000)
#
def list_if(df, field_name,
            condition_field_name1=None, condition_operator1=None, condition_field_value1=None,
            condition_field_name2=None, condition_operator2=None, condition_field_value2=None,
            condition_field_name3=None, condition_operator3=None, condition_field_value3=None):

    condition_field_name_list = []
    condition_operator_list = []
    condition_field_value_list = []
    if ((condition_field_name1 is not None) and
        (condition_field_name2 is not None) and
        (condition_field_name3 is not None)):
            condition_field_name_list = [condition_field_name1,
                                         condition_field_name2,
                                         condition_field_name3]
            condition_operator_list = [condition_operator1,
                                       condition_operator2,
                                       condition_operator3]
            condition_field_value_list = [condition_field_value1,
                                          condition_field_value2,
                                          condition_field_value3]
    elif ((condition_field_name1 is not None) and
          (condition_field_name2 is not None)):
            condition_field_name_list = [condition_field_name1,
                                         condition_field_name2]
            condition_operator_list = [condition_operator1,
                                       condition_operator2]
            condition_field_value_list = [condition_field_value1,
                                          condition_field_value2]
    elif (condition_field_name1 is not None):
            condition_field_name_list = [condition_field_name1]
            condition_operator_list = [condition_operator1]      
            condition_field_value_list = [condition_field_value1]            
    print('field_name: ', field_name)
    print(condition_field_name_list)
    print(condition_field_value_list)
    length_condition = len(condition_field_name_list)
    if (length_condition==0):
        return(df[field_name])
    else:
        for i in range(length_condition):
            print(condition_field_name_list[i])
            print(condition_field_value_list[i])
            if (condition_operator_list[i]=='='):
                df = df[df[condition_field_name_list[i]]==condition_field_value_list[i]]
            elif (condition_operator_list[i]=='>'):
                df = df[df[condition_field_name_list[i]]>condition_field_value_list[i]]
            elif (condition_operator_list[i]=='>='):
                df = df[df[condition_field_name_list[i]]>=condition_field_value_list[i]]
            elif (condition_operator_list[i]=='<'):
                df = df[df[condition_field_name_list[i]]<condition_field_value_list[i]]
            elif (condition_operator_list[i]=='<='):
                df = df[df[condition_field_name_list[i]]<=condition_field_value_list[i]]               
    #print(df)
    return (df[field_name])

def remove_outliers(df, field_name, lower=None, upper=None):
    if lower is not None:
        df = df[df[field_name]>=lower]
    if upper is not None:
        df = df[df[field_name]<=upper]
    return(df)