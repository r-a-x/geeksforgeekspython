# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/
# Finding the minimum number formed from positive numbers

def solve(input):
    output = []
    if input[0] == 'I':
        output.append(1)
        output.append(2)
        last = 1
    if input[0] == 'D':
        output.append(2)
        output.append(1)
        last = 0
    next_elem = 3
    for i in range(1, len(input)):
        if input[i] == 'I':
            output.append(next_elem)
            next_elem = next_elem + 1
            last = i + 1
        else:
            #
            output.append(output[-1])
            next_elem = next_elem + 1
            for j in range(last, i+1):
                output[j] = output[j] + 1
    return output

input = "DDIDDIID"
print solve(input)
