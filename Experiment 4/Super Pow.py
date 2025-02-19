class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337  # Given constraint

        def powerMod(x, n):
            """
            Computes (x^n) % MOD using fast modular exponentiation.
            """
            result = 1
            x %= MOD  
            while n:
                if n % 2 == 1:  
                    result = (result * x) % MOD
                x = (x * x) % MOD  
                n //= 2
            return result

        exponent = 0
        for digit in b:
            exponent = (exponent * 10 + digit) % 1140  
        
        return powerMod(a, exponent)
