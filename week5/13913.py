n,k = map(int,input().split())

if n>k:
    print(n-k)
    print(" ".join(map(str,[num for num in range(n,k-1,-1)])))
else:
    queue = [n]
    trace = [k]
    prev = [-1] * 100002
    prev[n]=-2
   
    while queue:
        q = queue.pop(0)
        mul = q*2
        pl = q+1
        mi = q-1

        if mul<=k+1 and prev[mul]==-1:
            queue.append(mul)
            prev[mul] = q
        if pl<=k+1 and prev[pl]==-1:
            queue.append(pl)
            prev[pl] = q
        if mi>=0 and prev[mi]==-1:
            queue.append(mi)
            prev[mi] = q

    j = prev[k]
    while j!=-2:
        trace.append(j)
        j = prev[j]

    print(len(trace)-1)
    print(" ".join(map(str,reversed(trace))))