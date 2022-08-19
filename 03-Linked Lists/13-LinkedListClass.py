# IMPLEMENTATION OF A SINGLY LINKED LIST - Daniel Villacis
# For every function's time complexity, refer to the 11-LinkedList.md file .
# We create a Node class to avoid creating a new node in each method. 
# Instead we only call a new Node from this class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    # Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # create new Node
        new_node = Node(value)  # Creating the new node

        # add Node to the end
        if self.head is None:   # verifies if our linkedlist is empty, can also use (self.length == 0)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True # optional, but necessary for other methods
    

    def pop(self):
        # First edge cases: we have an empty linked list
        if self.head is None:
            return None
        # Normal pop at the end
        temp = self.head
        pre = self.head
        while (temp.next):      # can also use (while temp.next is not None)
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None   # delete the last node (memory wise)
        self.length -= 1
        # Second edge case: we only have one node (verify after deletion)
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp     # return the last item after deletion
        #return temp.value used for testing


    def prepend(self, value):
        # create new Node
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:    # case where we only have one node left
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        tempIndex = 0
        temp = self.head
        while tempIndex != index:
            temp = temp.next
            tempIndex += 1
        return temp

    def set_value(self, index, value):
        # Ps. This method does not add a new node so we don't deal with pointers.
        temp = self.get(index)      # calls the get method to see if the index is outOfBounds
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:  # adding the value to the beginning
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:  # adding the value to the beginning
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # first step : switch head and tail
        temp = self.head        # set a temp node to [head]
        self.head = self.tail   # set head -> tail
        self.tail = temp        # set tail -> temp which is head
        # variable after temp and before temp
        after = temp.next
        before = None
        # for loop that goes through the length (main reverse logic)
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


#################  MAIN PROGRAM  #################

# Creating a new linkedlist
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

#my_linked_list.insert(1,1)

#print(my_linked_list.remove(2), '\n')

my_linked_list.reverse()

my_linked_list.print_list()



#my_linked_list.prepend(1)
#print('\nafter prepend our linkedlist will be : \n')
#my_linked_list.print_list()

#3 nodes
#print(my_linked_list.pop_first())
#2 node
#print(my_linked_list.pop_first())
#1 node
#print(my_linked_list.pop_first())

#print(my_linked_list.get(3))




