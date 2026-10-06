# n  = int(input("Entre a number"))
# for i in range(n,0,-1):
#   for j in range(1, i+1):
#     print("*", end = "")
#   print()

'''
rectangle start pattern

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end="")
    print()
'''
'''
#print an right angle triangle pattern
n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1 , i+1):
        print("*", end="")
    print()
    '''

# #prit an inverted triangle

# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print()

# #Midddle inverted  triangle

# n = int(input("Entre a number: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for k in range(2*i-1):
#         print("*", end="")
#     print()
'''
# print a diamond pattern

n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range (n-1, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
'''


# #print a floyds triangle pattern

# n = int(input("Enter a number: "))
# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num += 1
#     print()

'''
# print a number trianle pattern

n = int(input("Enter a number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
    '''

# #print a hollow rectangle pattern

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print(" *", end="")
#         else:
#             print("  ", end="")
#     print()

'''
#print a multiplication table pattern

n = int(input("Entre a number: "))

for i in range(1,11):
    print(n, "*", i, "=", n*i)

    '''