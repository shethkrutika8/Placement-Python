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

#count the number of the digit in the string

str = input("Entre the string : ")
count = 0

