# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    os.chdir("C:/Users/wd980804/Documents/Python/Lessons files")
    print(os.getcwd())
    
    #to rename the file_name by rearranging it based on our needs...
    for item in os.listdir():
        if item[-3:] == 'txt':
            f_name , f_ext = item.split('.')
            f_planet , f_solar , f_num = f_name.split('-')
            file_name = '{}-{}-{}.{}'.format(f_num[2:].strip().zfill(2),f_solar.strip(),f_planet.strip(),f_ext)
            os.rename(item,file_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
