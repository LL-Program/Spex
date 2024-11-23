import sys
import os
from interpreter import SpexInterpreter

#ARGS
VERSION = "0.0.2"

if len(sys.argv) != 2:
        print(f"Usage: ./spex.exe <path_to_spex_file>")
        sys.exit(1)
spex_file = sys.argv[1]

if not os.path.isfile(spex_file):
        print(f"Error: The file '{spex_file}' does not exist.")
        sys.exit(1)
interpreter = SpexInterpreter()

# try:
with open(spex_file, 'r') as file:
     script = file.read()
     interpreter.executeScript_Main(script=script)
# except Exception as e:
#     print(f"Spe* | FatalSystemError: {e}")
#     sys.exit(1)
