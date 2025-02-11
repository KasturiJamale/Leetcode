class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        n = [int(d) for d in str(x)]
        print(n, len(n))
        i = 0
        j = len(n) - 1

        while i < len(n)//2:
            if n[i] != n[j]:
                return False
            i+=1
            j-=1
        return True