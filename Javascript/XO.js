function XO(str) {
    const count = str.toLowerCase().split('').reduce((total,letter) => {
      total[letter] = (total[letter] || 0) + 1
      return total
    },{})
    return count.x == count.o
}

// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false