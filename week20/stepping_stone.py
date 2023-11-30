from heapq import heappush,heappop,heapify
def solution(stones, k):
    window = []
    for i in range(k):
        heappush(window,(-stones[i],i))
    answer = -window[0][0]
    for i in range(k,len(stones)):
        heappush(window,(-stones[i],i))
        while window[0][1]<i-k+1:
            heappop(window)
        answer = min(answer,-window[0][0])
    return answer
