def selection_sort(my_list):
    for i in range(len(my_list) - 1): # i = 0
        min_index = i
        for j in range(i+1, len(my_list)): # j = i+1
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]   # basic swap instruction
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

# time complexity of selection sort : 
# worst/average/best ->O(n^2) 
# space complexity -> O(1)

# Test  :
print(selection_sort([4,2,6,5,1,3]))