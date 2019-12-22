"""
 Given a sorted array of integer, 
return the two number such that
they would add up to a specific target. You may 
assume that each input would have exactly one
solution, and you may not use the same element 
twice...
"""

A = [-2,1,2,4,7,11,13]
target = 13
#bruth-forch approach 
#time Complexity: O(n^2)
#Space Complexity: O(1)
def two_sum_bruth_force(A,target):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] + A[j]  == target:
                print(A[i],A[j])   
                return True 
    return False
print(two_sum_bruth_force(A,target))
#hash table
# time complexity : O(n)
# Space complexity : O(n)

def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True 
        else:
            ht[target - A[i]] = A[i] 
    return False
print(two_sum_hash_table(A,target))
