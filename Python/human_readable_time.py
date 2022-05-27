def make_readable(seconds):
    sec = str(seconds % 60)
    min = str((seconds//60) % 60)
    hour = str(seconds // 3600)
    time = ['h','m','s']
    
    if len(sec) < 2:
        time[2] = f'0{sec}'
    else:
        time[2] = sec
    if len(min) < 2:
        time[1] = f'0{min}'
    else:
        time[1] = min
    if len(hour) < 2:
        time[0] = f'0{hour}'
    else:
        time[0] = hour
    
    return ':'.join(time)
    
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.
#     strictEqual(make_readable(3599), '00:59:59', 'make_readable(3599)');