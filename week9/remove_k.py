def solution(number,k):
    answer = []
    cnt = k
    sp = 0
    
    while cnt!=0 and len(answer)!=len(number)-k:
        max_v = ["-1",-1]
        ep = sp+cnt+1 if sp+cnt+1<=len(number) else len(number)
        for i in range(sp,ep):
            if number[i]=="9":
                max_v[0] = "9"
                max_v[1] = i
                break;
            if number[i]>max_v[0]:
                max_v[0] = number[i]
                max_v[1] = i
        answer.append(number[max_v[1]])
        cnt-=max_v[1]-sp
        sp = max_v[1]+1

    while len(answer)!=len(number)-k:
        answer.append(number[sp])
        sp+=1    
    
    return "".join(answer)