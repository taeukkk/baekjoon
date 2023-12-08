def solution(s):
    answer = 0
    L = len(s)
    for i in range(L):
        start,end=i,L-1
        last = L-1
        cnt = 0
        while start<=end:
            if s[start]==s[end]:
                if start==end:
                    cnt+=1
                else:
                    cnt+=2
                start+=1
                end-=1
            else:
                cnt=0
                if start!=i:
                    start=i
                    end = last-1
                    last -=1
                else:
                    end -=1 
        answer = max(answer,cnt)
    return answer