import numpy as np
from numpy_fingerprint_match import match

P1 = [
    [1,2,3],
    [2,3,1],
    [4,2,1]
]
T1 = [
    [5,6,7,0,0],
    [5,32,1,0,0],
    [1,2,3,0,0],
    [2,3,1,0,0],
    [4,2,1,0,0]
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
def test_if_match():
    print(match(P2,T2))
    print(match(P1,T1))
    assert match(P2,T2) == (1,1)

def test_2():
    assert match(P1,T1) == (2,0)
