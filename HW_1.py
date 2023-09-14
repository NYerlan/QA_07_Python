# print('Hello, World!')
#
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2nd number: '))
# result = num1 + num2
# print('Result: 1st number + 2nd number = ' + str(result))
# result = num1 - num2
# print('Result: 1st number - 2nd number = ' + str(result))
# result = num1 * num2
# print('Result: 1st number * 2nd number = ' + str(result))
# result = num1 / num2
# print('Result: 1st number / 2nd number = ' + str(result))
# result = num1 // num2
# print('Result: 1st number // 2nd number = ' + str(result))
# result = num1 ** num2
# print('Result: 1st number ** 2nd number = ' + str(result))
# result = num1 % num2
# print('Result: 1st number % 2nd number = ' + str(result))

# print('*********')
# print('*       *')
# print('*       *')
# print('*********')
#
num1 = int(input('Enter 4 digit number: '))
thousands = num1 // 1000
hundreds = num1 % 1000 // 100
decades = num1 % 100 // 10
digits = num1 % 10
print(f'Thousands: {thousands}')
print(f'Hundreds: {hundreds}')
print(f'Decads: {decades}')
print(f'Digits: {digits}')
