# implemented using c950 Webinar 1 as reference (Tepe, 17 Nov. 2020)

# Initialization  ------------------------------------------------------------------------------------------------------

class ChainingHashTable:
    # constructor
    # includes optional initial capacity parameter
    # assigns all buckets with an empty list
    # O(N) linear
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # insert function
    # inserts a new item into the hash table
    # O(1) constant average
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where the package will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # insert at end of list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # search/look-up function
    # searches for a package with matching key in the hash table
    # returns the package if found, or None if not found
    # O(1) constant average
    def search(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]  # value
            return None

    # remove function
    # removes an item with matching key from the hash table
    # O(1) constant average
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
