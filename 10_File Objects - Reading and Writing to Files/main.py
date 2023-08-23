# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#File Objects
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    ######## READING Examples #######
    #using context managers
    with open('text.txt','r+') as cm:

        #to print whole at once
        print(cm.read())
        cm.seek(0) # reset the cursor at starting position...
        #to print specific amount of characters..
        print(cm.read(10))
        print('tell - ', cm.tell())
        cm.seek(0) # reset the cursor at starting position...
        print(cm.readline()) #Every time we use it will read next line
        cm.seek(0) # reset the cursor at starting position...
        print(cm.readlines() , end='')
        print(cm.mode)

        #print multiple lines using loop:
        cm.seek(0) # reset the cursor at starting position...
        print('#print multiple lines using loop')
        for line in cm:
            print(line,end=' ')
        cm.close()  # IMP : to explicitly close the file

        #to print data in chunks(till selected length) each time:
        with open('text.txt','r+') as cm:
            size_to_read = 100
            file_contents = cm.read(size_to_read)
            print('\nprint contents in chunks...')
            while len(file_contents) > 0 :
                print(file_contents)
                print('tell -: ', cm.tell())
                file_contents = cm.read(size_to_read)
        cm.close()

    #File Methods & Objects
    f = open('text.txt','r+')
    print(f.read())
    print(f.mode)
    f.close()   #IMP : to explicitly close the file


    ######## WRITING Examples #######
    with open('text2.txt','w') as rf:
        rf.write('Test')
        rf.seek(0)
        rf.write('R')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
