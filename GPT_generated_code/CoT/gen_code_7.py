def is_palindrome(time):
    # Check if the time in the format 'hh:mm' is a palindrome
    return time == time[::-1]

def time_to_palindrome(current_time):
    hh, mm = map(int, current_time.split(":"))
    minutes_passed = 0
    
    while True:
        # Check if current time is a palindrome
        time_str = f"{hh:02}:{mm:02}"
        if is_palindrome(time_str):
            return minutes_passed
        
        # Increment time by one minute
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == 24:
                hh = 0
        
        minutes_passed += 1
