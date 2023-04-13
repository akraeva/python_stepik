num1 = float(input())
num2 = float(input())
operation = input()

if operation == '+' :
    print (num1 + num2)
elif operation == '-' :
    print (num1 - num2)
elif operation == '*' :
    print (num1 * num2)
elif operation == 'pow' :
    print (num1 ** num2)
elif num2 == 0 and (operation == '/' or operation == 'mod' or operation == 'div'):
    print ('Деление на 0!')    
elif operation == '/'  :
    print (num1 / num2)
elif operation == 'mod' :
    print (num1 % num2)
elif operation == 'div' :
    print (num1 // num2)