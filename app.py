import streamlit as st
import pandas as pd

# importing Datasets
df=pd.read_csv("./Datasets/startup_funding.csv")

# Data cleaning
df["Investors Name"] = df["Investors Name"].fillna("Undisclosed")

# creating necessary variables
startup_name = sorted(df["Startup Name"].unique().tolist())
investor_name = sorted(df["Investors Name"].unique().tolist())

# Front-end layout
st.sidebar.title("Startup Funding Analysis")
option=st.sidebar.selectbox("Select One",["Overall Analysis","Startup","Investor"])

if option=="Overall Analysis":
    st.title("Overall Analysis")
elif option=="Startup":
    st.sidebar.selectbox("Select Startup",startup_name)
    btn1=st.sidebar.button("Find Startup Details")
    st.title("Startup Analysis")
else:
    st.sidebar.selectbox("Select Investor",investor_name)
    btn2=st.sidebar.button("Find Investor Details")
    st.title("Investor Analysis")