def max_accordion_length(s):
    # The goal is to find the longest valid accordion of the form [ : ... : ]
    n = len(s)
    
    # Step 1: Find the first valid opening bracket '[' and colon ':'
    left_bracket = -1
    first_colon = -1
    for i in range(n):
        if s[i] == '[':
            left_bracket = i
            break
    
    if left_bracket == -1:
        return -1  # No opening bracket found

    for i in range(left_bracket + 1, n):
        if s[i] == ':':
            first_colon = i
            break
    
    if first_colon == -1:
        return -1  # No colon found after '['

    # Step 2: Now find the second colon ':' after the first one
    second_colon = -1
    for i in range(first_colon + 1, n):
        if s[i] == ':':
            second_colon = i
            break
    
    if second_colon == -1:
        return -1  # No second colon found after first one

    # Step 3: Find the closing bracket ']' after the second colon
    right_bracket = -1
    for i in range(second_colon + 1, n):
        if s[i] == ']':
            right_bracket = i
            break
    
    if right_bracket == -1:
        return -1  # No closing bracket found after second colon

    # Step 4: Count the vertical bars '|'
    vertical_bars = 0
    for i in range(first_colon + 1, second_colon):
        if s[i] == '|':
            vertical_bars += 1
    
    # Step 5: The length of the valid accordion is: 
    # 1 for '[' + 1 for ':' + vertical bars + 1 for ':' + 1 for ']'
    return 4 + vertical_bars
