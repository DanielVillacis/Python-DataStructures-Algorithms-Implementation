def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]      # move the next value to the previous one (swap)
                my_list[j+1] = temp
    return my_list

# time complexity of bubble sort : O(n^2) worst case and O(n) on best case
# space complexity : O(1)


my_list = [4,2,6,5,1,3]
my_list_sorted = bubble_sort(my_list)
print(my_list_sorted)
