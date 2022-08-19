def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print(i,j)

# Our time complexity is O(n) * O(n) = O(n^2) 

print_items(10)


