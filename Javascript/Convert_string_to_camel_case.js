function toCamelCase(str) {
  let allwords = str.replace(/_/g,'-');
  allwords = allwords.split('-',);
  console.log(allwords)
  for (let i = 1; i < allwords.length; i++){
    allwords[i] = allwords[i].charAt(0).toUpperCase() + allwords[i].slice(1);
    
    
  }
  return(allwords.join(''))
}