import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        min_hot = heapq.heappop(scoville)
        if min_hot >= K:
            return answer
        next_hot = heapq.heappop(scoville)
        heapq.heappush(scoville,min_hot + next_hot*2)
        answer += 1
    if heapq.heappop(scoville) < K :
        return -1
    return answer