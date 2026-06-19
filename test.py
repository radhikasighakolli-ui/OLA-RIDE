import streamlit as st
import pandas as pd

st.title("OLA Dataset Test")

df = pd.read_csv("OLA_Dataset.csv")

st.write("Number of rows:", len(df))
st.write(df.head())