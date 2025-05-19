class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """

        attackTime = duration
        currentEnd = timeSeries[0] + duration - 1

        for i in range(1, len(timeSeries)):
            print("currentEnd:", currentEnd, "attackTime : ", attackTime)
            if timeSeries[i] > currentEnd:
                attackTime += duration
                currentEnd = (timeSeries[i] + duration - 1)
            elif currentEnd >= timeSeries[i]:
                attackTime += (duration - (currentEnd - timeSeries[i]) - 1)
                currentEnd = (timeSeries[i] + duration - 1)
        return attackTime

        '''
        class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        totalDuration = duration

        currEnd = timeSeries[0] + duration - 1

        for inst in timeSeries[1:]:
            newEnd = inst+duration-1
            if inst <= currEnd:
                totalDuration += newEnd - currEnd
            else:
                totalDuration +=  duration
            currEnd = newEnd

        return totalDuration
        '''

