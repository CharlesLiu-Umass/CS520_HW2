def martian_days_off(n):
    # Number of full weeks
    full_weeks = n // 7
    # Leftover days after full weeks
    leftover_days = n % 7
    
    # Minimum days off: We assume leftover days are workdays
    min_days_off = full_weeks * 2
    # Maximum days off: We assume leftover days are weekends
    max_days_off = full_weeks * 2 + min(leftover_days, 2)
    
    return min_days_off, max_days_off
