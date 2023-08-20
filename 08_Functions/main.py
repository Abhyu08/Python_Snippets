# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#function #DRY - Don't Repeat Yourself
def hello_func():
    print('Inside the function!')
    return 'returned value from func.'

def greet_user(message , prefix='.'):
    return 'welcome {} to IDE{}'.format(message,prefix)

#another way of declaring functions...
def student_info(*args , **kwargs):
    print(args) #becomes tuples
    print(kwargs) #becomes dictionary

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #basic calling to func.
    hello_func()
    print(hello_func )

    print(hello_func())
    print(hello_func().upper().lower())

    #calling with args.
    print(greet_user('Sam','!'))

    student_info('Math','Art','Bio',name='Sam',age='25')

    #if we pass directly these type of value then...
    courses=['Math' , 'Art']
    info = {'name':'John' , 'age':22}
    student_info(courses,info)

    #if we are intentionally mention which are who
    student_info(*courses,**info)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
