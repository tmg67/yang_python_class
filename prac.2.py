def is_palindrome(s):
    # Convert to lowercase to make the comparison case-insensitive
    s = s.lower()
    
    # Remove spaces and non-alphanumeric characters
    cleaned_s = ''.join(char for char in s if char.isalnum())
    
    # Compare the cleaned string with its reverse
    return cleaned_s == cleaned_s[::-1]

# Example usage
word = " mom "
if is_palindrome(word):
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')