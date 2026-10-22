# n = int(input())
# for i in range(1,n):
#     for j in range(1,n):
#         print("*", end="")
#     print()

# *****
# *****
# *****
# *****

'''
n  = int(input())
for i in range(1, n):
    for j in range(1, i+1):
        print("*", end="")
    print()

*
* *
* * *
* * * *'''

# n = int(input())
# for i in range(n, 0 , -1):
#     for j in range(0, i-1):
#         print("*", end="")
#     print()

# * * * *
# * * *
# * *
# *
'''
n = int(input())
for i in range(1, n):
    for j in range(1, i+1):
        print(j, end="")
    print()
1
1 2
1 2 3
1 2 3 4'''

# n = int(input())
# num = 1
# for i in range(1, n):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()

# 1
# 22
# 333
# 4444

n = int(input())
for i in range(1, n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(1, i*2):
        print("*", end="")
    print()