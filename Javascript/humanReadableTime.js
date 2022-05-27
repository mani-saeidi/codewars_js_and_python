function humanReadable (seconds) {
  time = []
  sec = String(seconds % 60);
  min = String(Math.floor((seconds/60) % 60));
  hour = String(Math.floor(seconds/3600));
  
  time[2] = sec.length != 2 ? `0${sec}` : sec;
  time[1] = min.length != 2 ? `0${min}` : min;
  time[0] = hour.length != 2 ? `0${hour}` : hour;
  return `${time[0]}:${time[1]}:${time[2]}`
}

// Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

// HH = hours, padded to 2 digits, range: 00 - 99
// MM = minutes, padded to 2 digits, range: 00 - 59
// SS = seconds, padded to 2 digits, range: 00 - 59
// The maximum time never exceeds 359999 (99:59:59)

// You can find some examples in the test fixtures.
//     strictEqual(humanReadable(3599), '00:59:59', 'humanReadable(3599)');