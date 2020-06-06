class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def compare(p1,p2):
            if p1[0] != p2[0]:
                return -(p1[0] - p2[0])
            else:
                if p1[1] > p2[1]:
                    return 1
                else:
                    return -1
        
        people = sorted(people,cmp=compare)
        
        arr = []
        
        for p in people:
            arr.insert(p[1],p)
            
        return arr
        