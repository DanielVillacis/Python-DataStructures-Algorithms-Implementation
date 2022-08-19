# GRAPHS BY AN ADJACENCY LIST

{
'A': ['B', 'E'],
'B': ['A', 'C'],
'C': ['B', 'D'],
'D': ['C', 'E'],
'E': ['A', 'D']
}

From a space complexity standpoint, an adjacency list is more efficient. We only store our vertices in the list. In that case our space complexity will be O(|V|+|E|) -> Vertices + Edges.

Add vertex function : O(1)
Add edge function : O(|E|)
Remove vertex function : O(|E|+|V|)
Remove edge function : O()

# GRAPHS BY AN ADJACENCY MATRIX

Adjacency matrices are another way to store graphs. Each vertex will have a True value stored where its its nearby vertices are connected. From a space complexity standpoint, adjacency matrices are not space efficient. We have to iterate through heach vertex eventhough they're probably not connected to the main one. Making our space complexity O(|V|^2)

Add vertex function : O(|V|^2) really bad
Add edge function : O(1)
Remove vertex function : O(|V|^2)
Remove edge function : O()
