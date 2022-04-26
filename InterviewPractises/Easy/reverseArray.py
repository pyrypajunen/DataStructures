"""
The problem is that we want to reverse a T[] array 
in O(N) linear time complexity and we want the algorithm 
to be in-place as well - so no additional memory can be used!
"""

def reserveList(T):
    start = 0
    end = len(T) - 1
    
    while start < end:
        T[start], T[end] = T[end], T[start]
        start += 1
        end -= 1
    return T

T = [1,2,3,4,5]


print(reserveList(T))