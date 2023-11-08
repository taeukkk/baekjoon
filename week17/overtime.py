import heapq
def solution(n, works):
    answer = 0
    heap = []
    for w in works:
        heapq.heappush(heap,-w)
    while n:
        max_work = heapq.heappop(heap)
        heapq.heappush(heap,max_work+1)
        n-=1
    while heap:
        left = heapq.heappop(heap)
        if left<0:
            answer+=left**2
    return answer