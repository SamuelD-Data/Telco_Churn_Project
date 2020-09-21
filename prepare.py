# importing
import pandas as pd
from sklearn.model_selection import train_test_split

# creating function to prep data for analysis
def prepare_telco(telco_raw):
    # dropping duplicate rows
    telco_raw.drop_duplicates(inplace=True)
    # naming columns to have yes and no replaced with 0s and 1s
    cols = ["gender","partner","dependents","phone_service", "paperless_billing","churn"]
    telco_raw[cols] = telco_raw[cols].replace('Yes', 1)
    telco_raw[cols] = telco_raw[cols].replace('No', 0)
    # creating dummy df of all categorical columns with 3 unique values
    dummy_df = pd.get_dummies(telco_raw[['multiple_lines','online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']])
    # adding dummy columns to original DF
    telco_raw = pd.concat([telco_raw, dummy_df], axis = 1)
    # naming columns that hold data dummy columns were made from
    cols_to_drop = ['multiple_lines','online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
    # dropping columns that holds data dummy columns were made from
    telco_raw = telco_raw.drop(columns = cols_to_drop)
    # renaming tenure to monthly tenure so users can see what unit of measure is used
    telco_raw.rename(columns={'tenure':'monthly_tenure'}, inplace=True)
    # no missing values but there are values with only whitespace in total_charges
    # these are white spaces because their tenure is 0 so they havent been with us a full month, thus they havent been billed so they
    # have $0 in total charges.
    # replacing blank space with value of 0
    telco_raw['total_charges'] = telco_raw.total_charges.where((telco_raw.monthly_tenure != 0),0)
    # converting data type to float since we couldnt when there were white space values
    telco_raw['total_charges'] = telco_raw.total_charges.astype(float)
    # creating tenure_years column that shows how many years client has been with us
    telco_raw['tenure_years'] = round(telco_raw.monthly_tenure / 12, 1)
    # splitting data into train, test and validate DFs
    train_validate, test = train_test_split(telco_raw, test_size = .20, random_state = 123)
    train, validate = train_test_split(train_validate, test_size = .30, random_state = 123)
    # returning DFs
    return train, validate, test
