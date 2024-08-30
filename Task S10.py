# #Q.1
numbers = list(map(int, input('Enter numbers of numbers (comma-separated): ').split(',')))

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] >= numbers[j]:
            numbers[i], numbers[j] = numbers[j],numbers[i]
def second_largest(numbers: list[int]) -> int:
    pass
    secondLargest = 0
    largest = min(numbers)
 
    for i in range(len(numbers)):
        if numbers[i] > largest:
            secondLargest = largest
            largest = numbers[i]
    return secondLargest
print(f'Your second largest number is: {second_largest(numbers)}')
            




# # #Q.2
numbers =list(eval(input('enter numbers(comma-seperated): ')))
def missing_number(numbers: list[int]) -> int:
    pass
    max= numbers[0]
    for i in numbers:
        if i > max:
            max= i

    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i

    numbers2=[]

    for num in range(min + 1, max):
        if num not in numbers:
            numbers2.append(num)

    return numbers2

print(f'your missing number is: {missing_number(numbers)}')

# # #Q.3

numbers = list(eval(input('enter numbers(comma-seperated): ')))
target=int(input('Enter the number u want to see its index: '))
def number_of_occurences(numbers: list[int], target: int) -> int:
    pass
    occ=0
    first_index = -1
    last_index = -1
    for i in range(len(numbers)):
        if target== numbers[i]:
           occ += 1
        if numbers[i] == target:
            if first_index == -1:
                first_index = i
            last_index =i
    if occ<=0:
        print(f'The number {target} does not exist')
    else:
        print(f'number of occurences: {occ} , first index: {first_index} , last index: {last_index}')

number_of_occurences(numbers,target)

# #Q.4
numbers = list(eval(input('Enter list of numbers to know how many times it was rotated(comma-seperated): ')))
def rotated_sorted_array(numbers: list[int]) -> int:
    pass
    min = numbers[0]
    index = 0
    for i in range(0, len(numbers)):
        if min > numbers[i]:
            min = numbers[i]
            index = i
        
    return index
print(rotated_sorted_array(numbers))

















