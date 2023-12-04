digit_constants = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
def handle_stack(stack, number):
    if len(stack) < 2:
        stack.append(number)
    else: 
        stack.pop()
        stack.append(number)

def find_first_last_numbers(str):
    stack = []
    current_number = ""
    for char in str: 
        if char.isdigit(): 
            handle_stack(stack, char)
            current_number = ""
        else:
            current_number += char
            startwith = False
            for key in digit_constants.keys():
                if key.startswith(current_number):
                    startwith = True
                    if current_number in digit_constants:
                        handle_stack(stack, digit_constants[current_number])
                        current_number = char
                        break

            if not startwith:
                current_number = char
            
    if len(stack) == 2:
        print("".join(stack))
        return "".join(stack)
    print(stack[0] + stack[0])
    return stack[0] + stack[0]

def sum_of_calibration_values():
    with open("day_1_input.txt") as file:
        return sum([int(find_first_last_numbers(line.strip())) for line in file])

print(sum_of_calibration_values())
        

#how would i find the first and last numbrs in a string
# stack possibly?? 
# when do i pop with a stack?
# pop when i come across another number

#so I have these string constants that i need to find in the string
# what is the best way to find them in a string?
# i could use a dictionary to map them to their values
# then i could loop through the string and find them

#but that would take too much time
# i could use a stack to find them
# but how would I find them if ther're not digits but the start of the string of the number
