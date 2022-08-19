def print_items(n):
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            for k in range(n):
                print(i,j,k)

# Our time complexity is O(n) * O(n) * O(n) = O(n^3). After simplifications -> O(n^2)
# From a time complexity perspective, a quadratic time complexity is not efficient.

print_items(10)