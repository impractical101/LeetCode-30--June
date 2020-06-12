#Submitted by thr3sh0ld
#Logic: Use dictionary operations.
class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.lis = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.dic)
        self.lis.append(val)
        return True    
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.dic: 
            return False
        
        loc = self.dic[val] #Location index
        self.lis[loc] = self.lis[len(self.dic)-1]
        self.dic[self.lis[loc]] = loc
        self.lis.pop(len(self.dic)-1)
        del self.dic[val]
                
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        :rtype: int
        """
        from random import randint
        randin = random.randint(0, len(self.dic) - 1)
        return self.lis[randin]