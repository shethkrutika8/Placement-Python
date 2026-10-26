# #find the length of the string

# str = input("Entre a string  :")
# string = len(str)
# print("Length of the string is : ", string)
'''
#reverse  string

str = input("Entre a string : ")
rev = ""
for i in range(len(str)-1, -1, -1):
    rev += str[i]

print("Reverse : ", rev)'''

# #check whether string is a palidrome or not ?

# str = input("Entre a string : ")
# rev = ""
# original = str

# for i in range(len(str)-1, -1, -1):
#     rev += str[i]

# print ("Reverse : ", rev)

# if rev == original :
#     print("String is a pallindrome")
# else:
#     print("String is not a palidrome")

'''#count the vowels and consonents

str = input("Entre the string : ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonent_count = 0

for char in str:
    if char in vowels:
        vowel_count += 1
    else:
        consonent_count += 1

print("Vowels in the string : ", vowel_count)
print("consonent in the string : ", consonent_count)'''

# #count uppercase and lowercase
# str = input("Entre the string : ")
# uppercase = 0
# lowercase = 0
# for char in str:
#     if char.isupper():
#         uppercase += 1
#     else:
#         lowercase += 1
# print("Uppser case letter : ", uppercase)
# print("Lowercase letter : ", lowercase)
'''
#count the number of the digit in the string

str = input("Entre the string : ")
count = 0

for char  in str:
   if char.isdigit():
      count += 1

print("Number of the digit in the string is:" , count)
'''

# #count spaces in the string

# str = input("Entre a string : ")
# count = 0

# for char in str:
#     if char.isspace():
#         count += 1
# print("Count the spaces: ", count)


'''
#remove all the spaces form a string

str = input("Entre a string : ")
space = ""

for char in str:
    if char != " ":
        space += char

print("String without the space : ", space)

text = input("Entre a string : ")
space = text.replace(" ", "")
print(space)'''

# #count the frequancy of a character

# text = input("Entre a string : ")
# frequancy = {}

# for char in text :
#     if char in frequancy:
#         frequancy[char] += 1
#     else:
#         frequancy[char] = 1
# print(frequancy)
'''
#replace space with hypens

name = input("Entre a string : ")
space = name.replace(" ", "-")
print(space)'''

# # check whether twon string are anargrams

# str1 = input("Entre string 1: ")
# str2 = input("Entre string 2: ")

# if len(str1) != len(str2):
#     print("Not Amargam")
# else:
#     for i in str1:
#         if str1.count(i) != str2.count(i):
#             print("Not amargam")
#             break
#     else:
#         print("Amargam")

'''#Remove duplicate characater

str = input("Entre the string : ")
result = "" 

for char in str:
    if char not in result :
         result += char

print(result)
'''

#find the first non repeating character

str = input("Entre the string : ")

for char in str:
    if str.count(char) == 1:
        print("First non-repeating character : ", char)
        break
else:
        print("No non-reapetign charatare")
