from linked_list.linked_list import LinkedList

class HashTable:
    """[class used to create and operate on a hashtable]
    """


    def __init__(self, size=256):
        """[creates instance of a hashtable]

        Args:
            _size (int, optional): [sets length of HashTable.]. Defaults to 256.

        Attr: 
            _bucket (list): [a list of LinkedLists with head attr  values set 
            to None]. len(_bucket) == Arg:_size
        """
        self._size = size
        self._bucket = self._size * [LinkedList()]


    def _hash(self, key):
        """[runs key argument through simple hash algorithm]

        Args:
            key ([str]): [string of any length]

        Returns:
            [Int]: [Index between 0 and length of hashtable]
        """
        sum = 0
        for char in key:
            sum += ord(char)
            
        primed = sum * 23
        return primed % self._size


    def add(self, key, value):
        hashed_idx = self._hash(key)

        if self.contains(key):
            raise KeyError(f'hashtable already contains key: {key} at the hashable index.')
        else:
            self._bucket[hashed_idx].insert((key, value))

    def get(self, key):
        bucket = self._bucket[self._hash(key)]
        if not self.contains(key):
            raise ValueError(f'no Key: {key} found in Hashtable object')
        
        curr = bucket.head
        while curr:
            if curr.value[0] == key:
                return curr.value[1]
            else:
                curr = curr.next


    def contains(self, key):
        bucket = self._bucket[self._hash(key)]
        curr = bucket.head
        if curr.value == None:
            return False
        
        while curr:
            if curr.value[0] == key:
                return True
            else:
                curr = curr.next

        return False



    

        