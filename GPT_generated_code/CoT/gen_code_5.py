def martian_days_off(n):
    # Full weeks in the year
    full_weeks = n // 7
    # Remaining days after full weeks
    remaining_days = n % 7
    
    # Maximum days off:
    max_days_off = 2 * full_weeks + min(remaining_days, 2)
    
    # Minimum days off:
    min_days_off = 2 * full_weeks
    
    return min_days_off, max_days_off
