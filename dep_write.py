import sys
import traceback

def main():
    try:
        import matplotlib
        import matplotlib.pyplot as plt 
        with open("file.txt", "w") as f:
            f.write(f"hello world! {matplotlib.__version__}")

    except Exception:
        print(traceback.format_exc())
    
if __name__ == '__main__':
    main()