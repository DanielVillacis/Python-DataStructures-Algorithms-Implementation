def print_items(n):
    for i in range(n):  # O(n)
        print(i)

    for j in range(n):  # O(n)
        print(j)

# Since we drop constants from the equation, we can see that
# our total runtime is O(n) + O(n) = O(2n) = O(n)

print_items(10)

