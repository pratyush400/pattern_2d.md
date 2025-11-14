def Verify(P,T,i,j):
    for row in range(len(P)):
        for col in range(len(P)):
            if P[row][col] != T[row+i][col+j]:
                return False
    return True

def match(P,T):
    print(f'P: {P} and T: {T}')
    print(f'len of P: {len(P)=}, and T: {len(T)=}')
    fp_P = 0

    for k1 in range(len(P)):
        for k2 in range(len(P)):
            fp_P ^= P[k1][k2]
    for i in range(0, len(T)-len(P)+1):
        fp_n = 0
        for p1 in range(len(P)):
            for p2 in range(len(P)):
                fp_n ^= T[p1+i][p2]
        if fp_n == fp_P and Verify(P,T,i,0):
                print(f'Found it at : {(i,0)} ')  
                return(i , 0)
        for j in range(len(T)-len(P)):
            print(f'here are {i,j+1} ')
            for x in range(0, len(P)):
                    fp_n ^= T[i+x][j] 
                    fp_n ^= T[i +x][ j+len(P)]
            if fp_n == fp_P and  Verify(P,T,i,j+1):  
                print(f'Found it at : {(i,j+1)} ')  
                return(i , j+1)


