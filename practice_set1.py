# Q12. Vowel Frequency Analyzer

sentence = input()
count = 0

for ch in sentence.lower():
    if ch in "aeiou":
        count += 1

print(count)


# Q15. Smart Door Lock System

correct_pin = input()

for i in range(3):
    pin = input()
    if pin == correct_pin:
        print("ACCESS GRANTED")
        break
else:
    print("LOCKED")


# Q16. Water Tank Overflow Detector

n = int(input())
inflows = list(map(int, input().split()))

volume = 0

for i in range(n):
    volume += inflows[i]
    if volume > 1000:
        print(i + 1)
        break


# Q19. Number Mirror Validator

number = int(input())
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("PALINDROME")
else:
    print("NOT PALINDROME")


# Q20. Digital Lock Countdown

number = int(input())

while number >= 10:
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10

    number = total

print(number)