def put_slope(line,start,index,slope):
    put = 0
    for i in index:
        if i in slope:
            return -1
    for l in line:
        if l == start:
            put += 1
    return put

n,l = map(int, input().split())
l-=1
table = [list(map(int, input().split())) for _ in range(n)]
row,col = [],[]

#왼 오 
for i in range(n):
    move=0
    line = [table[i][j] for j in range(len(table))]
    slope = []
    for j in range(n-1):
        if line[j] == line[j+1] +1 :
            if j+1+l<n:
                index = list(range(j+1,j+2+l))
                if put_slope(line[j+2:j+2+l],line[j+1],index,slope) == l:
                    move += 1
                    slope += index
                else:
                    break
            else:
                break
        elif line[j] +1 == line[j+1]:
            if j-l>=0:
                index = list(range(j-l,j+1))
                if put_slope(line[j-l:j],line[j],index,slope) == l:
                    move += 1
                    slope += index
                else:
                    break
            else:
                break
        elif line[j] == line[j+1]:
            move += 1
        else:
            break
    # print("row_slope:",slope)
    if move == n-1:
        row.append(i)
# print("row:",row)

#위 아래 
for i in range(n):
    move = 0
    line = [table[j][i] for j in range(len(table[0]))]
    slope = []
    for j in range(n-1):
        if line[j] == line[j+1] +1 :
            if j+1+l<n:
                index = list(range(j+1,j+2+l))
                if put_slope(line[j+2:j+2+l],line[j+1],index,slope) ==l:
                    move += 1
                    slope += index
                else:
                    break
            else:    
                break
        elif line[j] +1 == line[j+1]:
            if j-l>=0:
                index = list(range(j-l,j+1))
                if put_slope(line[j-l:j],line[j],index,slope) ==l:
                    move+=1
                    slope += index
                else:
                    break

        elif line[j] == line[j+1]:
            move+=1
        else :
            break
    if move==n-1:
        col.append(i)
# print("col:",col)

print(len(row)+len(col))