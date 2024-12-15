def open_the_gate(number):
    password = list()
    digit = number + 1 // 2
    for i in range(1, digit):
        j = i + 1
        while i + j <= number:
            if number % (i + j) == 0:
                pass_numbers = str(i) + str(j)
                password.append(pass_numbers)
            j += 1
    return password
input_number = int(input('Input number: '))
print(open_the_gate(input_number))
#