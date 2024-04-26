print('Comparison of values.')
while True:
    num_one = input('Choose a number: ')
    num_two = input('Choose another number: ')
    try:
        float_num_one = float(num_one)
        float_num_two = float(num_two)
        if float_num_one > float_num_two:
            print('The firts number is greater than the second.')
            print(f'{float_num_one} > {float_num_two}')
            break
        elif float_num_two > float_num_one:
            print('The second number is grater than the first.')
            print(f'{float_num_two} > {float_num_one}')
            break
        elif float_num_one == float_num_two:
            print('The two numbers are equal.')
            print(f'{float_num_one} = {float_num_two}')
            break
    except ValueError:
        print('Unacceptable information.')
print('Fim')

