import os
import json
import classes
import time
import globals
import create_functs
import general_functs
import delete_functs
import list_functs

def main_menu():
    while(True):
        print(f'''        Current Region:{globals.region}



        1: Create new infrastructure
        2: List infrastructure
        3: Delete infrastructure
        4: Change region
        5: Apply
        6: Exit
        ''')
        option = int(input('Select an option: '))
        if option == 1:
            create_functs.create_infrastructure()
        elif option == 2:
            list_functs.list_infrastructure()
        elif option == 3:
            delete_functs.delete_infrastructure()
        elif option == 4:
            general_functs.clear_terminal()
            globals.change_region()
            print(f'Region Changed to {globals.region}')
            time.sleep(1)
        elif option == 5:
            general_functs.apply_changes()
            input('\nYour infrastructure is now running on AWS! Press any Key to continue editing.')
        elif option == 6:
            general_functs.clear_terminal()
            return 1       
        else:
            input('Invalid option, press any key to continue.')
            general_functs.clear_terminal()
        general_functs.clear_terminal()


def main():
    while(True):    
        globals.initialize()
        general_functs.clear_terminal()
        status = main_menu()
        if status == 1:
            return

if __name__=="__main__":
    main()
    