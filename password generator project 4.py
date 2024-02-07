print("welcome to password generator")
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','?','(',')']
no_letters=int(input("enetr no. of letters you want"))
no_numbers=int(input("enetr no. of numbers you want"))
no_symbols=int(input("enetr no. of symbols you want in your password"))
password=" "
for i in range(no_letters):
    a=random.randint(0,len(letters))
    password=password+letters[a]
for i in range(no_numbers):
    a=random.randint(0,len(numbers))
    password=password+numbers[a]
for i in range(no_symbols):
    a=random.randint(0,len(symbols))
    password=password+symbols[a]
print("your password is:",password)
