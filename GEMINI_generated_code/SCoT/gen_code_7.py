def get_next_palindrome_time_minutes(current_time_str: str) -> int:
    """
    Calculates the minimum number of minutes Karen should sleep until the
    time is a palindrome.

    Args:
        current_time_str: The current time in "hh:mm" 24-hour format.

    Returns:
        The minimum number of minutes until a palindrome time.
    """

    def is_palindrome(h: int, m: int) -> bool:
        """
        Checks if a given hour and minute combination forms a palindrome time string.
        """
        # Format hours and minutes with leading zeros if necessary
        h_str = str(h).zfill(2)
        m_str = str(m).zfill(2)
        
        # Concatenate to form the "hh:mm" string
        time_display = h_str + ":" + m_str
        
        # Check if the string is a palindrome
        return time_display == time_display[::-1]

    # Parse the input time
    current_h_str, current_m_str = current_time_str.split(':')
    current_h = int(current_h_str)
    current_m = int(current_m_str)

    minutes_slept = 0

    # Loop indefinitely until a palindrome time is found
    # The loop is guaranteed to terminate as 00:00 is always a palindrome
    # and a full day is 1440 minutes.
    while True:
        # Check if the current time (after potential minute increments) is a palindrome
        if is_palindrome(current_h, current_m):
            return minutes_slept
        
        # If not a palindrome, increment time by one minute
        minutes_slept += 1
        current_m += 1

        # Handle minute overflow (60 minutes -> 1 hour)
        if current_m == 60:
            current_m = 0
            current_h += 1

            # Handle hour overflow (24 hours -> 00:00 next day)
            if current_h == 24:
                current_h = 0