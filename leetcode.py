def getMoneySpent(keyboards, drives, b):
    # Write your code here.
    maxbudget = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                maxbudget = max(maxbudget, (keyboards[i] + drives[j]))
    return maxbudget
