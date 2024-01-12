#Q)1)Using command-line arguments involves the sys module.
# Review the docs for this module and using the information in there write a short program that when run from the command-line reports what operating system platform is being used.

import sys

def report_platform():
    platform = sys.platform
    print(f"Operating System Platform: {platform}")

if __name__ == "__main__":
    report_platform()
