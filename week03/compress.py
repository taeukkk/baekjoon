from string import ascii_uppercase
def sub_msg(msg,table):
    i = 2
    while True:
        if i > len(msg):
            return [msg[0:],'']
        else:
            temp = msg[0:i]
            if temp not in table:
                return [msg[0:i-1],temp]
            i+=1
def solution(msg):
    answer = []
    table = {}
    alpha = list(ascii_uppercase)
    for i in range(len(alpha)):
        table[alpha[i]] = i+1
    while msg:
        word = sub_msg(msg,table)
        answer.append(table[word[0]])
        table[word[1]] = len(table)+1
        msg = msg[len(word[0]):]

    return answer