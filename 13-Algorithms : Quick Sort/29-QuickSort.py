# Swap function
def swap(my_list, index1, index2):      # Funtion to swap indexes in our list
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# Pivot function : will sort a little and return the index in the middle of the list O(n)
def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

# QuickSort algorithm (recursive)
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)   # O(n)
        quick_sort_helper(my_list, left, pivot_index - 1)   # O(log n)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

# Main quicksort:
def quick_sort(my_list):    # O(n log n) just like merge sort in best and average case
    return quick_sort_helper(my_list, 0, len(my_list) - 1)



# worst case : when we already have sorted data -> O(n^2)
#my_list = [4,6,1,7,3,2,5]


#print(pivot(my_list, 0, 6))
print(quick_sort([4,6,1,7,3,2,5]))