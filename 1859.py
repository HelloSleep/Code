import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    things = int(input())
    object = list(map(int,(input().split())))
    max_val =object[-1]
    money=0
    for k in range(things-1 , -1 ,-1):
        if object[k] >= max_val:
            max_val = object[k]
        money += max_val - object[k]
        
    print(f"#{test_case} {money}")
