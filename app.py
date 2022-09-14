import streamlit as st 
import subprocess

output = subprocess.check_output(["python", "--version"]).decode()
st.write(output)
    
with st.spinner("Installing pandas"):
    output = subprocess.check_output(["python", "-m", "pip", "install", "pandas"]).decode()
    # output = subprocess.check_output(["python", "-m", "pip", "install", "pandas"]).decode()
    st.write(output)
    
import pandas as pd 
import matplotlib.pyplot as plt 

st.write(pd.__version__)
fig, ax = plt.subplots()
ax.plot(range(10))
st.pyplot(fig)