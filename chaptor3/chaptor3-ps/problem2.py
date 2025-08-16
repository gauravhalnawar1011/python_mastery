# Program: Fill in a letter template with user input

# Template with placeholders <|Name|> and <|Date|>
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Taking input from user
name = input("Enter your Name: ")
date = input("Enter the Date: ")

# Replace placeholders with actual values
# Note: .replace() only changes the first match, but by chaining you can replace multiple parts
filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)

print("\n--- Filled Letter ---")
print(filled_letter)


# Example: using hardcoded values (no input needed)
print("\n--- Example with hardcoded values ---")
print(letter.replace("<|Name|>", "Gaurav").replace("<|Date|>", "16 Aug 2025"))
