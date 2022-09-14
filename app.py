import streamlit as st 
import subprocess

output = subprocess.check_output(["python", "--version"]).decode()
st.write(output)
    

with st.spinner("Installing pandas"):
    output = subprocess.check_output(["python", "-m", "pip", "install", "pandas"]).decode()
    st.write(output)
    
import pandas as pd 

st.write(pd.__version__)
