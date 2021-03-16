x=input("Enter number1: ")
y=input("Enter number2: ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
except TypeError as e:
    print('Type error exception')
    z = None
#below block is to find out the exception
except Exception as e:
    print(f'exception name -{type(e).__name__}')
    z = None
finally:
    print('''Code in finally will always execute.
    useful for resource clean up.
    Like when a file is in open state and code fails in between, 
    in that case File can be closed in Finally block''')

print("Division is: ", z)
