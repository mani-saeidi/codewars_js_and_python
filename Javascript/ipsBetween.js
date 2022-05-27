function ipsBetween(start, end){
  ipOne = start.split('.');
  ipTwo = end.split('.');
  ipDiff = [];
  for (let i = 0; i < ipOne.length; i++){
    for (let j = 0; j < ipTwo.length; j++){
      if (i == j){
        ipDiff.push(ipTwo[i]-ipOne[j])
      }
    }
  }
  return ipDiff[0]*256*256*256 + ipDiff[1]*256*256 + ipDiff[2]*256 + ipDiff[3]
}

// Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

// All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

// Examples
// * With input "10.0.0.0", "10.0.0.50"  => return   50 
// * With input "10.0.0.0", "10.0.1.0"   => return  256 
// * With input "20.0.0.10", "20.0.1.0"  => return  246