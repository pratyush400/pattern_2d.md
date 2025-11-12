
def match(P, T):
    for i in range(0, len(T)-len(P)+1):
        for j in range(0, len(T)-len(P)+1):
            match = True
            for x in range(0, len(P)):
                for y in range(0, len(P)):
                    if P[x][y] != T[i+x][j+y]:
                        match = False   
                        break
            if match: 
                return (i,j)             
            
                            

            
