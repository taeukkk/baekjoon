def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        cut_s = []
        for j in range(0,len(s),i):
            cut_s.append(s[j:j+i])

        prev_s = 0
        next_s = 1
        result = cut_s[prev_s]
        while next_s!=len(cut_s):
            p = cut_s[prev_s]
            n = cut_s[next_s]
            if p!=n:
                if next_s-prev_s>1:
                    result += str(next_s-prev_s)
                    prev_s = next_s-1
                result += n
                prev_s+=1
                next_s+=1
            else:
                next_s+=1
        if next_s-prev_s>1:
            result += str(next_s-prev_s)
        answer = min(answer,len(result))
    return answer