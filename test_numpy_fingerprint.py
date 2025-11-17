import numpy as np
from numpy_fingerprint_match import match

P1 = [
    [1,2,3],
    [2,3,1]
]
T1 = [
    [5,6,7],
    [5,32,1],
    [1,2,3],
    [2,3,1],
    [4,2,1]
]
P2 = [
    [1,0],
    [0,1]
]
T2 = [
    [5,1,0,2],
    [3,1,0,4],
    [8,0,1,9],
    [6,7,2,3]
]
print(match(P2,T2))
assert match(P2,T2) == (1,1)