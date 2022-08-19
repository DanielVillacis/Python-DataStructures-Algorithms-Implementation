# LinkedLists will have :

- head node
- tail node
- .next() will connect to the next node
  [head.value]->(next)[value]->(next)[value]->(next)[value]->(next)[tail.value]

# Append a new value to the end of the linked list O(n) :

- O(n) cause we're inserting the new value to the end of the list [tail]
- Once we add our new value, we have to reset the tail position. Cause it is still
  pointing to our previous node.
- In order to set our new tail value, we have to iterate through our linkedlist
  to find the actual tail position and set it to the node appended.

# Inserting or deleting a node at the head of the linked list O(1) :

- O(1) cause we're doing the same number of operations no matter the lenght of the list.
- Update the [Head] position :
  if we added : 1. add the new node
  2.head will be our new item added.
  if we deleted : 1. head will be the successor of the head itemd to be deleted (head.next()). 2. remove the item.

# Inserting an item somewhere in the middle of the list O(n) :

- iterate throught the list starting from the head until we get to the node before we're trying to insert.
- make the new node point to it's successor : newNode.next = tail for example.
- make the previous node (that was pointing to the next node) point to the new node inserted.
- This operation has a O(n) time complexity.

# Removing a node value somewhere in the middle of the list O(n) :

- Iterate throught the list starting from the head until we get to the node before we're trying to remove.
- Set the pointer of the previous node point to the node next to the one to be deleted.
- Remove the desired node.
- This operation has a O(n) time complexity.

# Search for a node value in the list O(n) :

- Compared to the searchByIndex method of the list O(1), searching with an index in a linkedlist is a O(n) operation.
- Iterate throught the list starting from the head until we get to the desired index
