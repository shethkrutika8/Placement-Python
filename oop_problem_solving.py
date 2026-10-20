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

# # Create a Student class with name and marks

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Student name : " , self.name)
#         print("Student marks : ", self.marks)

# s1 = student("Krutika", 99)
# s1.display()
 

'''# demosnstrate inheritance using the Manager and Employee


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name is : ", self.name)
        print("Salary is : ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def display_manager(self):
        self.display()
        print("Department is : ", self.department)

m1 = Manager("Krutika", 50000, "IT")
m1.display_manager()

'''

# #demonstrate method overriding

# class Student :
#     def display(self):
#         print("I am a student")

# class Teacher:
#     def display(self):
#         print("I am a teacher")

# s1 = Student()
# T1 = Teacher()

# s1.display()
# T1.display()

'''# Create a BankAccount class with deposite and withdraw
class BankAccount:
    def __init__(self, amount):
        self.amount = amount

    def deposite(self, deposite_amount):
        if deposite_amount > 0:
            self.amount = self.amount + deposite_amount
            print("Amount deposited succesfully!")
        else:
            print("Deposite amount must be positive.")


    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            print("Withdrawal amount must be positive.")
        elif withdraw_amount <= self.amount:
            self.amount = self.amount - withdraw_amount
            print("Amount withdraw succesfully!")
        else:
            print("Current Balance : ", self.amount)

    def display(self):
        print("Current Balance:", self.amount)

account = BankAccount(1000)

account.display()
account.deposite(500)
account.display()
account.withdraw(200)
account.display()'''

# #Handle division by zero using try-execept

# n1 = int(input("Entre the first number :"))
# n2 = int(input("Entre the second number:"))

# try:
#     result = n1/n2
#     print("Division = ", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by Zero!")
'''
#Read the text file and count word

file = open("IMP.txt", "r")
content = file.read()
words = content.split()
print("Total number of words :", len(words))
file.close()'''

# #. Create a dictionary of student marks and find the topper


# student = {
#     "Krutika" : 90,
#     "Dhruvisha" : 85,
#     "Upal" : 85,
#     "Milan" : 80
# }
# topper = max(student, key=student.get)
# print("Student Marks : ", student)
# print("Topper : ", topper)
# print("Highest Mark : ", student[topper])


#solve a two-sum problem using a dictinary

number = [2,7,11,15]
target = 9

seen = {}

for i in range(len(number)):
    required = target -number[i]

    if required in seen:
        print("Numbers:", required, "and", number[i])
        print("Indexes:", seen[required], "and", i)
        break
    seen[number[i]] = i