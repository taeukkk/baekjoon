import math
def solution(w,h):
    div = math.gcd(w,h)
    return w*h-(w//div+h//div-1)*div