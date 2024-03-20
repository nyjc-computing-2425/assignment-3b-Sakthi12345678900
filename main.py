stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
new_form = stdform.replace('x10^', 'E')
print('This number in E notation is',new_form + '.')