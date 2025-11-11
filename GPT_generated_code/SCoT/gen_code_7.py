def is_palindrome(time):
    # Check if the given time is a palindrome
    return time[0] == time[4] and time[1] == time[3]

def increment_time(hh, mm):
    # Increment the time by one minute, handling overflow
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
        if hh == 24:
            hh = 0
    return hh, mm

def min_sleep_time(time):
    # Parse input time string
    hh, mm = map(int, time.split(":"))
    
    # Start counting minutes
    minutes = 0
    while True:
        # Format current time as a string
        current_time = f"{hh:02}:{mm:02}"
        
        # Check if current time is a palindrome
        if is_palindrome(current_time):
            return minutes
        
        # Increment the time by one minute
        hh, mm = increment_time(hh, mm)
        
        # Increment the counter
        minutes += 1
