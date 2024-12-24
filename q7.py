n = int(input())
units = list(map(int, input().split(' ')))
 = [0 for i in range(n)]

for i in range(1, n-1):
    if units[i] != -1:
        units[i-1] = i
    else:
        mult[i] = 