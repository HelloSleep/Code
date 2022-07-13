import sys
from collections import Counter
sys.stdin = open("input.txt", "r")


T= int(input())

for test_case in (1,T+1):
    case= int(input())
    price =list(map(int, input().split()))
    cprice = Counter(price)
    print(f"#{test_case} {cprice.most_common(1)[0][0]}")
    


