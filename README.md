### Identifying the Drivers of Churn at Telco

## Background

We are making efforts to reduce customer churn because it is more cost efficient to keep our current customers than to attract new ones.

## Goals

My goal for this project is to create a model that will acurrately predict customer churn using the customer data provided. I will also be identifying the primary drivers of customer churn.

I will deliver the following: 

- classification_project.ipynb
    - A Jupyter Notebook showing the process and analysis by which the drivers of customer churn are documented.
    
- README.md
    - A Markdown file containing the project description with goals, a data dictionary, project planning, instructions for recreaction of the project and its findings, key findings and takeaways. 
    
- predictions.csv
    - A CSV file containing customer IDs, probability of churn, and prediction of churn (1 = Churn, 0 = not_churn)

- acquire.py
    - A Python file containing a function to acquire the customer data
    
- prepare.py
    - A Python file containing functions that prepare the customer data to be worked with

- model.py
    - A Python file containing the functions needed to recreate the model 
    
- A walkthrough-style presentation with a high-level overview of the project

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

## Key Findings and Takeaways

- Exploration uncovered that some of the strongest drivers of churn include:
    - Dependents
    - Partners
    - Automatic vs Manual Payments
    - Monthly Charges
    
- All of this information suggest that our most reliable customers are price sensitive, people with families who greatly value the convenience of automatic payments.

- Recommendations to reduce churn:
    - Lower monthly charges because our customers appear to be price sensitive
    - Offer promotions that encourage clients to add partners and dependents to account. Once signed up, switching multiple people to a competitor becomes a barrier to exit and increases tenure.
    - Invest in marketing that promotes the use of automatic payments because our clients will leave us for our competitors if they don't feel our services meet their convenience needs.

- We created a model that identifies these variables and uses logistic regression to make predictions about churn.
    - The model maintained an accuracy of roughly 74% on both in and out of sample data
    - We expect it to perform with same accuracy on more unseen data in the future
    - If our churn rate increases in the future, the model will become less accurate as it's recall metric is low so it tends to predict incorrectly when a customer churns.
    
- In the near future I would like to use what we learned from this project to build a new, more refined model that will improve it's ability to predict when a customer is churning, when they actually are (ie. improved recall) as this is our current model's largest area of opportunity.