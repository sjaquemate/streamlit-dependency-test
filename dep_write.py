import sys
import traceback

def main():
    try:
        import matplotlib.pyplot as plt 
        import streamlit as st 
        with open("file.txt", "w") as f:
            f.write("hello world!")

    except Exception:
        print(traceback.format_exc())
    
if __name__ == '__main__':
    main()