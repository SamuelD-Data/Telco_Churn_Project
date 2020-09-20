import pandas as pd

def prepare_telco(x):
    x.drop_duplicates(inplace=True)
    cols = ["gender","partner","dependents","phone_service", "paperless_billing","churn"]
    x[cols] = x[cols].replace('Yes', 1)
    x[cols] = x[cols].replace('No', 0)
    dummy_df = pd.get_dummies(x[['multiple_lines','online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']])
    x = pd.concat([x, dummy_df], axis=1)
    cols_to_drop = ['multiple_lines','online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies']
    x = x.drop(columns = cols_to_drop)
    x.rename(columns={'tenure':'monthly_tenure'}, inplace=True)
    x['total_charges'] = x.total_charges.where((x.monthly_tenure != 0),0)
    x['total_charges'] = x.total_charges.astype(float)
    
    X = dfp.drop(['churn'], axis = 1)
    y = dfp[['churn']]
    X_train_validate, X_test, y_train_validate, y_test = train_test_split(X, y, test_size = .20, random_state = 123)
    X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate, test_size = .30, random_state = 123)
