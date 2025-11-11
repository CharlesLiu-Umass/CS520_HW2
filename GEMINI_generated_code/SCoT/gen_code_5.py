def calculate_martian_days_off(n: int) -> tuple[int, int]:
    """
    Calculates the minimum and maximum possible number of days off per year on Mars.

    A Martian year lasts n days. Martian weeks are 5 work days and 2 days off.

    Args:
        n: The number of days in a Martian year (1 <= n <= 1,000,000).

    Returns:
        A tuple containing two integers: (minimum_days_off, maximum_days_off).
    """

    # Calculate days off from full weeks.
    # Each full week (7 days) always contains 2 days off.
    full_weeks_days_off = (n // 7) * 2

    # Calculate the number of remaining days after accounting for full weeks.
    remainder_days = n % 7

    # --- Calculate Minimum Possible Days Off ---
    # To minimize days off, we want the 'remainder_days' to fall on work days.
    # In a 7-day cycle (W W W W W D D), we can have up to 5 consecutive work days.
    # - If remainder_days is 0, 1, 2, 3, 4, or 5: We can always align the start
    #   of the year so these days are all work days (e.g., start on Monday).
    #   So, 0 additional days off from the remainder.
    # - If remainder_days is 6: Even if we start on Monday, the 6th day will be
    #   a Saturday (a day off). So, 1 additional day off from the remainder.
    min_extra_days_off = 0
    if remainder_days == 6:
        min_extra_days_off = 1
    
    minimum_days_off = full_weeks_days_off + min_extra_days_off

    # --- Calculate Maximum Possible Days Off ---
    # To maximize days off, we want the 'remainder_days' to fall on days off.
    # In a 7-day cycle (D D W W W W W), we can have up to 2 consecutive days off.
    # - If remainder_days is 0: No additional days off.
    # - If remainder_days is 1: We can start on Saturday, getting 1 day off.
    # - If remainder_days is 2 or more: We can start on Saturday, getting both
    #   Saturday and Sunday as days off. This gives 2 additional days off.
    # This can be elegantly expressed as taking the minimum of 'remainder_days' and 2.
    max_extra_days_off = min(remainder_days, 2)

    maximum_days_off = full_weeks_days_off + max_extra_days_off

    return [minimum_days_off, maximum_days_off]