num1 = 11
num2 = num1         
# Doesn't really act as a pointer like C++. num2 becomes a reference to num1. 
# Therefor the value of num2 can change and will not affect num1 like a real pointer does.

print('Before num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

print('\nmemory addres of num1 :', id(num1))
print('\nmemory addres of num2 :', id(num2))

num2 = 22

print('\nAfter num2 value is updated:')
print('num1 =', num1)
print('num2 =', num2)

print('\nmemory addres of num1 :', id(num1))
print('memory addres of num2 :', id(num2))


########################################################
print('\n\n########################################')
########################################################

dict1 = {
    'value' : 11
    }

dict2 = dict1

print('\nBEFORE VALUE IS UPDATED:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))


dict2['value'] = 22     # Will act as a pointer, changing the value of dict1 as they're in the same address

print('\nAFTER VALUE IS UPDATED:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))




