name = input("What is your name?")
print("hello", name)
age = input("How old are you?")
try:
    # another way to format print is via f-strings
    print(f"{name}, you were born in {2024 - int(age)}"

except:
    print("Age must be a valid number")