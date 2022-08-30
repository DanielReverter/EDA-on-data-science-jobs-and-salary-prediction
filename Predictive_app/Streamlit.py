import streamlit as st
import streamlit.components.v1 as components
from datetime import date
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

st.set_page_config(
     page_title="Salary prediction",
     page_icon="💰",
     layout="wide",
)

year = str(date.today().year)

experience_level = st.selectbox(
     'Experience level:',
     ('Junior', 'Intermediate', 'Senior', 'Executive'))

job_title = st.selectbox(
     'Job title:',
     ("Data Engineer", "Data Scientist", "Data Analyst", "Machine Learning Engineer", "Data Science Manager", 
     "Data Architect", "Research Scientist", "Analytics Engineer", "Machine Learning Scientist", "AI Scientist", 
     "BI Data Analyst", "Big Data Engineer", "Data Science Consultant", "Director of Data Science", 
     "Applied Machine Learning Scientist", "Data Analytics Manager", "Lead Data Engineer", "Computer Vision Engineer",
     "Applied Data Scientist", "Business Data Analyst", "Head of Data", "Data Engineering Manager",
     "Machine Learning Infrastructure Engineer", "Lead Data Scientist", "Machine Learning Developer",
     "Data Analytics Engineer ", "ETL Developer", "Head of Data Science", "other"))

salary_currency = st.selectbox(
     'Salary currency:',
     ("USD", "EUR", "GBP", "INR", "CAD", "other"))

employee_residence = st.selectbox(
     'Employee residence:',
     ("United States", "United Kingdom", "India", "Canada", "Germany", "France", "Spain", "Greece", "Netherlands", "other"))

remote_ratio = st.selectbox(
     'Remote ratio:',
     ("No remote work (less than 20%)", "Partially remote", "Fully remote (more than 80%)"))

company_location = st.selectbox(
     'Company location:',
     ("United States", "United Kingdom", "India", "Canada", "Germany", "France", "Spain", "Greece", "Netherlands", "other"))

company_size = st.selectbox(
     'Company size:',
     ("Less than 50 employees (small)", "50 to 250 employees (medium)", "More than 250 employees (large)"))


experience_rename = {"Junior":"EN", "Intermediate":"MI", "Senior":"SE", "Executive":"EX"}

location_rename = {"United States":"US", "United Kingdom":"GB", "India":"IN", "Canada":"CA", "Germany":"DE", "France":"FR", 
"Spain":"ES", "Greece":"GR", "Netherlands":"NL", "other":"other"}

remote_rename = {"No remote work (less than 20%)":"0", "Partially remote":"50", "Fully remote (more than 80%)":"100"}

size_rename = {"Less than 50 employees (small)":"S", "50 to 250 employees (medium)":"M", "More than 250 employees (large)":"L"}



experience_level = experience_rename[experience_level]

employee_residence = location_rename[employee_residence]

remote_ratio = remote_rename[remote_ratio]

company_location = location_rename[company_location]

company_size = size_rename[company_size]

data = {'work_year': [year], 'experience_level': [experience_level], 'job_title': [job_title],
'salary_currency': [salary_currency], 'employee_residence': [employee_residence], 'remote_ratio': [remote_ratio],
'company_location':[company_location], 'company_size':[company_size]}

df = pd.DataFrame.from_dict(data)

pipeline = pickle.load(open("Predictive_model/pipeline.p","rb"))

df_pipelined = pipeline.transform(df)

tree_reg = pickle.load(open("Predictive_model/tree_regressor.p","rb"))

salary_prediction = tree_reg.predict(df_pipelined)

st.write("The predicted salary is: ", salary_prediction[0])