n = int(input())
dic = dict()
for i in range(n):
    curr = list(map(int, input().split(' ')))
    # left, right, bridge
    dic[curr[0]] = (6 if curr[0] == 1 else curr[0]-1, 1 if curr[0] == 6 else curr[0]+1, curr[1])
    dic[curr[1]] = (6 if curr[1] == 1 else curr[1]-1, 1 if curr[1] == 6 else curr[1]+1, curr[10])

dic = dict(sorted(dic.items()))
visited = set()
res = 0
for i in dic:
    if abs(dic[i][3] - i) > n:
        

for i in dic:
    if i in visited:
        visited.remove(i)
    if dic[i] == -1:
        continue
    l, r = i + 1, dic[i]
    if l > r:
        for left in range(l+1, 2*n):
            if l in visited:
                l += 1
                continue

            if l not in dic:
                l += 1
                continue

            if dic[l] > r or dic[l] < l:
                res += 1
                # print(i, l, r, dic, visited)
                # print(l, r, dic)
                # dic[dic[l]] = -1
                visited.add(dic[l])
                # print(i, l, r, dic, visited)
            l += 1
    while l < r:
        if l in visited:
            l += 1
            continue

        if l not in dic:
            l += 1
            continue

        if dic[l] > r or dic[l] < l:
            res += 1
            # print(i, l, r, dic, visited)
            # print(l, r, dic)
            # dic[dic[l]] = -1
            visited.add(dic[l])
            # print(i, l, r, dic, visited)
        l += 1
    # dic[dic[i]] = -1
    # print(i, res)
    dic[i] = -1

print(res)
# for i in dic:
#     print(i)
#     if dic[i] == -1:
#         continue
#     l, r = min(dic[i], i) + 1, max(dic[i], i)
#     while l < r:
#         if dic[l] > r or dic[l] < l:
#             res += 1
#             # print(l, r, dic)
#             # dic[dic[l]] = -1
#             print(l, r, dic)
#         l += 1
#     # dic[dic[i]] = -1
#     dic[dic[i]] = -1

# print(res)