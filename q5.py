def matrix_mul(m1,m2) :  ## it is assumed that m1 is of size (nx3) and m2 of size(3x3) 
    n = len(m1)
    j = 0
    
    result = [[0]*3 for i in range(n)] 
    for i in range(n) :
        j = 0 
        while(j<3) :
            col = j 
            row = i 
            pro = 0 
            for k in range(3) :
                pro += m1[row][k]*(m2[k][col]) 

            result[row][col] = pro 
            j += 1

    return result 



def main() :
    n = int(input("enter the numbber of points : ")) 
    m1 = []
    for i in range(n) :
        x,y = map(int,input().split()) 
        m1.append([x,y,1]) 

    cx = int(input("enter the x scaling factor : ")) 
    cy = int(input("enter the y scaling factor : ")) 
    m2 = [[cx,0,0],[0,cy,0],[0,0,1]] 

    scaled =  matrix_mul(m1,m2) 

    print(scaled) 

main() 
 
