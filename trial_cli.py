# import sys
# import os
#
# print ('    line 1e to stderr  ', file=sys.stderr)
# sys.stderr.write('    line 2e to stderr  \n') ; sys.stderr.flush()
# os.write(2, b'    line 3e to stderr  \n')

import argparse

def process_input(input_value):
    # Your code to process the input and produce results
    return f"Processed: {input_value}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your program description")
    parser.add_argument("input", help="Input for your program")

    args = parser.parse_args()

    input_value = args.input
    result = process_input(input_value)

    # Print the result to the console
    print(result)
