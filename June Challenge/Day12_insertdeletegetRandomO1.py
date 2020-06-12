class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = []
        self.data = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        
        self.map.append(val)
        self.data[val] = len(self.map)-1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            index = self.data[val]
            l = len(self.map)
            self.map[index],self.map[l-1] = self.map[l-1],self.map[index]
            self.data[self.map[index]] = index
            self.map.pop()
            del self.data[val]
            return True
        
        return False
            
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0,len(self.map)-1)
        return self.map[index]