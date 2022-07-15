#firtst you should map function change from str to int and finlly list
#you should carefully see output type.
#using str funcction + "" space and max,min fuction
#my effort 40%

def solution(s):
    
    arr = list(map(int, s.split()))
    
    return str(min(arr)) + " " + str(max(arr))
