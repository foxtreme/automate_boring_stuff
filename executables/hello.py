#! python3
import sys


def greeting(args):
    """
    Greets depending on given name
    :param args: list of names
    :return: console output
    """
    if len(args) > 1:
        print("Hello {}".format(" ".join(args[1:])))
    else:
        print('Hello world!')


greeting(sys.argv)

# @python E:\Documents\Github Projects\automate_boring_stuff\hello.py %*
# the '@' symbol tells windows to not display this command, only run it
# the '%*' symbols tell windows to forward any command arguments to this program
# the pythonw command will tell window this is a windowless program
