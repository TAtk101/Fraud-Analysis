# Fraud-Analysis
# Project Overview

This project analyzes a synthetic credit card transaction dataset to identify patterns and risk indicators associated with fraudulent transactions.

The goal was to use SQL, Python, and Power BI to investigate transaction behavior and determine which factors could help prioritize transactions for further fraud review.

Instead of assuming that one variable indicates fraud, this project focuses on analyzing multiple risk indicators together and using the results to support investigation decisions.

# Business Problem

Financial institutions process large volumes of transactions, making it difficult to manually review every transaction for potential fraud.

The objective of this analysis is to answer:

- What percentage of transactions are fraudulent?
- Are fraudulent transactions associated with higher transaction amounts?
- Are foreign transactions associated with higher fraud rates?
- Does a location mismatch indicate increased fraud risk?
- Is lower device trust associated with fraud?
- Does higher transaction velocity indicate increased fraud risk?
- Which factors could be useful for prioritizing transactions for investigation?

# Dataset
Kaggle: Credit Card Fraud Detection Dataset

The dataset contains 10,000 credit card transactions with information about transaction characteristics and whether the transaction was fraudulent.

# Tools Used

MySQL — Data exploration and fraud-rate analysis
Python / Pandas — Data cleaning, analysis, and visualization
Power BI — Dashboard and business-focused data visualization
GitHub — Project documentation 

# SQL Analysis Key Findings
Transaction Amount Analysis:
Fraudulent transactions averaged $216.18 compared with $175.33 for legitimate transactions. The top 50 highest-value transactions had a 12% fraud rate compared with 1.51% overall.

Foreign Transaction:

