import streamlit as st 
import subprocess

output = subprocess.check_output(["python", "--version"]).decode()
st.write(output)

@st.cache 
def load_dependencies():
    with st.spinner("Installing pandas"):
        output = subprocess.check_output(["python", "-m", "pip", "install", "pandas"]).decode()
        output = subprocess.check_output(["python", "-m", "pip", "install", "matplotlib"]).decode()
        st.write(output)
    
load_dependencies()

import pandas as pd 
import matplotlib 
st.write(pd.__version__)
st.write(matplotlib.__version__)

import matplotlib.pyplot as plt 

fig, ax = plt.subplots()
ax.plot(range(10))
st.pyplot(fig)