var capitals = function (word) {
  result = []
	for (let i = 0; i < word.split('').length; i++){
    if (word.charCodeAt(i) < 92)
      result.push(i)
  }
  return result
};

// Instructions
// Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

// Example
// Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );