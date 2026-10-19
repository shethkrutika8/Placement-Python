# #write a function to check the prime number 

# n = int(input("Entre the number : "))

# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print("Prime Number")
#             break
#     else:
#         print("Not a prime Number")

# #with the function call

# def check_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Entre a Number : "))

# if check_prime(n):
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


'''# Find factorial using recursion

def find_factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)

num = int(input("Enter the number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {find_factorial_recursive(num)}")

'''

#create a student class with the name and marks

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name : ", self.name)
        print("Student mark : ", self.marks)

s1.stuent("Krutika", 90)

s1.dispaly()


