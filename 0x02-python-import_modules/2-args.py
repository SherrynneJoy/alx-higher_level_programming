#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_args = len(sys.argv) - 1
    if no_args == 0:
        print("0 arguments.")
    elif no_args == 1:
        i = 1
        print("1 argument: ")
        print("{}: {}".format(i, sys.argv[i]))
    else:
        print("{} arguments: ".format(no_args))
        for i in range(no_args):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
