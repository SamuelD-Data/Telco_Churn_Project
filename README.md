# Predicting Churn at Telco

## Background

Telco is making efforts to reduce customer churn because it is more cost efficient to keep current customers than to attract new ones.

## Goals

My goals for this project are as follows
- Create a model that will acurrately predict customer churn using the customer data provided
- Deliver a presentation that summarizes this project

A link to the presentation slides can be found below.

https://docs.google.com/presentation/d/1fI64dzhV6jX33lD-tAv9IEc0MOXx1_ilWL54OKl9aRQ/edit?usp=sharing

## Data Dictionary

Churn: 1 = Customer has churned | 0 = Customer has not churned

Contract_Type_ID: 1 = Month to Month | 2 = One Year | 3 = Two Year

Dependents: 1 = Dependents are on account | 0 = No Dependents on account

Device_Protection: 1 = Has device protection | 0 = Does not have device protection

Female: 1 = Female | 0 = Male

Internet_Service_Type_Id: 1 = DSL | 2 = Fiber Optic | 3 = None

Is_Automatic_Payment: 1 = Customer makes payment via Bank Transfer or Credit Card | 0 = Customer makes payment via Electronic or 
Mailed Check

Monthly_Charges: The amount the customer pays per month for service

Monthly Tenure: How long (months) the client has been a customer.

Multiple_Lines: 1 = Has multiple lines | 0 = Has 1 line or no lines

Online_Backup: 1 = Has online backup | 0 = Does not have online backup

Online_Security: 1 = Has internet security | 0 = Does not have internet security

Paperless_Billing: 1 = Recieves electronic billing | 0 = Receives paper billing

Partner: 1 = Partner on account | 0 = No partner on account

Payment_Type_ID: 1 = Electronic Check | 2 = Mailed Check | 3 = Bank Transfer (Automatic) | 4 = Credit Card (Automatic)

Phone_Service: 1 = Has Phone Service | 0 = No Phone Service

Senior_Citizen: 1 = Senior | 0 = Non-Senior

Streaming_Movies: 1 = Streams movies | 0 = Does not stream movies

Streaming_TV: 1 = Streams TV | 0 = Does not stream TV

Tech_Support: 1 = Has tech support | 0 = Does not have tech support

Tenure: How long (months) the client has been a customer.

Tenure Years: The number of years a customer has done business with us

Total_Charges: The total amount the customer has payed to us in monthly charges

## Initial Thoughts

I can add columns to dimensionalize variables in new ways.
Example: New column "Automatic_Payments", holds 1 for automatic payments and 0 otherwise

When I'm exploring, what will I do if I find that there are many variables that appear to have the same correlation with churn?
Answer: Plot to see if those variables have a stronger correlation with certain subgroups.

## Initial Hypothesis

In my experience, customers with family members on their accounts tend to stay longer. 

H0: monthly tenure of customers with dependents <= monthly tenure of customers without dependents
Ha: monthly tenure of customers with dependents > monthly tenure of customers without dependents

H0: monthly tenure of customers with partners <= monthly tenure of customers without partners
Ha: monthly tenure of customers with partners > monthly tenure of customers without partners

## Project Plan

1) Create acquire.py

acquire data from the telco_churn database on the Codeup data science database server.

2) Create prepare.py

convert object columns with binary values to 0s and 1s
convert object columns with 3 - 4 values to numerical values
address null and/or empty values
address outliers (if any exist)
convert data types as needed
split into train, validate, test

3) Explore

plot heatmap to find strong correlations between churn and all other variables
test each reasonable hypothesis
use exploration to identify variables with the strongest correlation to churn

3) Model

create a baseline model
create models using the strongest driver variables identified in exploration
when modeling, discern which features are having the biggest impact
fit to train and evaluate on train
select all models that outperform the baseline
select best model from validate and apply to test dataset

4) conclusion

summarize findings from project:
drivers, recommendations, model performance
next steps
expectations for model performance on future unseen data

## How to Reproduce

Install acquire.py, prepare.py into your working directory. (You must have access to Codeup data science database)

Run the jupyter notebook.

# Conclusion
I'll now summarize what I learned from exploration and modeling, make recommendations, discuss what to do next, and summarize the model.
***
- Exploration uncovered that some the following features are related to churn:
    - Dependents
    - Partners
    - Automatic vs Manual Payments
    - Monthly Charges
    
- Recommendations to reduce churn:
    - Lower monthly charges because our customers appear to be price sensitive
    - Offer promotions that encourage clients to add partners and dependents to account. Once signed up, switching multiple people to a competitor becomes a barrier to exit and increases tenure.
    - Invest in marketing that promotes the use of automatic payments because clients will leave Telco for a competitor if they don't feel Telco's services meet their convenience needs.

- Created a model that uses these variables to make predictions about churn.
    - The model maintained an accuracy of roughly 74% on both in and out-of-sample data
    - I expect it to perform with similar accuracy on more unseen data in the future
    
- In the near future I would like to use what I learned from this project to build a new, more refined model that will improve it's ability to predict when a customer is churning, when they actually are (ie. improved recall) as this is the current model's largest area of opportunity.