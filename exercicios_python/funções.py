def soma():
   
    num1 = input('Write one number: ')
    num2 = input('Write two number: ')

    float_num1 = float(num1)
    float_num2 = float(num2)

    resultado = (float_num1 + float_num2)

    return resultado

print(f'O resultado da soma é:',soma()) 
