class RandomizedCollection:

    def __init__(self):
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.list:
            self.list.append(val)
            return False
        else:
            self.list.append(val)
            return True      

    def remove(self, val: int) -> bool:
        if val in self.list:
            index = self.list.index(val)
            del self.list[index]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()