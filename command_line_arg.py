'''
@author : Abhishek R S
'''

import sys

# parse and return dictionary of command-line args
def get_args(argv):
    options = {}
    
    while(argv):
        if argv[0][0] == '-':
            options[argv[0]] = argv[1]
        argv = argv[1:]

    return options

def main():
    myargs = get_args(sys.argv)

    if not(myargs):
        # no command-line args
        print("No command line args given")
    else:
        print(myargs)
        print("")

if __name__ == '__main__':
    main()
