from heapq import heappush,heappop,heapify
def solution(A, B):
    answer = 0
    heapify(A)
    heapify(B)
    while B:
        a = heappop(A)
        b = heappop(B)
        if b<=a:
            heappush(A,a)
        else:
            answer+=1
    return answer