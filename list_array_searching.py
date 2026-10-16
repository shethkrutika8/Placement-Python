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


'''# implement linear search

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
    '''


# #implement a binary search

# n = int(input("Entre the elements : "))
# list = []

# for i in range(n):
#     element = int(input(f"Entre the elements {i+1} : "))
#     list.append(element)

# list.sort()
# print("Sorted list", list)

# search = int(input("Entre the number you want to search : "))\

# low = 0
# high = n - 1
# found =  False

# while low <= high:
#     mid = (low + high) // 2

#     if list[mid] == search:
#         print("Element fount at index : ", i)
#         found = True
#         break
#     elif list[mid] <= high:
#         low = low + 1
#     else:
#         high = mid - 1

# if found  == False:
#     print("Element not found")

#remove a duplucate form the list 
'''
n = int(input("Entre the number : "))
list = []

for i in range(n):
    element = int(input(f"Entre the elements {i+1} : "))
    list.append(element)

print("Old list", list)

new_list = []

for i in range(n):
    if list[i] not in new_list:
        new_list.append(list[i])

print("New list : ", new_list)

'''

# # find common element in two lists

# n = int(input("Entre the number of arrays you want to entre in the list : "))
# list1 =[]

# for i in range(n):
#     element = int(input(f"Entre the element {i+1} : "))
#     list1.append(element)

# m = int(input("Entre the number added to array : "))
# list2 = []

# for j in range(m):
#     element = int(input(f"Entre the number {j+1} : "))
#     list2.append(element)

# common_element = []

# for i in range(n):
#     if list1[i]  in list2:
#         if list1[i] not in common_element:
#             common_element.append(list1[i])

# print("Common element", common_element)


'''#find the missing number from 1 to n:

n = int(input("Entre the number into list : "))
list = []

for i in range(n):
    element = int(input(f"Entre the number {i+1} : "))
    list.append(element)

for i in range(1, n+1):
    if i not in list:
        print("Missing number is : ", i)

'''

# #Move all zeros to the end

# n = int(input("Entre the list size : "))
# list = []

# for i in range(n):
#     element = int(input(f"Entre the number {i+1} : "))
#     list.append(element)

# print("Original list : ", list)

# result = []

# for i in range(n):
#     if list[i] != 0 :
#         result.append(list[i])

# for i in range(n):
#     if list[i] == 0:
#         result.append(list[i])

# print("Zero at the end : ",result) 

#count even and odd element


