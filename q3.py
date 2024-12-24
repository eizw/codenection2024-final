x, y, k = tuple(map(int, input().split(' ')))

factors = [i for i in range(1,k+1) if k%i==0]
res = 0
l, r = 0, len(factors) - 1
while (l <= r):
    if factors[r] <= max(x, y) and factors[l] <= min(x, y):
        res += ((max(x, y) - factors[r]) + 1) * ((min(x, y) - factors[l]) + 1)
    l += 1
    r -= 1

print(res)