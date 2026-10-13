# PROG 3.1

text = input("Input String : ")

letters = 0
digits = 0
special_symbols = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special_symbols += 1

print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of special symbols:", special_symbols)
