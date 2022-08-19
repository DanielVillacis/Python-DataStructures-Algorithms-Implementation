def insertion_sort(my_list):
    for i in range(1, len(my_list)):    # we start at index = 1
        temp = my_list[i]
        j = i-1     # comparing i to the value before (index = 0)
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

# time complexity of insertion sort : worst case -> O(n^2) 
# best case -> O(n) when almost everything is sorted
# space complexity : O(1)

# Main Program:
print(insertion_sort([2,1,4,3,5,6]))