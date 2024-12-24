n, x = map(int, input().split())
total = 0
count = 0

for i in range(1, n + 1):
    total += i
    count += 1
    if total >= x:
        print(count)
        break
else:
    for i in range(n - 1, 0, -1):
        total += i
        count += 1
        if total >= x:
            print(count)
            break
    else:
        print(count)