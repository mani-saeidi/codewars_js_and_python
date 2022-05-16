function incrementString (strng) {
  let index = strng.search(/[0-9]/g);
  let splitTextAndNums = [];
  if (strng === '' || index === -1)
    return strng + String(1);
  else splitTextAndNums.push( strng.substring(0, index), strng.substring(index, strng.length) );
  
  let numBreaker = splitTextAndNums[1].split('');
  for (let i = (numBreaker.length - 1); i >= 0; i--) {
    if (numBreaker[i] < 9) {
      numBreaker[i]++;
      break;
    }
    else if (numBreaker[i] == 9 && i === 0) {
      numBreaker[i] = 10;
    }
    else if (numBreaker[i] == 9) {
      numBreaker[i] = 0;
    }
  }
  numBreaker = numBreaker.join("");
  return splitTextAndNums[0] + numBreaker;
}

// Your job is to write a function which increments a string, to create a new string.

// If the string already ends with a number, the number should be incremented by 1.
// If the string does not end with a number. the number 1 should be appended to the new string.
// Examples:

// foo -> foo1

// foobar23 -> foobar24

// foo0042 -> foo0043

// foo9 -> foo10

// foo099 -> foo100

// Attention: If the number has leading zeros the amount of digits should be considered.