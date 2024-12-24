n = int(input())
bags = {}
l, r = [], []
for i in range(n):
    curr = list(map(int, input().split(' ')))
    bags[curr[0]] = curr[1]
    if curr[0] > 0:
        r.append(curr[0])
    else:
        l.append(curr[0])

l.sort()
r.sort()
diff = len(r) - len(l)

if diff > 0:
    res = sum([bags[i] for i in l]) + sum([bags[r[i]] for i in range(len(l)+1)])
elif diff < 0:
    res = sum([bags[i] for i in r]) + sum([bags[l[i]] for i in range(len(r)+1)])
else:
    res = sum([bags[i] for i in bags])
    
print(res)

# res = 0
# count = [0, 0]
# for i in bags:
#     if i > 0:
#         count[0]+=1
#     else:
#         count[1]+=1

# if count[0] > count[1]:
#     res += sum([bags[i] for i in bags if i < 0])
# elif count[0] < count[1]:
#     res += sum([bags[i] for i in bags if i > 0])