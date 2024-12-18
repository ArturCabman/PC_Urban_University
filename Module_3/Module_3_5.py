def get_multiplied_digits(numbers):
    str_number = str(numbers)
    first_digit = int(str_number[0])
    if len(str_number) > 1:

        return first_digit * get_multiplied_digits(int(str_number[1:]))

    elif first_digit == 0:
        return 1
    else:
        return first_digit
result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
