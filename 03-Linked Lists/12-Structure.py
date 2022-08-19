# Structure of the node of a linked list :
#   - In python, a node of a linked list is basically a dictionnary.
#   - node will have a "value": value
#   - node will have a "next": none
#
# Illustrated example of a linked list structure :
head = {
        "value": 11,
        "next": {
                "value": 3,
                "next": {
                        "value": 23,
                        "next": {
                                "value": 7,
                                "next": None
                                }
                        }
                }
        }

# This is not quite a linkedlist
print(head['next']['next']['value'])   
# We want our code syntax to run print(myLinkedList.head.next.next.value)