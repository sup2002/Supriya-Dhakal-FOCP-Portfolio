#Q)2)Write a program that, when run from the command line, reports how many arguments were provided.
# (Remember that the program name itself is not an argument).

import sys

def report_argument_count():
    num_arguments = len(sys.argv) - 1  
    print(f"Number of command-line arguments: {num_arguments}")

if __name__ == "__main__":
    report_argument_count()
