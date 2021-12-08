arr1 = [2, 7, 11, 15]
target1 = 9

arr2 = [3, 2, 4]
target2 = 6

arr3 = [3,3]
target3 = 6

def two_sum(arr, target):
    hash_table = {}

    for i, elem in enumerate(arr):
        complement = target - arr[i]
        if complement in hash_table:
            return (hash_table[complement], i)
        else:
            hash_table[arr[i]] = i
    

list1 = two_sum(arr1, target1)
print(list1) 

list2 = two_sum(arr2, target2)
print(list2)

list3 = two_sum(arr3, target3)
print(list3)