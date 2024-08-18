def beautifulTriplets(d, arr):
    count = 0
    # Write your code here
    for i in range(len(arr)):
        if (arr[i] + d in arr) and (arr[i] + (2 * d)) in arr:
            count +=1
    return count
