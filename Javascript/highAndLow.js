function highAndLow(numbers){
  return `${Math.max(...(numbers.split(' ').map(el => Number(el))))} ${Math.min(...(numbers.split(' ').map(el => Number(el))))}`
}