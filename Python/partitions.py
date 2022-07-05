def partitions(n):
    p = [0] * n
    k = 0
    p[k] = n
    list_partitions = []
    while True:
            list_partitions.append([i for i in p if i != 0])
            rem_val = 0
            while k >= 0 and p[k] == 1:
                rem_val += p[k]
                k -= 1
            if k < 0:
                return len(list_partitions)
            p[k] -= 1
            rem_val += 1
            while rem_val > p[k]:
                p[k + 1] = p[k]
                rem_val = rem_val - p[k]
                k += 1
            p[k + 1] = rem_val
            k += 1
    


# An integer partition of n is a weakly decreasing list of positive integers which sum to n.

# For example, there are 7 integer partitions of 5:

# [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
# Write a function which returns the number of integer partitions of n. The function should be able to find the number of integer partitions of n for n at least as large as 100.