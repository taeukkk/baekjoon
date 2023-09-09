answer = [0,0]

def merge(area):
    A=len(area)
    zero,one = 0,0
    n,e,w,s = [],[],[],[]
    for i in range(A):
        if i<A/2:
            n.append(area[i][:A//2])
            e.append(area[i][A//2:])
        else:
            s.append(area[i][:A//2])
            w.append(area[i][A//2:])
        for j in range(A):
            if area[i][j]==1:
                one+=1
            elif area[i][j]==0:
                zero+=1

    if zero==0:
        answer[1]+=1
        return
    elif one==0:
        answer[0]+=1
        return
    elif A==2:
        answer[0]+=zero
        answer[1]+=one
        return
    else:
        merge(n)
        merge(e)
        merge(w)
        merge(s)

def solution(arr):
    merge(arr)
    return answer