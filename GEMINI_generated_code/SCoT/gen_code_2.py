from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    current_group: List[str] = []  # To build the current group efficiently
    balance_counter: int = 0

    # Step 1: Clean the input string by removing all spaces.
    # This simplifies subsequent character processing.
    cleaned_string = paren_string.replace(" ", "")

    # Step 2 & 3: Iterate through the cleaned string to identify and separate groups.
    for char in cleaned_string:
        # Add the current character to the group being formed.
        current_group.append(char)

        # Update the balance counter based on the character.
        if char == '(':
            balance_counter += 1
        elif char == ')':
            balance_counter -= 1

        # If the balance counter returns to zero, it signifies the end of a
        # complete, balanced, top-level parenthesis group.
        if balance_counter == 0:
            # Join the characters collected for the current group into a string
            # and add it to our list of results.
            result.append("".join(current_group))
            # Reset current_group to prepare for collecting the next group.
            current_group = []

    # Step 4: Return the list of separated groups.
    return result