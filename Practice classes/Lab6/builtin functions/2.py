def count_case_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count


text = "Hello World!"
upper, lower = count_case_letters(text)
print(f"Upper case letters: {upper}, Lower case letters: {lower}")
