# Merge sort breaks one list in half many times until there's a lot of list of only one item (recursfif)
# A list of only one time is by default sorted.
# Merge is method (a portion) of the sort algorithm.

# Big O : 
# - space complexity : O(n) 
# - time complexity : O(log n) + O(n) = O(n log n) most efficient sort algorithm

# MERGE FUNCTION :
def merge(list1, list2):
    list_combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list_combined.append(list1[i])
            i += 1
        else:
            list_combined.append(list2[j])
            j += 1
    while i < len(list1):
        list_combined.append(list1[i])
        i += 1
    while j < len(list2):
        list_combined.append(list2[j])
        j += 1
    return list_combined


# MERGE SORT ALGORITHM :
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = int(len(my_list) / 2)     # int(len() /2) makes the middle if the list always a full number and not decimal (for odd length lists)
    left = my_list[:mid]            # get the list from index 0 to one before mid (not including mid)
    right = my_list[mid:]           # get the list from mid to the end of the list
    return merge(merge_sort(left),merge_sort(right))


print(merge_sort([3,1,4,2]))
#print(merge([1,2,7,8], [3,4,5,6]))
