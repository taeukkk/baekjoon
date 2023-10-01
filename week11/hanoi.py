num = {
    1: "n",
    2: "w",
    3: "h",
    "n": '1',
    "w": '2',
    "h": '3'
}
def redirect(start,mid,end,list):
    list = list.replace('1',num[start]).replace('2',num[mid]).replace('3',num[end])
    list = list.replace('n',num['n']).replace('w',num['w']).replace('h',num['h'])
    return list

def solution(n):
    answer = []
    dp = ["-"]*16
    dp[2] = "1,2/1,3/2,3"
    for i in range(3,n+1):
        dp[i] = redirect(1,3,2,dp[i-1])+"/1,3/"+redirect(2,1,3,dp[i-1])
    for pair in dp[n].split("/"):
        p = pair.split(",")
        answer.append([int(p[0]),int(p[1])])
    return answer