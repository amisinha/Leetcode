class MyHashSet:

    def __init__(self):
        self.obj = set()
        

    def add(self, key: int) -> None:
        self.obj.add(key)
        

    def remove(self, key: int) -> None:
        self.obj.discard(key)
        

    def contains(self, key: int) -> bool:
        return key in self.obj
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)