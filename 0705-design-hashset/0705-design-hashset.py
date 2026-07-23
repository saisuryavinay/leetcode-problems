class MyHashSet:

    def __init__(self):
       self.hash_map = {} 

    def add(self, key: int) -> None:
        self.hash_map[key] = True
 
    def remove(self, key: int) -> None:
        self.hash_map.pop(key,None)
    def contains(self, key: int) -> bool:
        return self.hash_map.get(key,False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)