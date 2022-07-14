def solution(A, B):
    #3번 나누어서 생각하기
    #1.A라는 행렬의 행과 B라는 행렬의 렬을 
    #2.이 둘을 zip함수로  묶어주기 열참조시 zip(*B)
    #3.이 두 값의 곱을 더해주기 그리고 이를 2차원 행렬로서 분할해주기
    #for A_row in A
    #for B_col in zip(B*)
    print([[sum (a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A ])
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]