function dontGiveMeFive(start, end)
{
  let listOfNums = [];
  for (let i = start; i <= end; i++){
    if (!String(i).includes(5)){
      listOfNums.push(i);
    }
  }
  return listOfNums.length;
}