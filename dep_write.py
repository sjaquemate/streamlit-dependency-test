import matplotlib.pyplot as plt 
import streamlit as st 

def main():
    with open("file.txt", "w") as f:
        f.write("hello world!")

if __name__ == '__main__':
    main()