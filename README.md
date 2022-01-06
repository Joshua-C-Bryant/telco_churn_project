# Telco Churn Classification Project

## Presentation Link: https://www.canva.com/design/DAEl5emTKHk/9gphAP2pKz1uE50jwFFTfw/view?utm_content=DAEl5emTKHk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

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
- Your target audience for your notebook walkthrough is the Codeup DataScience team. This should guide your language and level of explanations inyour walkthrough.

## Deliverables:
- a Jupyter Notebook Report showing process and analysis with the goal offinding drivers for customer churn. This notebook should be commented anddocumented well enough to be read like a report or walked through as apresentation. Your final notebook should be clearly named.
- a README.md file containing the project description with goals, initialhypotheses, a data dictionary, project planning (lay out your process throughthe data science pipeline), instructions or an explanation of how someoneelse can recreate your project and findings (What would someone need to beable to recreate your project on their own?), answers to your hypotheses, keyfindings, recommendations, and takeaways from your project.
- a CSV file with customer_id, probability of churn, and prediction of churn.(1=churn, 0=not_churn). These predictions should be from your best performingmodel ran on X_test. Note that the order of the y_pred and y_proba are numpyarrays coming from running the model on X_test. The order of those valueswill match the order of the rows in X_test, so you can obtain the customer_idfrom X_test and concatenate these values together into a dataframe to writeto CSV.
- individual modules, .py files, that hold your functions to acquire andprepare your data.
- a notebook walkthrough presentation with a high-level overview of yourproject (5 minutes max). You should be prepared to answer follow-up questionsabout your code, process, tests, model, and findings.

### Initial Hypothesis:
I believe tenure, contract type, and internet service are the three maindrivers of churn. 

#### Data Dictionary:

| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| customer_id                | 7043 non-null: object  | Identification number for customer                 |
| gender                     | 7043 non-null: object  | Customer gender, male or female                    |
| senior_citizen             | 7043 non-null: int64   | Yes or No, is the customer a senior citizen        |
| partner                    | 7043 non-null: object  | Yes or No, does the customer customer has a parter |
| dependents                 | 7043 non-null: object  | Number of dependents a customer has                |
| tenure                     | 7043 non-null: int64   | Months a customer has been with the company        |
| phone_service              | 7043 non-null: object  | Phone Service plan, Yes or No                      |
| multiple_lines             | 7043 non-null: object  | Multiple lines, Yes or No                          |
| internet_service_type_id   | 7043 non-null: int64   | 1, 2, 3                                            |
| online_security            | 7043 non-null: object  | Yes, no, or no internet service                    |
| online_backup              | 7043 non-null: object  | Yes, no, or no internet service                    |
| device_protection          | 7043 non-null: object  | Yes, no, or no internet service                    |
| tech_support               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_tv               | 7043 non-null: object  | Yes, no, or no internet service                    |
| streaming_movies           | 7043 non-null: object  | Yes, no, or no internet service                    |
| contract_type_id           | 7043 non-null: int64   | 1, 2, 3                                            |
| paperless_billing          | 7043 non-null: object  | Yes or no, customer uses paperless billing         |
| payment_type_id            | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| monthly_charges            | 7043 non-null: float64 | Monthly charges the customer pays                  |
| total_charges              | 7043 non-null: object  | Total charges the customer has paid                |
| churn                      | 7043 non-null: object  | Yes or no, whether or not the customer has churned |
| contract_type_id.1         | 7043 non-null: int64   | 1, 2, 3                                            |
| contract_type              | 7043 non-null: object  | Month-to-month, One year, Two year                 |
| internet_service_type_id.1 | 7043 non-null: int64   | 1, 2, 3                                            |
| internet_service_type      | 7043 non-null: object  | DSL, Fiber Optic, or None                          |
| payment_type_id.1          | 7043 non-null: int64   | 1, 2, 3, 4                                         |
| payment_type               | 7043 non-null: object  | E-check, mailed check, bank transfer, credit card  |


Project Planning:

What Next:
