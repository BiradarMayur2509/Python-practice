"""
Given a title case string, Write a programme to modify the string as given below.
 Add (-) hyphen before each upper case character, excluding the first upper case character
 Converts all uppercase characters into lowercase characters.
 
 i/p : TitleCase
 o/p : title-case
"""

string = input()
result = string[0].lower()

for char in string[1:]:
    if char.isupper():
        result += "-"
        result += char.lower()
    else:
        result += char


print(result)