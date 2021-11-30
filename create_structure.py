import sys
from main import main

print('Arguments: ' + str(sys.argv))

if len(sys.argv) < 3:
    raise Exception("Not enough arguments.")

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
