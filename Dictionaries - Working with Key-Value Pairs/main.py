# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    #Dictonary
    #Syntax : { 'Key' : Value , ...}
    #value can be of any type [String, Integer , Float , Lists , ...]
    student = {'name' : 'John' , 'age' : 25 , 'courses' : ['Math' , 'Physics']}
    print(student)
    print(student['name'])
    print(student['courses'])

    #print(student['keydoesnotexist']) #it will throw err

    #so instead of that , use get() function
    print(student.get('age'))
    print(student.get('keydoesnotexist')) #returns None by default[no exception!]
    print(student.get('keydoesnotexist' , 'customMsgwhennotfound'))

    #updating & adding fields in Dictionary
    student['phone'] = '1234567890'
    student['name'] = 'Jane'
    print(student)

    #another simpler way of doing multiple updates in one shot
    student.update({'name' : 'Shane' , 'age' : 26 , 'phone' : '0987654321'})
    print(student)

    #removing key from Dictionary
    del student['age']
    print(student)
    name = student.pop('name') #delete the age key and return the value
    print(name)
    print(student)

    #dictionary usefull functions
    print(len(student))
    print(student.keys())
    print(student.items()) #print in pairs

    for key in student:
        print(key)

    for key , value in student.items():
        print(key , ' ' , value)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
