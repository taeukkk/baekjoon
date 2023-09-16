def reverse(str):
    result = []
    str = str[1:len(str)-1]
    for i in range(len(str)):
        if str[i]=='(':
            result.append(')')
        else:
            result.append('(')
    return "".join(result)
            
def solution(p):
    answer = ''
    left,right = 0,0
    for i in range(len(p)):    
        if p[i]=='(':
            left+=1
        else:
            right+=1
        if left==right:
            u = p[:i+1]
            if p[0]=='(':
                answer += u +solution(p[i+1:])
            else:
                answer += '('+ solution(p[i+1:]) +')' + reverse(u)
            break;
    return answer