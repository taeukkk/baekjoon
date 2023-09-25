from math import gcd
def solution(arrayA,arrayB):
    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for A in arrayA:
        gcdA = gcd(gcdA,A)
    for B in arrayB:
        if B%gcdA==0:
            gcdA = 0
            break

    for B in arrayB:
        gcdB = gcd(gcdB,B)
    for A in arrayA:
        if A%gcdB==0:
            gcdB = 0
            break
        
    return max(gcdA,gcdB)   