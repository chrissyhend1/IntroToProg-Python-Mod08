# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# CHenderson,12.4.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
file_name = 'products.txt'
lstOfProductObjects = []
strStatus = ""  # Captures the status of an processing functions

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products'  name
        product_price: (float) with the products' standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CHenderson,12.4.2020,Modified code to complete assignment 8
    """
    #--Fields--
    str_product_name = ""
    str_product_price = ""

    #--Constructor--
    def __init__(self, product_name='', product_price=''):
        #--Attributes--
        self.__product_name = product_name
        self.__product_price = product_price

    #--Properties--
    # Product Name
    @property
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):  # (setter or mutator)
        if str(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Numbers cannot be letters")

    #--Methods--
    def to_string(self):
        """ Converts product data to a string value"""
        return self.__str__()

    def __str__(self):
        """Converts product name to a string"""
        return self.product_name + "," + str(self.product_price)

# End of Class

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        CHenderson,12.4.2020,Modified code to complete assignment 8
    """

    #--Fields--

    #--Methods--
    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Removes data from user input into a list as a dictionary row

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want the task removed from:
        :return: (list) of dictionary rows
        """
        strFile = open(file_name, "w")
        for row in list_of_rows:
            strFile.write(str(row["Product"]) + ',' + str(row["Price"] + "\n"))  # Write data to text file
        strFile.close()  # Close text file
        print("Data saved to file!")
        return list_of_rows, 'Success'


    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            strProduct, strPrice = line.split(",")
            dicRow = {"Product": strProduct.strip(), "Price": strPrice.strip()}
            list_of_rows.append(dicRow)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(product, price, list_of_rows):
        """ Adds data from user input into a list as a dictionary row

        :param product: (string) product you want added to file:
        :param price: (string) price of the product:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.append({"Product": product, "Price": price})
        return list_of_rows, 'Success'

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Processes input data for use in the program
    methods:
        print_menu_Products():
        input_menu_choice():
        print_current_Products_in_list(list_of_rows):
        input_yes_no_choice(message):
        input_press_to_continue(optional_message=''):
        input_new_task_and_priority():

    changelog: (When,Who,What)
        CHenderson,12.4.2020,Added code to complete assignment 8
     """

    #--Methods--
    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File        
        3) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(list_of_rows):
        """ Shows the current Products in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products and prices in the list are: *******")
        for row in list_of_rows:
            print(str(row["Product"]).title() + " $" + row["Price"])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets a new task and new priority input from the user

        :return: (string)
        """
        strProduct = input("Please enter a product: ")  # Accept user input of a task
        strPrice = input("Please enter a price: ")  # Accept user input of a priority
        print()
        return strProduct, strPrice

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.read_data_from_file(file_name, lstOfProductObjects)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_Products()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Product
        strProduct, strPrice = IO.input_new_task_and_priority()
        strProduct, strPrice = FileProcessor.add_data_to_list(strProduct, strPrice, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.write_data_to_file(file_name, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '3':  # Exit Program
        print("Goodbye!")
        break  # and Exit

input()