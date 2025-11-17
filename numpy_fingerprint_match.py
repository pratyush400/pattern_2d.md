import numpy as np

def Verify(P,T,i,j):
    return np.array_equal(T[i : i + len(P), j:j+len(P)],P)

def match(P,T):
    fp_P = 0
    np_P = np.array(P)
    np_T = np.array(T)
    fp_P = np.bitwise_xor.reduce(np_P, axis=None)
    for i in range(0, len(np_T)-len(np_P)+1):
        fp_n = 0
        block = np_T[i:i+ len(np_P), 0:len(np_P)]
        fp_n = np.bitwise_xor.reduce(block, axis=None)
        if fp_n == fp_P and Verify(np_P,np_T,i,0):
                return(i , 0)
        for j in range(len(np_T)-len(np_P)):
            # print(np_T[i:i+len(np_P), 0:len(np_P)])
            block2 = np_T[i:i + len(np_P), j]
            block3 = np_T[i:i + len(np_P), j + len(np_P)]
            fp_n ^= np.bitwise_xor.reduce(block2)
            fp_n ^= np.bitwise_xor.reduce(block3)
            if fp_n == fp_P and  Verify(np_P,np_T,i,j+1):  
                return(i , j+1)


