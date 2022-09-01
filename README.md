# Data science jobs - comprehensive analysis and salary prediction

## Summary

The objective of this project is simple: to get a better grasp on the current market for data related jobs worldwide. This is done in 2 steps: In the first one, a comprehensive EDA (Exploratory Data Analysis) is performed using multiple visualization tools to help the reader follow along. Pretty much all aspects regarding data related jobs that can be analyzed are (experience level of employee, job title, company location, salary and many more) but the focus of the EDA lies on the job salaries. To further understand the market, some machine learning techniques are used to create a predictive model for those salaries. The predictive model is then deployed online so anyone can use it without having to meddle with the code.

## Data

All data used in this project is gathered from [ai-jobs.net](https://ai-jobs.net/). The purpose of the site is to make global salaries in AI/ML and Big Data a bit more open and transparent. It operates similarly to the well-known website [glassdoor.com](https://glassdoor.com/), as people voluntarily and anonymously post their job details. The two main differences are that ai-jobs only gathers information on data related jobs and that all data gathered is fully available to anyone.

Data can be directly downloaded as a csv file, and can be found in this repository at "Data/data_science_jobs_dataset.csv". Each row of the dataset represents the job details of an individual. The details consist of 11 different variables:

- work_year: The year the salary was paid.
- experience_level: The experience level in the job during the year with the following possible values: 
    - EN: Entry-level/Junior
    - MI: Mid-level/Intermediate
    - SE: Senior-level/Expert
    - EX: Executive-level/Director
- employment_type: The type of employement for the role: 
    - PT: Part-time
    - FT: Full-time
    - CT: Contract
    - FL: Freelance
- job_title: The role worked in during the year.
- salary: The total gross salary amount paid.
- salary_currency: The currency of the salary paid as an ISO 4217 currency code.
- salary_in_usd: The salary in USD (FX rate divided by avg. USD rate for the respective year via [fxdata.foorilla.com](https://fxdata.foorilla.com/)).
- employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
- remote_ratio: The overall amount of work done remotely, possible values are as follows:
    - 0: No remote work (less than 20%)
    - 50: Partially remote
    - 100: Fully remote (more than 80%)
- company_location: The country of the employer's main office or contracting branch as an ISO 3166 country code.
- company_size: The average number of people that worked for the company during the year:
    - S: Less than 50 employees (small)
    - M: 50 to 250 employees (medium)
    - L: More than 250 employees (large)

## EDA

EDA can be divided into two main parts:

### Cleaning

Data is pretty much ready to analyze: There is no missing data and each column values are already standarized. Only 2 things are modified:

- Abreviations are changed to their actual meaning for extra clarity (for example EN --> Junior).
- "salary" and "salary_currency" columns are dropped. "salary_in_usd" is used as the only salary column for better comparisons.

### Analysis

