def add (x,y):
    return (x+y)
def subtract(x,y):    
    return (x-y)
def multiply(x,y):
    return(x*y) 
def divide(x,y):
    return(x/y)

print('select operation' )
print('select 1 to add')
print('select 2 to subtract')
print('select 3 to multiply')
print ('select 4 to divide')

while True:
    choice=input('enter choice 1/2/3/4:')
    if choice in ('1','2','3','4'):
        num1=float(input('enter first number:'))
        num2=float(input('enter second number:'))

        if choice=='1':
            print ('result:', add (num1,num2))
        if choice=='2':
            print ('result:', subtract( num1,num2)) 
        if choice=='3':
            print ('result:', multiply(num1,num2)) 
        if choice=='4':
            print ('result:' ,divide(num1,num2)) 

            break
        else:
            print("invalid input")         
