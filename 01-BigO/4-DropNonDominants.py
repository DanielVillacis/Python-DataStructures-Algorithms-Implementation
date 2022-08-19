def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            print(i,j)

    for k in range(n):
        print(k)

# Time complexity is O(n^2) + O(n) = O(n^2)

print_items(10)