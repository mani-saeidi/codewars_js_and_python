def sum_of_diff(arr):
  total = []
  arr = sorted(arr, reverse=True)
  for index,each_num in enumerate(arr[0:-1]):
    a = arr[index] - arr[index+1]
    total.append(a)
  return sum(total)
  
print(sum_of_diff([2,1,10]))

# Your task is to sum the differences between consecutive pairs in the array in descending order.

# For example:

# sum_of_diff([2, 1, 10])
# Returns 9

# Descending order: [10, 2, 1]

# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell).