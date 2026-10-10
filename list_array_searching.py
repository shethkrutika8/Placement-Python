# #find the maximum and minimum number in the list

# num = int(input("Entre the elements if the list you want to add : "))
# list = []

# for i in range(num):
#     element = int(input(f"Entre the number {i+1} : "))
#     list.append(element)

# maximum = list[0]
# minimum = list[0]

# for i in range(1, len(list)):
#     if list[i] > maximum:
#         maximum = list[i]
#     elif list[i] < minimum:
#         minimum = list[i]

# print(f"Maximum number in the list is : {maximum}")
# print(f"Minimum number in the list is : {minimum}")
'''
#find thee second largest element in the list

num = int(input("Entre thr element of the list you eant to add into the list : "))
list = []

for i in range(num):
    element = int(input(f"Entre the number {i+1} : "))
    list.append(element)

maximum = list[0]
second_maximum = list[0]

for i in range(1, len(list)):
    if list[i] > maximum:
        second_maximum = maximum
        maximum = list[i]

    elif list[i] > second_maximum and list[i] != maximum:
        scond_maximum = list[i]

print(f"Maximum number in the list is : {maximum}")
print(f"Second maximum number in the list is : {second_maximum}")'''

# #find the sum and the average of the list

# num = int(input("Entre the element of the list you want to entre in the list : "))
# list  = []

# for i in range(num):
#     element = int(input(f"Entre the number {i+1} : "))
#     list.append(element)

# sum = 0
# for i in range(len(list)) :
#     sum += list[i]

# print(f"Sum is : {sum}")

# average = sum / list[i]
# print(f"Average is {average}")
'''
# sort a list without a list 

n = int(input("Entre the number : "))
list = []

for i in range(n):
    element = int(input(f"Entre the number {i+1} : "))
    list.append(element)

for i in range(n):
    for j in range(0, n-i-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print("Sorted Array : ", list)

    
'''

# #implement a buuble sort 

# n = int(input("Entre the number : "))
# list = []

# for i in range(n):
#     element  = int(input(f"Entre the number : {i+1}"))
#     list.append(element)

# for i in range(n):
#     for j in range(0, n-i-1):
#         if list[j] > list[j+1]:
#             temp = list[j]
#             list[j] = list[j+1]
#             list[j+1] = temp

# print("sorted array : ", list)


# implement linear search

n = int(input("Entre the number : "))
list = []

for i in range(n):
    element = int(input(f"Entre the number {i+1} : "))
    list.append(element)

search = int(input("Entre the number you want to search : "))

found = False

for i in range(n):
    if list[i] == search:
        print("Element found at index : ", i)
        fount = True
    

