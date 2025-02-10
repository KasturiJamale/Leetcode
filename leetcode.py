class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorteds = sorted(s)
        sortedt = sorted(t)

        return sorteds == sortedt

        '''
        i=0

        if len(sorteds) != len(sortedt):
            return False

        if len(sorteds) == len(sortedt):
            while i in range(len(sorteds)):
                if sorteds[i] != sortedt[i]:
                    return False
                i+=1
            return True
        '''
