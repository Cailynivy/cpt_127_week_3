
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.



# Problem 1: Write a program that takes a list of numbers and prints out the sum of all the numbers in the list.

def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [2,4,6,8,10]
print ("Sum", sum_of_list(numbers))

# Problem 2: Write a program that takes a list of numbers and prints out the average of all the numbers in the list.

def ave_of_list(numbers):
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)
numbers = (2,4,6,8,10)
average = ave_of_list(numbers)

print("Average", average)



# Problem 3: Write a program that takes a list of numbers and prints out the largest number in the list.

list = [2,4,6,8,10]
largest = max(list)
print("Largest", largest)