# capitalize

original_string = "hello world"

capitalized_string = original_string.capitalize()
center_string = original_string.center(23, "*")

substring = "o"
substring_count = original_string.count(substring, 1, 20)

print("-"*30)
print("ORIGINAL STRING: ", original_string)
print("-"*30)
print(".capitalize(): ", capitalized_string)
print(".center(23, '*'): ", center_string)
print(".count(1, 20): ", substring_count)
