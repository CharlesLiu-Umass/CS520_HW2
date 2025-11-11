from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group_chars = []  # Using a list of characters for efficient appending
    balance_counter = 0

    for char in paren_string:
        if char == '(':
            balance_counter += 1
            current_group_chars.append(char)
        elif char == ')':
            balance_counter -= 1
            current_group_chars.append(char)
        # Spaces are ignored and not added to current_group_chars.
        # This correctly implements the "Ignore any spaces in the input string" rule,
        # ensuring that the output strings only contain parentheses.

        # If balance_counter returns to 0, it signifies the end of a top-level, balanced group.
        # We also check if current_group_chars is not empty to handle cases where input might start with spaces.
        if balance_counter == 0 and current_group_chars:
            groups.append("".join(current_group_chars))
            current_group_chars = []  # Reset for the next group

    return groups