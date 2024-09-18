def count_characters(string):
    lowercase_count = 0
    uppercase_count = 0
    digit_count = 0
    special_count = 0
    
    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isspace():
        
            special_count += 1
            
    return lowercase_count, uppercase_count, digit_count, special_count
    
  
input_string = "My name is Roderick Vaflor, Age 19, and I like to play a game called BloodStrike."
lowercase, uppercase, digits, special = count_characters(input_string)

print(f"Sentence): {input_string}")
print(f"Lowercase): {lowercase}")
print(f"Uppercase): {uppercase}")
print(f"Digit): {digits}")
print(f"Special Symbol): {special}")
