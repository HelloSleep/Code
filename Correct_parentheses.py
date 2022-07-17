#Open bracker makes +1 ,Close bracker -1
#compare if conclusion equls 0
#if close bracket more than open bracket while calculating, ==x<0 ,break
# no using stack structure, but simple ans easy
#my effort 10% honestly i approch '(' is open , ')'is close but i couldn't imagine using +-

def solution(s):
    x = 0
    for w in s:
        if x < 0:                
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
