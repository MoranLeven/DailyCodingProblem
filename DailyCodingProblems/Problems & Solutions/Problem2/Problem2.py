#This solution has O(n) space complexity
arr = [1,2,3,4,5]


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

print(except_index_multiplier(arr))

#This solution is faster and better O(1) kinda off using only one loop :) --Badass Way-- 
def except_index_multiplier2(arr):
    if len(arr) == 1:
        print(0)
        return
    
    i, temp = 1, 1
    n = len(arr) 
    product = [0]*n #allocating memory for array
    #product = [0 for i in range(n)] == another way to allocate memory to array 

    for i in range(n):
        product[i] = temp
        temp *= arr[i]

    temp = 1

    for i in range(n-1,-1,-1): 
        product[i]*= temp 
        temp = temp * arr[i]
        
    return product


print(except_index_multiplier2(arr))
