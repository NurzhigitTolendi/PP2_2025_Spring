def is_palindrome(s):
    cleaned = ''.join(filter(str.isalnum, s)).lower()
    return cleaned == cleaned[::-1]

# Пример использования
text = "A man, a plan, a canal, Panama!"
print(f"Is palindrome: {is_palindrome(text)}")
