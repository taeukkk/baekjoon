n = int(input())
table,result = [],[]
for _ in range(n):
    room = list(map(int,input().split()))
    table.append(room)
table.sort(key = lambda t: (t[1], t[0]))
result.append(table[0])
for i in range(1,n):
    if result[-1][1]<=table[i][0]:
        result.append(table[i])
print(len(result))