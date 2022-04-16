n = int(input())
arr = set(map(int, input().split()))
m = int(input())
qry = list(map(int, input().split()))

# set 자료구조 -> 해쉬 set
# 특정 원소를 O(1)에 찾음

for x in qry:
    if x in arr:
        print(1)
    else:
        print(0)
