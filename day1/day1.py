#from Daily Coding Problem

#problem1
"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""

list1=input("Enter a sequence of numbers separated by commas")
list=[float(number)for number in list1.split(",")]
test_value=float(input("Enter  a test value"))
for i in range(len(list)):
    for j in range(len(list)-i):
        if list[i] + list[j] == test_value:
            print("true")
        
            
    




