import streamlit as st 
import subprocess
import sys 
st.write(sys.version, sys.version_info)
output = subprocess.check_output(["python", "--version"]).decode()
st.write(output)
@st.cache 
def load_dependencies():
    outputs = [
        # subprocess.check_output(["python", "-m", "pip", "install", "pandas"]).decode(),
        subprocess.check_output(["python", "-m", "pip", "install", "matplotlib"]).decode(),
    ]
    return outputs 
    
outputs = load_dependencies()
st.write ( subprocess.check_output(["python", "-m", "pip", "list"]).decode() )
st.write(outputs)

st.write( subprocess.check_output(["python", "-c" ,"import os; print(os.listdir())"]).decode() ) 
st.write( subprocess.check_output("ls").decode() )
st.write( subprocess.check_output(["python", "dep_write.py"]).decode() ) 

with open('file.txt') as f:
    lines = f.readlines()
    st.write(lines)