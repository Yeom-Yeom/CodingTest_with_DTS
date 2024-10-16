import math
def solution(numer1, denom1, numer2, denom2):
    a = numer1*denom2 + numer2*denom1
    b = denom1*denom2
    n = math.gcd(a,b)
    
    if n == 1:
        return [a,b]
    else:
        return [a/n, b/n]
    
print(solution(1,2,3,4))