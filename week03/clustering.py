def get_set(l,s):
    only_s,l_and_s = [],[]
    while s:
        temp = s.pop()
        if temp in l:
            l_and_s.append(temp)
            l.remove(temp)
        else:
            only_s.append(temp)
    return [only_s+l+l_and_s, l_and_s]

def solution(str1, str2):
    result = []
    str1 = str1.lower()
    str2 = str2.lower()
    sub1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    sub2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if len(sub1)>len(sub2):
        result = get_set(sub1,sub2) 
    else :
        result = get_set(sub2,sub1)
    if len(result[0])==0:
        return 65536

    return int((len(result[1])/len(result[0]))*65536)