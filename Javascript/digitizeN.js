function digitize(n) {
  return (String(n).split('')).map(el=>Number(el)).reverse()
}

// Convert number to reversed array of digits
// Given a random non-negative number, you have to return the digits of this number within an array in reverse order.