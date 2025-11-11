from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    groups = []
    current_group = []
    open_count = 0
    
    for char in paren_string:
        if char == '(':
            if open_count == 0:  # Starting a new group
                current_group = ['(']
            else:
                current_group.append('(')
            open_count += 1
        elif char == ')':
            current_group.append(')')
            open_count -= 1
            if open_count == 0:  # End of a complete group
                groups.append(''.join(current_group))
                current_group = []
    
    return groups
