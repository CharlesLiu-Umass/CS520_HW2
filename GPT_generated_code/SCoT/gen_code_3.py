def max_accordion_length(s):
    n = len(s)
    
    # Step 1: Find the first '['
    first_open_bracket = -1
    for i in range(n):
        if s[i] == '[':
            first_open_bracket = i
            break
    
    if first_open_bracket == -1:
        return -1  # No opening bracket, impossible to form an accordion
    
    # Step 2: Find the first ':', after the '['
    first_colon = -1
    for i in range(first_open_bracket + 1, n):
        if s[i] == ':':
            first_colon = i
            break
    
    if first_colon == -1:
        return -1  # No colon after '['

    # Step 3: Find the last ':', after the first colon
    second_colon = -1
    for i in range(first_colon + 1, n):
        if s[i] == ':':
            second_colon = i
            break
    
    if second_colon == -1:
        return -1  # No second colon after the first colon
    
    # Step 4: Find the closing bracket ']' after the second colon
    closing_bracket = -1
    for i in range(second_colon + 1, n):
        if s[i] == ']':
            closing_bracket = i
            break
    
    if closing_bracket == -1:
        return -1  # No closing bracket after the second colon
    
    # Step 5: Count the number of vertical lines '|'
    vertical_lines = 0
    for i in range(first_colon + 1, second_colon):
        if s[i] == '|':
            vertical_lines += 1
    
    # The length of the accordion is fixed length 4 plus the number of vertical lines '|'
    return 4 + vertical_lines
