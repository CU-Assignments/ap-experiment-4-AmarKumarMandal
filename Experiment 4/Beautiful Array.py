class Solution(object):
    def beautifulArray(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [1]

        odd_part = self.beautifulArray((n + 1) // 2)  
        even_part = self.beautifulArray(n // 2)  

        return [2 * x - 1 for x in odd_part] + [2 * x for x in even_part]
