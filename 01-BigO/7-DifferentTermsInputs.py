def print_items(a,b):
    for i in range(a):  # O(a)
        print(i)
    
    for j in range(b):  # O(b)
        print(j)

# Total time complexity : O(a) + O(b) = O(a+b)

print_items(2,4)