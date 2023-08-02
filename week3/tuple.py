def str_to_list(str):
    str = str[1:len(str)-1]
    str_list = str.split('},')
    result = []
    for i in range(len(str_list)):
        str_list[i] = str_list[i].replace('{',"")
        str_list[i] = str_list[i].replace('}',"")
        str_list[i] = str_list[i].replace(','," ")
        str_to_int = str_list[i].split(" ")
        temp=[]
        for i in str_to_int:
            temp.append(int(i))
        result.append(temp)
    return result
def solution(s):
    str = str_to_list(s)
    table = {}
    for s in str:
        table[len(s)] = s
    answer = []
    for i in range(len(table)):
        temp = table[i+1]
        for j in temp:
            if j not in answer:
                answer.append(j)
    return answer