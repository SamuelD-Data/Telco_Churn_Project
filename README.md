### Identifying the Drivers of Churn at Telco

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

## Thoughts

## Initial Hypothesis

## Project Plan

1) Create acquire.py

acquire data from the telco_churn database on the Codeup data science database server.

2) Create prepare.py

convert object columns with binary values to 0s and 1s
convert object columns with 3 - 4 values to numerical
address outliers
split into train, validate, test

3) Explore

plot correlation matrix of all variables
test each hypothesis
are there cutoffs I should use to label each continuous feature as increased risk? Plot the continuous variables using a swarmplot or boxplot with death_event, and also observe the outcomes of the t-tests.

3) Model

try different algorithms: decision tree, logistic regression, random forest, knn, svm
which features are most influential?
evaluate on train
select top 3 +/- models to evaluate on validate
select top model
create a model.py that pulls all the parts together.
run model on test to verify.

4) conclusion

summarize findings
make recommendations
next steps
how to run with new data.

## How to Reproduce

Install acquire.py, prepare.py and model.py into your working directory. (You must have access to Codeup data science database)

Run the jupyter notebook.