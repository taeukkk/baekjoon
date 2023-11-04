import re
def solution(skill, skill_trees):
    answer = 0
    pattern = ""
    for s in skill:
        pattern += s+","
    pattern = "[^"+pattern[:len(pattern)-1]+"]"

    for st in skill_trees:
        st = re.sub(pattern,"",st)
        if st == skill[:len(st)]:
            answer+=1

    return answer