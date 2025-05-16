class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        *********************************************
        This code was failing 2 test cases out of 107 which are if there are multiple same letters, the cnt in the for loop, it will keep on taking for each letter, because of which time limit will exceed. So an alternative for that is to get the count in dictionary of each letter
        *********************************************

        for i in range(len(s)):
            cnt = s.count(s[i])
            #print(cnt)
            if cnt == 1:
                return i
                break
        return -1
        '''
        charcterInfo = {}

        for i in range(len(s)):
            char = s[i]
            if char in charcterInfo:
                charcterInfo[char] += 1
            else:
                charcterInfo[char]= 1

        for i in range(len(s)):
            if charcterInfo[s[i]] == 1:
                return i
        return -1