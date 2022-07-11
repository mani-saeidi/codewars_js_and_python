function removeK(k){
  return k**2+((k+1)*k) / 2;
}

// Task
// Given a number k, find the smallest integer n such that if any k elements are removed from the set {1, 2, ..., n}, one can still find k distinct numbers among the remaining elements with sum of n.

// Input/Output
// [input] integer k

// The number of elements to be removed.

// 2 ≤ k ≤ 10000

// [output] an integer

// The smallest value of n.

// Example
// For k = 2, the output should be 7.

// The initial set is {1, 2, 3, 4, 5, 6, 7}.

// No matter what 2 elements you remove, (1, 6), (2, 5), or (3, 4) will sum up to 7.

// Why isn't the result 6? Because: In set {1, 2, 3, 4, 5, 6}, if we remove 2 elements (1,2), or (4,5) the remaining elements do not contain 2 elements that sum up to 6.