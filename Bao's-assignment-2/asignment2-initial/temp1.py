from functools import reduce
import itertools

arr = [1,2,3,[4,[5,["a",[11,12]]],6],7,[8,9]]




def flatten (lst):
    return reduce(lambda prev, curr: prev + (flatten(curr) if type(curr) is list else [curr]), lst, [])


print(flatten(arr))

# from collections.abc import Iterable


# def flatten(x):
#     if isinstance(x, Iterable):
#         return [a for i in x for a in flatten(i)]
#     else:
#         return [x]

# print(flatten(["A",2,3,[4,5,6],7,[8,9]]))

