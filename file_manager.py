import os.path
import os
import shutil
import sys
from def_file_manager import *


while True:
    print('1. Add new folder')
    print('2. Del file/folder')
    print('3. Copy file/folder')
    print('4. View directory')
    print('5. View folder')
    print('6. View file')
    print('7. View sys')
    print('8. Creator')
    print('9. Play quiz')
    print('10. Balance')
    print('11. Change directory')
    print('12. Exit')

    choice = input('Choice item: ')
    if choice == '1':
        def choice1():
            new_folder = input('Name new folder: ')
            for i in range(1):
                if not os.path.exists(new_folder):
                    os.makedirs(new_folder)
            return new_folder
        choice1()
        pass

    elif choice == '2':
        del_folder = input('Name of del folder/file: ')
        os.rmdir(del_folder)
        pass

    elif choice == '3':
        copy_folder = input(' What folder/file your copy?: ')
        new_folder_copy = input('Name your copy')
        shutil.copy(copy_folder, new_folder_copy)
        pass

    elif choice == '4':
        choice4()
        pass

    elif choice == '5':

        choice5()
        pass

    elif choice == '6':
        # print(glob.glob('C:\\Users\\User\\PycharmProjects\\python educations\\education_Start_with_lesson5\\*.*'))
        # print(glob.glob('C:\\Users\\User\\PycharmProjects\\python educations\\education_Start_with_lesson5\\.*'))

        with os.scandir(path='.') as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    print(entry.name)
                pass
        pass

    elif choice == '7':
        print(sys.platform)
        pass
    elif choice == '8':
        choice8('Beluncho')
        pass
    elif choice == '9':
        import vyctory_new
        vyctory_new.victory_new()
        pass
    elif choice == '10':
        import use_function
        use_function.balance_fun()
        pass
    elif choice == '11':
        import os
        directory = os.getcwd()
        print(directory)
        os.chdir(input('new directory: '))
        directory = os.getcwd()
        print(directory)
    elif choice == '12':

        break
