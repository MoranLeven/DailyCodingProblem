'''Given an array of integers,
return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''

#This solution has O(n) space complexity
def except_index_multiplier(arr):
    n = len(arr)
    left = [0]*n
    right = [0]*n
    product = [0]*n
    left[0]= 1
    right[n-1] = 1
    for i in range(1,n):
        left[i] = arr[i-1] * left[i-1]
    for j in range(n-2,-1,-1):
        right[j] = arr[j+1]*right[j+1]
    for i in range(n):
        product[i] = left[i] * right[i]
    return product
    

arr = [1,2,3,4,5]
print(except_index_multiplier(arr))

#This solution is faster and better O(1) kinda off using only one loop :) --Badass Way-- 
def except_index_multiplier2(arr):
    i, temp = 1,1
    n = len(arr)
    product = [0]*n
    for i in range(n):
        product[i] = temp
        temp= temp * arr[i]
    temp = 1
    for i in range(n - 1, -1, -1): 
        product[i] = product * temp 
        temp *= arr[i] 


    return product
print(except_index_multiplier2(arr))
        
    
    
    




        
        
        
        
