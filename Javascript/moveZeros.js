function moveZeros(arr) {
  let count = 0;
  let movedList = [];
  let zerosArray = [];
  for(let i = 0; i < arr.length; i++){
    if (arr[i] === 0){
      zerosArray.push(0);
    }
    else {
      movedList.push(arr[i]);
      console.log(arr[i])
    }
  }
  return movedList.concat(zerosArray);
}