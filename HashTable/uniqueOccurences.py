class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counted = Counter(arr)
        occ = [counted[key] for key in counted]
        
        if len(set(occ)) == len(occ):
            return True
        else:
            return False