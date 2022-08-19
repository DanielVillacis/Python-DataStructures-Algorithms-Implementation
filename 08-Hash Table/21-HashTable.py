class HashTable:
    def __init__(self, size=7): # 7 will be our default size in case none is passed in argument
        self.data_map = [None] * size

    # Hash method
    def __hash(self, key): 
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)     # ord() gets the ASCII number for each letter as we're looping through it
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)                    # hash method will return the address where we will store our new key
        if self.data_map[index] == None:
            self.data_map[index] = []               # set an empty list at the index if it's not created
        self.data_map[index].append([key, value])   # appends the key and value to the index

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):      # we only iterate through the index list
                if self.data_map[index][i][0]== key:        # i : different list in the same address, 0: first element of the list key-value -> key
                    return self.data_map[index][i][1]       # returning the value (1) of the key
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys



#########  MAIN PROGRAM FOR THE CLASS (USE FOR TESTING)  ######### 
my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

#print(my_hash_table.get_item('bolts'))
#print(my_hash_table.get_item('washers'))
#print(my_hash_table.get_item('nail'))

#print(my_hash_table.keys())

#my_hash_table.print_table()




#### VERY COMMMON INTERVIEW QUESTION ####
# LIST1 = [1,3,5]
# LIST2 = [2,4,5]
# Q: Check if the two list have and item in common
# the interviewer will want to see the second approach

# First approach : create nested for loops -> O(n^2)
def item_in_common(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
    return False

list1 = [1,3,5,10,12,32,346,56,30]
list2 = [2,4,7,9,11,41,26,5]
#print(item_in_common(list1, list2))


# Second approach : use a HashTable (dictionnary) and loop through the first list and put it in the dictionnary
# {1: True, 2: True, 5: True}
# look through the dictionnary of list2 O(1)
def item_in_common_hashTable(list1, list2):
    my_dict = {}        # dictionnary
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False

list3 = [1,3,5,10,12,32,346,56,30]
list4 = [2,4,7,9,11,41,26,6]
print(item_in_common_hashTable(list3, list4))



    
