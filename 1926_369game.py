#Not complited
from traceback import print_tb


T=int(input())
case=['3','6','9']
for test_case in range(1, T + 1):
    li=[]
    s= str(test_case)
    for i in s:
        li.append(i)

    for k in li:
        if k in case:
            print("-")
        else:
            print(int(li))
    
        #print()
    #print(li)
    
    
    

    
    
        
    
            
