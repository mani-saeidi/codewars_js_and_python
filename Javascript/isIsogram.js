function isIsogram(str){
  return (new Set(str.toLowerCase().split('')).size == str.length)
}