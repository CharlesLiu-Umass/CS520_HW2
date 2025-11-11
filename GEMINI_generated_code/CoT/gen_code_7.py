def find_next_palindrome_time(current_time_str: str) -> int:
    """
    Calculates the minimum number of minutes until the next palindrome time.

    Args:
        current_time_str: A string representing the current time in "hh:mm" format.

    Returns:
        The minimum number of minutes Karen should sleep.
    """

    # Helper function to check if a time (given as integers h, m) is a palindrome
    def is_palindrome(h: int, m: int) -> bool:
        # Format hours and minutes as two-digit strings
        h_str = f"{h:02d}"
        m_str = f"{m:02d}"
        
        # A time HH:MM is a palindrome if HH is the reverse of MM
        return h_str == m_str[::-1]

    # Parse the input time string
    parts = current_time_str.split(':')
    current_hh = int(parts[0])
    current_mm = int(parts[1])

    minutes_slept = 0

    # Loop indefinitely until a palindrome time is found
    while True:
        # Check if the current time is a palindrome
        if is_palindrome(current_hh, current_mm):
            return minutes_slept

        # Increment time by one minute
        current_mm += 1
        if current_mm == 60:
            current_mm = 0
            current_hh += 1
            if current_hh == 24:
                current_hh = 0  # Reset to midnight

        # Increment the counter for minutes slept
        minutes_slept += 1