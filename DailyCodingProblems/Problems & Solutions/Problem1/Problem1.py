#Easy approach  to solve this problem == [*O(n^2)*]. So it is sulg way.
def sum_and_pair(list1, k):
    for i in range(0, len(list1)):
        for j in range(0, len(list1)):
            if k == list1[i] + list1[j]:
                return True, list1[i], list1[j]   
    return False       
nums = [10,15,3,7]
    

k = 15
print(sum_and_pair(nums, k))

# another approach to solve this problem == O(N). This is Sonic HedgeHog
def sum_and_pair(arr, k):
    for i in arr:
        if k>i and (k-i in arr):
            number1 = k-i
            number2 = k-number1
            return True, number1, number2 
    else:
        return False
print(sum_and_pair(nums, k))
