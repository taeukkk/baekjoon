def solution(n, left, right):
    rl = int(left/n)
    cl = left%n
    rr = int(right/n)
    cr = right%n
    table = []
    for i in range (rl,rr+1):
        for j in range(0,i+1):
            table.append(i+1)
        for j in range(i+1,n):
            table.append(table[j-1]+1)
    return table[cl:cl+right-left+1]