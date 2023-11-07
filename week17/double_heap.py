import bisect
def solution(operations):
    heap = []
    for op in operations:
        command = op.split(" ")
        if command[0]=="I":
            val = int(command[1])
            idx = bisect.bisect_right(heap,val)
            heap = heap[:idx]+[val]+heap[idx:]
        else:
            if command[1]=="1": #max_pop
                if heap:
                    heap.pop()
            else: #min_pop
                if heap:
                    heap.pop(0)
    if not heap:
        return [0,0]
    return [heap[-1],heap[0]]