# Telco Churn Classification Project

## Project Goals:
    - Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.
    - Create modules (acquire.py, prepare.py) that make your process repeateable.
    - Construct a model to predict customer churn using classification techniques.
    - Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using your Jupyter Notebook from above; your presentation should be appropriate for your target audience.
    - Answer panel questions about your code, process, findings and key takeaways, and model.

## Business Goals:
    - To find drivers for customer churn at Teclo. Why are customers churning?
    - Construct a ML classification model that accurately predicts customer churn
    - Document your process well enough to be presented or read like a report

## Audience:
    - Your target audience for your notebook walkthrough is the Codeup Data Science team. This should guide your language and level of explanations in your walkthrough.

## Deliverables:
    - a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation. Your final notebook should be clearly named.
    - a README.md file containing the project description with goals, initial hypotheses, a data dictionary, project planning (lay out your process through the data science pipeline), instructions or an explanation of how someone else can recreate your project and findings (What would someone need to be able to recreate your project on their own?), answers to your hypotheses, key findings, recommendations, and takeaways from your project.
    - a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions should be from your best performing model ran on X_test. Note that the order of the y_pred and y_proba are numpy arrays coming from running the model on X_test. The order of those values will match the order of the rows in X_test, so you can obtain the customer_id from X_test and concatenate these values together into a dataframe to write to CSV.
    - individual modules, .py files, that hold your functions to acquire and prepare your data.
    - a notebook walkthrough presentation with a high-level overview of your project (5 minutes max). You should be prepared to answer follow-up questions about your code, process, tests, model, and findings.

### Initial Hypothesis:
    I believe tenure, contract type, and internet service are the three main drivers of churn. 

Data Dictionary:

Project Planning:

What Next: