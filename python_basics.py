# print("What does the Visualize button do?")
# n1 = int(input("Entre number 1 : "))
# n2 = int(input("Entre number 2 : "))
# print("Sum of two number")
# sum = n1+n2;
# print(sum)



# n = int(input("Entre the number : "))
# print("Number is even or odd")
# print("---------------------")
# if n % 2 == 0 :
#   print(f"Number is even  : {n}")
# else:
#   print(f"Number is odd  : {n}")



# n1 = int(input("Entre the number : "))
# n2 = int(input("Entre the number : "))
# print("Number is largest form another number")
# print("-------------------------------------")
# if n1 > n2 :
#   print(f"Numbe one is larger than number two : {n1}")
# else:
#   print(f"Number two is greter than the first number {n2}")


# n1 = int(input("Entre the number : "))
# n2 = int(input("Entre the number : "))
# n3 = int(input("Entre the number : "))
# print("Number is largest form another number")
# print("-------------------------------------")
# if n1 > n2 :
#   print(f"Numbe one is larger than number two : {n1}")
# elif n1 > n3:
#   print(f"Number two is greter than the first number : {n1}")
# elif n2 > n3 :
#   print(f"Number 2 is graeter than the third number :  {n2}")
# else:
#   print(f"Number three is grater than the first two number  : {n3}")



# n = int(input("Entre the number : "))
# print("Number is positive negative or zero")
# print("-----------------------------------")
# if n > 0:
#   print(f"Number is positive : {n}")
# elif n < 0:
#   print(f"Number is negative : {n}")
# else:
#   print(f"Number is zero : {n}")


# print("What does the Visualize button do?")
# n = int(input("Entre the number : "))
# print("Sum of the digit of the number")
# sum = 0
# while n > 0 :
#   digit = n % 10
#   sum +=  digit
#   n =  n // 10

# print(f"Sum of the number is : {sum}")

# n = int(input("Entre the number : "))
# print("Reverse of the digit of the number")
# reverse  = 0

# while n > 0 :
#   digit = n % 10
#   reverse = (reverse*10)  + digit
#   n  = n // 10
# print(f"reverse of the number is : {reverse}")

# n = int(input("Entre the number : "))
# print("Count of the digit of the number")
# count  = 0


# while n > 0 :
#   count += 1
#   n = n // 10
# print(f"Count of the number is : {count}")


# n = int(input("Entre the number : "))
# print("Palindrome of the digit of the number")
# reverse  = 0
# orignal = n


# while n > 0 :
#   digit = n % 10
#   reverse = (reverse * 10) + digit
#   n = n // 10

# if reverse  == orignal:
#   print(f"Number is palindrome number : {reverse}")
# else:
#   print(f"Number is not Palidrome number : {reverse}")


# num = int(input("Entre the Number : "))
# temp = num
# digits = len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit ** digits
#     temp = temp // 10

# if sum == num :
#     print(num, "is an armstrong number")
# else:
#     print(num, "is not an armstrong number")

# n = int(input("Entre the number"))
# factorial = 1
# for i in range(1, n+1):
#     factorial = factorial*i
# print(factorial)


# n = int(input("Entre the number "))
# for i in range(1, 11):
#     print(n, "*", i , "=", n * i)

'''
n = int(input("Entre the number"))

if n <= 1 :
    print("Neither prime nor composite")
else:
    count = 0 

for i  in range(1, n+1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not prime ")
'''

# #fibbonaci series

# n = int(input("Entre the number : "))
# a = 0
# b = 1
# for i in range(n+1):
#     print(a, end= " ")
#     c = a+b
#     a = b
#     b = c

'''
#reverse a strign without using slicing

name = input("Entre a string")
original = name
reverse = ""

for i in range(len(name)):
    reverse = name[i] + reverse
print(f"Reverse of the string is:  {reverse}")
print(f"Original string is : {original}")
'''

# #revrese the string chaech pallidrom or not
# name = input("Enter a string: ")

# reverse = ""
# original = name

# for i in range(len(name)):
#     reverse = name[i] + reverse

# if reverse == original:
#     print(f"String is palindrome: {reverse}")
# else:
#     print(f"String is not palindrome: {reverse}")
'''

#count the number of vowels and consonants in a string
string = input("Entre the string :")
vowels = 0
consonants = 0

for i in string:
    if i.isalpha():
        if i.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(f"Number of vowels : {vowels}")
print(f"number of consonants : {consonants}")'''

# count word in the sentence

# string = input("Entre a string : ")
# words = string.split()
# count = len(words)

# for i in words:
#     print(i)
# print(f"Number of words in the string : {count}")

'''"# count fruqancy of each character in the string
string = input("Entre the frequancy")
char_count = {}
for char in string:
    if char in char_count :
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"Character frequency in the string: {char_count}")
 "'''

# #remove spaces form the string
# string = input("Entre the string : ")
# string = string.replace(" ", "")
# print(f"String after removing spaces : {string}")
'''
#remove dulicate character from the string
string = input("Entre the string  : ")
chars = ""
for char in string:
    char = char.lower()

    if char not in chars:
        chars += char
        
print(f"String after removing duplicate characters : {chars}")
'''

# #find the first non-repaeting character

# string = input("Entre the string : ")

# for char in string :
#     if string.count(char ) == 1:
#         print(f"First non-repeating character is : {char}")
#         break

'''
#find first two string is anargam or not

string1 = input("Entre the first string : ")
string2 = input("Entre the second string : ")

if sorted(string1) == sorted(string2):
    print(f"{string1} and {string2} are anagrams")
else:
    print(f"{string1} and {string2} are not anagrams")
    '''

# find the longest word in the string

string = input("Entre the string : ")
words = string.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Longest word in the string is: {longest_word}")