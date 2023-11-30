"""
TASK A
This file contains the hashtable class and the lookup and store functions
sourced partly from zybooks

A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time


B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time
"""
class HashTable:
    """
    we have 40 packages so the default capacity of the hashtable is 40
    we are using an array to abstract the hashtable functionality
    I will implement a built-in hashing function in order to handle collisions.
    """
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    # Task A Insertion function
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)  # sorting keys into buckets
        bucket_arr = self.table[bucket]  # getting a list of all keys from the bucket that matches the key parameter
        # search bucket, if key param is already in bucket then just update
        for itemPair in bucket_arr:
            if itemPair[0] == key:
                itemPair[1] = value # bucket_arr = [[key, values],[key, values]...]
                return True
        # else add to self.table[bucket] list (return true on line 54 eliminates need for if else)
        key_value = [key, value]
        bucket_arr.append(key_value)
        return True

    # Searches the hash table for an item with the matching key
    # Will return the item if founcd, or None if not found
    # Task B look up function
    def look_up(self, key):
        bucket = hash(key) % len(self.table)
        bucket_arr = self.table[bucket]  # same code as before to get bucket list
        for itemPair in bucket_arr:  # find item in bucket list by key
            # print(key_value)
            if itemPair[0] == key:
                return itemPair[1]  # bucket_arr = [[key, values],[key, values]...]
        print("Could Not Find Item")  # could put error handling here if needed
        return False

    # Removal function that will delete a key from the hash table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_arr = self.table[bucket]  # get bucket list with appropriate key hash
        # removes the item if it is present
        if key in bucket_arr:  # python functionality for searching an array
            bucket_arr.remove(key)