function isPangram(string){
  alphabet='abcdefghijklmnopqrstuvwxyz'
  letters = string.toLowerCase().split('')
  organized = letters.filter(letter => 'abcdefghijklmnopqrstuvwxyz'.includes(letter))
                     .sort((a,b) => a > b ? 1 : -1)
  organized = [...new Set(organized)]
  return alphabet == organized.join('') ? true : false;
}

// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.