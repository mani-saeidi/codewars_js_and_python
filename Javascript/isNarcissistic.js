function isNarcissistic(n) {
  digitsArr = String(n).split('')
  if (n == digitsArr.reduce((total,digit) => total += Number(digit)**String(n).length,0))
    return true 
  return false; 
}

// A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.

// Ex: 153, where l = 3 ( the number of digits in 153 )
// 13 + 53 + 33 = 153

// Write a function that, given n, returns whether or not n is a Narcissistic Number.

