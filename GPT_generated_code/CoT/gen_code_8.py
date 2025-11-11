def is_s_palindrome(s):
    # A dictionary to check character mirror properties
    mirror_chars = {
        'a': 'A', 'A': 'a', 'o': 'O', 'O': 'o', 'X': 'X', 'x': 'X', 'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'
    }

    # Convert the string to lowercase to make case-insensitive comparisons
    s = s.lower()

    # Check the string symmetry from both ends
    n = len(s)
    
    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - i - 1]

        # Check if the characters match or can mirror each other
        if left_char not in mirror_chars or mirror_chars[left_char] != right_char:
            return "NIE"
    
    return "TAK"
