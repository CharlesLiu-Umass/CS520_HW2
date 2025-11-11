def is_s_palindrome(s):
    # Define the mirror reflection mapping
    mirror_map = {
        'a': 'a', 'b': 'd', 'd': 'b', 'h': 'h', 'i': 'i', 'm': 'm', 
        'o': 'o', 'p': 'q', 'q': 'p', 't': 't', 'u': 'u', 'v': 'v', 
        'w': 'w', 'x': 'x', 'y': 'y'
    }
    
    n = len(s)
    
    # Check if the string is symmetric and each character has a mirror image
    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - 1 - i]
        
        # Check if both characters exist in the mirror_map and are reflections of each other
        if left_char not in mirror_map or right_char not in mirror_map:
            return "NIE"
        if mirror_map[left_char] != right_char:
            return "NIE"
    
    # If it passed all checks, it's an s-palindrome
    return "TAK"
