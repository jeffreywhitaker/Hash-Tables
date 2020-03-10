# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # make an index from the hash
        index = self._hash_mod(key)

        # create link node using key/value
        new_node = LinkedPair(key, value)

        # each index has a link list 
        # travel down that link list

        # set current to that index
        current = self.storage[index]

        # if no link list at index
        if current == None:
            # put the new node there & return
            self.storage[index] = new_node
            return
        
        # set previous to None for looping
        previous = None
        # loop through nodes that exist
        while current != None:
            # if we find a key match
            if current.key == key:
                # overwrite value & return
                current.value = value
                return
            # if no match, continue down list
            previous = current
            current = current.next
        
        #if node not found in list, add it to end
        previous.next = new_node




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # make an index from the hash of the key
        index = self._hash_mod(key)
        # save it as current, make previous
        previous = None
        current = self.storage[index]

        # remove that node
        while current is not None:
            # check if keys match
            if current.key == key:
                # if head of list, set next value
                if previous is None:
                    self.storage[index] = current.next
                # if not head of list, connect nodes
                else:
                    previous.next = current.next
                return
            
            # iterate through by advancing pointers
            previous = current
            current = current.next

        # otherwise, print error
        print("Error, key not found in hashtable")
        return




    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # make an index from hashed key
        index = self._hash_mod(key)

        # make pointer
        current = self.storage[index]

        #iterate through the list
        while current != None:
            # if the keys match
            if current.key == key:
                # return value
                return current.value
            # if no match, increment pointer
            else:
                current = current.next

        #if not found, error and return
        print('Error, key not found in hashtable')
        return



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #make a new table with twice the size
        new_hashtable = HashTable(self.capacity * 2)

        # for each link list
        for i in range(self.capacity):
            # if there is a list at [i]
            if self.storage[i] is not None:
                # for each node in list
                current = self.storage[i]
                while current is not None:
                    # insert key and value
                    new_hashtable.insert(current.key, current.value)
                    # iterate through the list
                    current = current.next
        
        # set old table to new table
        self.capacity = new_hashtable.capacity
        self.storage = new_hashtable.storage

        return



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
