# print("Hello World")

'''#Add two numbers 
a = int(input("Entre the first number : "))
b = int(input("Entre the second number : "))

sum = a+b
print(sum)'''

# #check wheteher number is even or odd

# n = int(input("Entre the number : "))

# if n % 2 == 0:
#     print(f"Number is even : {n}")
# else:
#     print(f"Number is odd {n}")

'''#find largest in two numbers
a = int(input("Entre the first number : "))
b = int(input("Entre the second number : "))

if a > b:
    print(f"Number 1 is larget : {a}")
elif b > a:
    print(f"Number 2 is larget : {b}")
else:
    print(f"Numbers are equal")
    '''

# #find largest number in three numbers
# a = int(input("Entre the first number : "))
# b = int(input("Entre the second number : "))
# c = int(input("Entre the third number : "))

# if a >= b and a >= c:
#     print(f"Number a is bigger {a}")
# elif b >= a and b >= c:
#     print(f"Number b is bigger {b}")
# else:
#     print(f"Number c is bigger {c}")

# print("Largest Number : ", max(a, b, c))

'''# check positive negative number

n = int(input("Entre the number : "))

if n > 0:
    print(f"Number is positive : {n}")
elif n < 0:
    print(f"Number is negative : {n}")
else:
    print(f"Number is zero : {n}")'''

# #swap two numbers

# a = int(input("Entre the first number : "))
# b = int(input("Entre the second number : "))
# print(a)
# print(b)


# temp = a
# a = b
# b = temp

# print("Aftre swap", a)
# print("After swap", b)

'''#Find the sum of digits

n = int(input("Entre the number : "))

sum = 0

while n > 0 :
    digit = n % 10
    sum += digit
    n = n // 10

print(sum)'''

# #reverse a number

# n = int(input("Entre the number : "))
# reverse = 0
# while n > 0:
#     digit =  n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)
'''
# count the digit in a number

n = int(input("Entre the number : "))
count = 0
if n == 0:
    count = 0
else:
    while n > 0:
        count += 1
        n = n // 10
# print("Count is:" , count)'''

# #check whether the number is palidrome or not 

# n = int(input("Entre the number : "))
# rev = 0
# original  = n

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print(rev)

# if original == rev:
#     print(f"Number is palidrome : {rev}")
# else:
#     print(f"Number is not palidrome : {rev}")

# print("Original :", original)
'''
# check the number is Armstrong or not ?

n = int(input("Entre the number : "))
temp = n 
sum = 0
power = len(str(n))

while n > 0:
    digit = n % 10
    sum += digit **power
    n = n // 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")'''

# #find factrorial

# n = int(input("Entre the number : "))
# if n < 0:
#     print("Factorial cannot be found :")
# else:
#     fact = 1

#     for i in range(1, n+1):
#         fact *= i
#     print(f"Factorial of {n} is", fact)

'''#print a multiplication table

n = int(input("Entre the number : "))

for i in range(1, 11):
    print(n, "*", i , "=", n * i)'''

# #check a prime number 
# n = int(input("Entre the number : "))
# if n <  2 :
#     print("Not a prime")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
'''
# fibbonaci series
n = int(input("Entre the number : "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c'''

# #find the GCD of two numbers.

# a = int(input("Entre the first number : "))
# b = int(input("Entre the second number : "))
# gcd = 1
# for i in range(1, min(a,b)+1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

#  print("GCD : ", gcd)


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# for i in range(max(a, b), (a * b) + 1):
#     if i % a == 0 and i % b == 0:
#         lcm = i
#         break

# print("LCM:", lcm)

