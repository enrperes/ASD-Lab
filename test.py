# --- PYTHON2 ---

# # needed in python2 to allow using "end=..." with print function
# from __future__ import print_function

# def printArray(a):
#     print(a, end = " ")

# def scanArray():
#     # use raw_input() instead of input() for compatibility with python2
#     tokens = raw_input().split(" ")
#     # note the additional "if x" for filtering empty tokens (e.g. due to trailing spaces)
#     return [int(x) for x in tokens if x]


# --- PYTHON3 ---


def printArray(a):
    print(a, end = " ")

def scanArray():
    # raw_input() does not exist anymore in python3, simply use input()
    tokens = input().split(" ")
    # note the additional "if x" for filtering empty tokens (e.g. due to trailing spaces)
    return [int(x) for x in tokens if x]

