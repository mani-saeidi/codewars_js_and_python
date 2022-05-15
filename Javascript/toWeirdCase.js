function toWeirdCase(string){
  splitString = string.split(' ')
  weirdList = [];
  weirdString = ''
  for (let i = 0; i < splitString.length; i++){
    let evenCap = ''
    for (let j = 0; j < splitString[i].length; j++){
       j % 2 == 0 ? evenCap += splitString[i][j].toUpperCase() : evenCap += splitString[i][j];
    }
    weirdList.push(evenCap)
  }
  weirdString = weirdList.join(' ')
  return weirdString
}
console.log(toWeirdCase('This is a test'))
//ThIs Is A TeSt