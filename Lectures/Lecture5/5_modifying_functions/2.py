import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net" 

pattern = r"[Jj]ohn" # our regex 

replaced_match_with = 'Johnny'

result = re.sub(pattern, replaced_match_with, text_to_match)

print(result) 