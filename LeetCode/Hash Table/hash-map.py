class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """

        self.hashMap[key] = value
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """

        if key in self.hashMap:
            return self.hashMap[key]
        else:
            return -1


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """

        if key in self.hashMap:
            del self.hashMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)