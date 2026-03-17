#  Taner Bulbul
#  MSML 606 - Data Structures and Algorithms
#  Bonus Project: N-gram Analysis with Hash Tables
#  external source policy included before each code section as comments


# external‑source policy:
# Used my own code and logic to build the hashmap ADT class
# This is the hash table code mostly from HW3
# with some small chnages and improvements

# Hash table with open addressing and linear probing
# imported from the application code

from sympy import nextprime

class HashMap:
    #  declare a special value constant to use in the deleted slots
    #  It means the slot is available for insertion and allows the search to 
    #  continue (if we set it to None after deletion, it would stop he search) 
    _TOMBSTONE = object()
    # hash table will store 1-Ngrams as keys and their metadata
    # which are match count and vlume count for all years
    
    def __init__(self, size=1009):
        self.size_m = size  # size of the table, should be a prime number
        self.table = [None] * self.size_m  # hash table, storage for key-value pairs
        self.n = 0  # count of elements stored in the hash table
        self.total_insert_probes = 0  # total probes for insertions
        self.total_search_probes = 0  # total probes for searches
        self.search_count = 0  # number of searches

    # Find a value associated with the key
    # and return the key or None if not found
    def search(self, key):
        # apply the hash function
        idx = self._hash(key)
        start_idx = idx  # check if I reached my index after probing
        probes = 1  # count probes for search
        self.search_count += 1  # increment search count
        while self.table[idx] is not None:
            # if the slot is not a tombstone and the key matches, return the value
            if self.table[idx][0] is not self._TOMBSTONE:
                if self.table[idx][0] == key:
                    self.total_search_probes += probes
                    return self.table[idx][1]  # return the value
            # linear probing, check the next slot
            idx = (idx + 1) % self.size_m
            if idx == start_idx:  # rolled over to start
                break  # didn't find the key, return None
            probes += 1
        self.total_search_probes += probes
        return None

    # insert the key value pair into the hash tables
    # return True if inserted or False if not inserted
    def insert(self, key, value):
        if self.n >= self.size_m * 0.7:  # load factor ((n/m) >= 0.7)
            self.dynamicResizing()
        # apply the hash
        idx = self._hash(key)
        start_idx = idx
        first_tombstone = None
        probes = 1  # count probes for insertion
        #  if the slot in hash index is already full, look for the
        #  next available slot using linear probing
        while self.table[idx] is not None:
            if self.table[idx][0] is self._TOMBSTONE:  # deleted slot
                if first_tombstone is None:
                    first_tombstone = idx
            elif self.table[idx][0] == key:  # key already exists, update value
                self.table[idx][1] = value  # insert the value
                self.total_insert_probes += probes
                return
            idx = (idx + 1) % self.size_m  # probe
            if idx == start_idx:
                raise Exception("Hash table is full")
            probes += 1
        # Insert at first tombstone if found, else at empty slot
        if first_tombstone is not None:
            self.table[first_tombstone] = [key, value]
        else:
            self.table[idx] = [key, value]
        self.n += 1  # increment element count in the hash table
        self.total_insert_probes += probes

    # remove the key value pair from the hash table
    def delete(self, key):
        # apply the hash
        idx = self._hash(key, self.hash_method)
        start_idx = idx
        while self.table[idx] is not None:
            # if the slot is not a tombstone and the key matches
            if self.table[idx][0] is not self._TOMBSTONE and self.table[idx][0] == key:
                # Mark as deleted assigning a special tombstone object
                self.table[idx] = [self._TOMBSTONE, None]
                self.n -= 1 # decrement count of elts in the table
                return True
            #linear probing, check the next slot
            idx = (idx + 1) % self.size_m
            if idx == start_idx:
                break
        return False
    
    # resize hash table when it reaches a loading factor (0.7 in this
    # hash implementtaion)
    # improveent to just doubling the hash table size,, we set the size to
    # closest next prime number to make division hash efficient
    def dynamicResizing(self):
        #  copy the existing hash table
        prev_table = self.table
        #  double the hash table size and adjust to next prime
        new_size = self.size_m * 2
        self.size_m = nextprime(new_size)
        self.table = [None] * self.size_m
        # reset number of elements and reinsert the old hash entries to the new
        self.n = 0
        for item in prev_table:
            # reinsert the element except tombstones (previously deleted items)
            if item and item[0] is not self._TOMBSTONE:
                self.insert(item[0], item[1])  # key, value

    # Using DBJ2 hash, if I used simple ASCII sum it would generate
    # too many collisions since ngrams can have many similar words
    # with same characters and in different order.
    # Ref: http://www.cse.yorku.ca/~oz/hash.html
    def _hash(self, key):
        # Convert the words in Ngram to numbers
        hash_val = 5381
        # << 5 is equal to multiplying by 32 but faster
        for char in key:
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        # use division hash method
        return hash_val % self.size_m