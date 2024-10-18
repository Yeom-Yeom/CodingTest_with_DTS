from math import factorial
def solution(balls, share):
    return factorial(balls) // (factorial(balls-share)*factorial(share))

# import math
# def solution(balls, share):
#   return math.comb(ball, share)