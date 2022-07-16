#my effort 20%
#acctually almost situation is set but i can't handle it
#and refresh max(priorities) and just checking i==location is too impresive
def solution(priorities, location):
    answer = 0
    while 1:
        m = max(priorities)
        for i in range(len(priorities)):
            if m == priorities[i]:
                answer+=1
                priorities[i]=0
                m =max(priorities)
                
                if i == location:
                    return answer