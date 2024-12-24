n, m, p = tuple(map(int, input().split(' ')))

items = list(map(int, input().split(' ')))
target = list(map(int, input().split(' ')))

res, curr = 0, target
for i in items:
    if i in curr:
        curr.remove(i)
    if len(curr) == m-p-1:
        res += 1
        curr = target

print(res)