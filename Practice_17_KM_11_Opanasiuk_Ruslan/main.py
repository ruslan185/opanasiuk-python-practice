'''from factorial import factorial as f
from exp_root import exponentiation as exp, root
from logarithm import logarithm as log'''


from factorial import factorial as f
from exp_root import exponentiation as exp, root
import logarithm.logarithm as log


def get_int_bigger_zero(message):
    while True:
        try:
            x = int(input(message))
            if x <= 0 :
                raise Exception('num cannot be zero and less than zero')
            return x
        except Exception as e:
            print(e)

def get_int(message):
    while True:
        try:
            return int(input(message))
        except Exception as e:
            print(e)

def get_float_bigger_zero(message):
    while True:
        try:
            x = float(input(message))
            if x < 0 :
                raise Exception('num cannot be less than zero')
            return x
        except Exception as e:
            print(e)

def get_base_log(message):
    while True:
        try:
            x = float(input(message))
            if x <= 1 :
                raise Exception('num cannot be less than one')
            return x
        except Exception as e:
            print(e)


def menu():
    print(f'''
{'-'*25} MENU {'-'*25}

1) factorial value -> fac() 
2) value of squared number -> exp2() 
3) value of cubed number -> exp3() 
4) value of square root -> root2() 
5) value of cube root -> root3() 
6) value of logarithm -> log() 
7) value of natural logarithm -> ln() 
8) value of common logarithm -> lg()

EXIT -> all the rest''')
    
    while 1:

        test = int(input('''
Choose the number of function you would like to test: '''))
            
            
        if test == 1:
            number = get_int_bigger_zero('Enter a number for calculating factorial: ')
            print(f'Factorial value for {number} is: {f.fac(number)}')
            
        elif test == 2:
            number = get_int('Enter a number to square it: ')
            print(f'{number} squared is: {exp.exp2(number)}')

        elif test == 3:
            number = get_int('Enter a number to cube it: ')
            print(f'{number} cubed is: {exp.exp3(number)}')
            
        elif test == 4:
            get_float_bigger_zero('Enter a number to get a square root: ')
            print(f'The square root of {number} is: {root.root2(number)}')

        elif test == 5:
            get_float_bigger_zero('Enter a number to get a cube root: ')
            print(f'The cube root of {number} is: {root.root3(number)}')
            
            
        elif test == 6:
            base = get_base_log('Enter a base of logarithm: ')
            arg = get_float_bigger_zero('Enter an argument of logarithm: ')
            print(f'The logarithm with the base {base} and argument {arg} is: {log.log(base,arg)}')

        elif test == 7:
            arg = get_float_bigger_zero('Enter an argument of natural logarithm: ')
            print(f'The value of natural logarithm with argument {arg} is: {log.ln(arg)}')

        elif test == 8:
            arg = get_float_bigger_zero('Enter an argument of common logarithm: ')
            print(f'The value of common logarithm with argument {arg} is: {log.lg(arg)}')

        else:
            break


    return 'The program is over!'

print((menu()))

