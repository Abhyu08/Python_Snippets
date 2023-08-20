# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #Lists
    courses = ['History' , 'Math' , 'Science' , 'Physics']
    print(courses)
    print(len(courses))
    print(courses[1])

    #to print last item
    print(courses[-1])

    #slicing in lists
    print(courses[0:2]) #Here [2] is non-included
    print(courses[2:])

    #to add new values to our lists at the end of list
    courses.append('Art')
    print(courses)

    #to add value to specific location
    courses.insert(0,"Geography")
    print(courses)

    #adding lists under lists
    courses2 = ['Biology']
    courses.append(courses2)
    print(courses)

    #extending list
    courses2 = ['Biology3']
    courses.extend(courses2)
    print(courses)

    #remove value from lists
    courses.remove('History')
    print(courses)

    #pop(remove) value from last and print
    print(courses.pop())
    print(courses.pop())

    #sort the list
    courses.sort()
    print(courses)
    nums = [1 , 5, 9, 3, 8]
    nums.sort()
    print(nums)

    #reverse sort by actually changing the lists values
    nums.sort(reverse=True)
    print(nums)

    #sorting lists without changing the lists values
    sorted(nums)
    print(nums)
    print(sorted(nums))

    #using aggregate functions
    print(max(nums))
    print(min(nums))
    print(sum(nums))

    #to return index through search
    print(courses.index('Math'))

    print('Math' in courses) #if exists return true

    #to print lists index and values simultaneously
    for index,item in enumerate(courses):
        print(index, item)

    #splitting values and join them into a single string..
    courses_split_and_join = " - ".join(courses)
    print(courses_split_and_join)

    #split stirng with the help of delimiter
    new_list = courses_split_and_join.split(' - ')
    print(new_list)

    #tuples are same as lists but immutable(non-editabe) and declared with round brackets
    #becuase of that tuples has limited function it can work with.

    #syntax : tuple_name = ('','values...')

    #Sets - unordered
    #Sets - Unique
    #Syntax : set_course = { 'Math' , .... }
    #Between two sets we can use [intersection,difference,union] function


    #Empty Lists
    empty_lists = []
    empty_lists = list()

    #Empty Tuples
    empty_tuple = ()
    empty_tuple = tuple()

    #Empty Sets
    empty_set = {} #DOES NOT WORK - It Created Dict
    empty_set = set()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
