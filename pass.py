
import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "0123456789"
symbols = "[](){},./\_-=!@#$%^&*"

upper, lower, nums, syns  = True, True, True, True
all = ""
if upper:
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += digits
if syns:
    all += symbols

length = int(input("Enter Length of Password: "))
numbers = int(input("How Many Passwords You Want: "))

for x in range(numbers):
    password = "".join(random.sample(all, length))
    print(password)

