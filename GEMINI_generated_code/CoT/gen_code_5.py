def calculate_martian_days_off(n: int) -> tuple[int, int]:
    """
    Calculates the minimum and maximum possible number of days off
    in a Martian year of n days.

    Args:
        n: The number of days in a Martian year (1 <= n <= 1,000,000).

    Returns:
        A tuple containing two integers: (minimum_days_off, maximum_days_off).
    """

    # Calculate the number of full 7-day weeks and remaining days
    num_full_weeks = n // 7
    remaining_days = n % 7

    # Days off from full weeks are fixed (2 days off per week)
    base_days_off = num_full_weeks * 2

    # --- Calculate Minimum Days Off ---
    min_additional_off = 0
    # If remaining_days is 6, we must have at least one day off.
    # (e.g., if the 6 days are Mon-Sat, Saturday is a day off).
    # For remaining_days <= 5, we can choose a starting day (e.g., Monday)
    # so all remaining days are work days.
    if remaining_days == 6:
        min_additional_off = 1
    
    min_total_days_off = base_days_off + min_additional_off

    # --- Calculate Maximum Days Off ---
    max_additional_off = 0
    # If remaining_days is 1, we can have that single day be a day off
    # (e.g., start the year on Saturday).
    if remaining_days == 1:
        max_additional_off = 1
    # If remaining_days is 2 or more, we can arrange the start of the year
    # to include both weekend days (Saturday and Sunday).
    # (e.g., start the year on Saturday, so Sat and Sun are days off).
    elif remaining_days >= 2:
        max_additional_off = 2
    
    max_total_days_off = base_days_off + max_additional_off

    return min_total_days_off, max_total_days_off