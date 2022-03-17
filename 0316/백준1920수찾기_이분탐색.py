# n = int(input())
# N = list(map(int, input().split()))
# N.sort()
# m = int(input())
# M = list(map(int, input().split()))


from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


# 이분탐색과 재귀함수 사용
def binary(l, N, start, end):
    if start > end: 
        return 0
    mid = (start+end)//2
    if l == N[mid]:
        return 1
    elif l < N[mid]:
        return binary(l, N, start, mid-1)
    else:
        return binary(l, N, mid+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))

