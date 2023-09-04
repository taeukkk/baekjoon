def solution(topping):
    answer = 0
    lt = len(topping)
    cnt = set()
    start = [0]*lt
    end = [0]*lt

    for i in range(lt):
        cnt.add(topping[i])
        start[i] = len(cnt)

    cnt = set()
    for i in range(lt-1,-1,-1):
        cnt.add(topping[i])
        end[i] = len(cnt)

    for i in range(lt-1):
        if start[i] == end[i+1]:
            answer+=1

    return answer