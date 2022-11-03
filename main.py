"""
Here we are importing the python packages we need and
also the csv file require to produce this program
"""

import csv
import re
import time
import pandas as pd

#Here is the set value of cart from the beginning of the project
Total=0
cart = ""

#Here we are reading the csv file
df = pd.read_csv("a-StarUniformData.csv")


#Here we added colours in our program to make a good user friendly program
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKRED = '\033[91m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Magenta = "\033[35m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    blue = '\033[94m'
    cyan = '\033[96m'
    red = '\033[91m'
    white = '\033[0m'
    bold = '\033[1m'
    purple = "\033[35m"
    header = '\033[95m'
    green = '\033[92m'
    yellow = '\033[93m'
    pink = '\033[95m'
    lightgrey = '\033[37m'

"""
here is our menu system which includes with three option for the customer,
Buy a product from A* Uniform, Book an appointment, see the prices of the products 
and finally exit the program 
"""





def main_menu(time=None):
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "1" + bcolors.OKCYAN, "]", bcolors.ENDC, "Buy a product")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "2" + bcolors.OKCYAN, "]", bcolors.ENDC, "Book an appointment")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "3" + bcolors.OKCYAN, "]", bcolors.ENDC, "See the prices")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "4" + bcolors.OKCYAN, "]", bcolors.ENDC, "Exit the program")

#here we add validation in our program 'try and accept'
    while True:
        try:
            choice = int(input(bcolors.BOLD + "" + bcolors.ENDC))
            if 0 < choice < 5:
                break
            else:
                print(bcolors.OKRED + "Please choose a number from 1-4" + bcolors.ENDC)
        except ValueError:
            print(bcolors.OKRED + "Please enter a number" + bcolors.ENDC)

# Here we created a personal detail information and customer email request

    if choice == 1:
        shop_product()
    if choice == 2:
        title = input('Please enter your title')
        first_name = input('Please enter your first name')
        last_name = input('Please enter your last name')
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#Here is the validation for user's email
#Also a conformation for the booking system and a date for the booking an appointment
#A receipt will be given to the customer
        while True:
            email = input("Please enter your e-mail \n>>")
            if (re.search(regex, email)):
                print("Valid Email")
                break
            else:
                print("Invalid Email")
        date = input('Please enter the date that is suitable for you (dd/mm/yyyy) : ')
        time = input('Please enter a suitable time for you using the 24h method')
        confirmation = input("Would you like to confirm your booking Y/N")
        if confirmation == "Y" or confirmation == "y":
            print("Here is a receipt for your measuring appointment")
            print("################Booking Details##############")
            print("Title: ", title)
            print("First Name: ", first_name)
            print("Last Name: ", last_name)
            print("Email: ", email)
            print("Date of appointment: ", date)
            print("Time of appointment: ", time)
#Here the booking times txt file is called to open


            file1 = open("booking-times.txt", "a")
            file1.write("Title:")
            file1.write(title)
            file1.write("\n")
            file1.write("First Name:")
            file1.write(first_name)
            file1.write("\n")
            file1.write("Last Name:")
            file1.write(last_name)
            file1.write("\n")
            file1.write("\n")
            file1.write("Email: /n")
            file1.write(email)
            file1.write("\n")
            file1.write("Date of appointment: ")
            file1.write(date)
            file1.write("\n")
            file1.write("Time of appointment: ")
            file1.write(time)
#Here is validation check if customer has accidental chose option for an appointment
#They don't want appointment the program brings them back to the main menu

        elif confirmation == "N" or confirmation =="n":
            main_menu()

#Here it gives the prices showing function
    if choice == 3:
        show_prices()
#Here is the exiting program function
    if choice == 4:
        print(bcolors.OKRED + "Exiting...." + bcolors.ENDC)
        time.sleep(0.5)
        exit()



"""
Here is where the products for the school is stored in a function
The set value is at 0 and will increase value when customer has purchase a product
"""

def shop_product():


    global subtotal, total
    subtotal = 0
    total = 0
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "1" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "2" + bcolors.OKCYAN, "]", bcolors.ENDC, "Secondary School")

#Here is the validation for the choices of primary and secondary school
    while True:
        try:
            choice = int(input(bcolors.BOLD + "" + bcolors.ENDC))
            if 0 < choice < 3:
                break
            else:
                print(bcolors.OKRED + "Please choose a number from 1-3" + bcolors.ENDC)
        except ValueError:
            print(bcolors.OKRED + "Please enter a number" + bcolors.ENDC)

# Here it shows the primary schools form A to D
    if choice == 1:
        print(bcolors.OKCYAN + "[" + bcolors.ENDC, "1" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School A")
        print(bcolors.OKCYAN + "[" + bcolors.ENDC, "2" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School B")
        print(bcolors.OKCYAN + "[" + bcolors.ENDC, "3" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School C")
        print(bcolors.OKCYAN + "[" + bcolors.ENDC, "4" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School D")
        primary_school_list = ["Primary School A", "Primary School B", "Primary School C", "Primary School D"]

# Validation
        while True:
            try:
                choice = int(input(bcolors.BOLD + "" + bcolors.ENDC))
                if 0 < choice < 5:
                    p_choice = primary_school_list[choice - 1]
                    break
                else:
                    print(bcolors.OKRED + "Please choose a number from 1-4" + bcolors.ENDC)
            except ValueError:
                print(bcolors.OKRED + "Please enter a number" + bcolors.ENDC)
# Here showing category of girls, boys and both products choice
        category_list = ["Girls", "Boys", "Both"]
        print(bcolors.cyan + "[" + bcolors.white, "1", bcolors.cyan + "]" + bcolors.white + "Girls")
        print(bcolors.cyan + "[" + bcolors.white, "2", bcolors.cyan + "]" + bcolors.white + "Boys")
        print(bcolors.cyan + "[" + bcolors.white, "3", bcolors.cyan + "]" + bcolors.white + "Accessories")
# Validation
        while True:
            try:
                category = int(input(
                    "Please choose what do you want to shop for from the list above\n>> " ))
                if 0 < category <= 3:
                    p_cat_choice = category_list[category - 1]
                    break
                else:
                    print(
                        bcolors.red + "Invalid input! \nPlease select a valid option from the menu above" + bcolors.white)
            except ValueError:
                print(bcolors.red + "Please select a valid *number* option from the menu above" + bcolors.white)

#Here we extracting the values of school and category to get type of product and price
#Then give option to user to select the product
#Giving option for the quantity
#Then Calculating total price

        extract = df.loc[(df['School'] == p_choice) & (df['Category'] == p_cat_choice)]
        extract.reset_index(drop=True, inplace=True)
        extract_col = extract[["Type", "Price"]]
        print(extract_col)
        item_index = input(
            "Select the index of the item you would like to buy e.g. 2\n>> " )
        item_choice = extract_col.iloc[[item_index]]
        print(item_choice)
        i_price = item_choice["Price"]
        float(i_price)
        print(bcolors.bold + "The price is £", float(i_price), bcolors.white)
        amount_item = input("Please enter the amount of items needed \n>> ")
        float(amount_item)
        subtotal = float(amount_item) * float(i_price)
        print("Subtotal is £", float(subtotal), )

# Option to buy another product or they can go to the checkout

        while True:
            print("\nWould you like to: ")
            print(bcolors.cyan + "[" + bcolors.white, "1", bcolors.cyan + "]" + bcolors.white + "Buy another item")
            print(bcolors.cyan + "[" + bcolors.white, "2", bcolors.cyan + "]" + bcolors.white + "Go to checkout")
            buy_again = input(">> ")

# Giving the list of product
# Validation
            if buy_again == "1":
                again = True
                break
            elif buy_again == "2":
                print("Go to checkout")
                print("Here is a list of your order")
                again = False
                break
            else:
                print("Please enter 1 or 2")
#Calculating total sum
        total += subtotal

        data = [[p_choice, p_cat_choice, item_choice["Type"].to_string(), item_choice["Price"].to_string(),
                 amount_item]]  # the data
#Opening customer data stored csv file
# Here we stored customer detail and previous order in the CSV file
        cust_file = open('customer.csv', 'a', newline='')
        writer = csv.writer(cust_file)
        writer.writerows(data)
        cust_file.close()
    cust_df = pd.read_csv("customer.csv")

    print(bcolors.pink + "Total £", total, bcolors.white)
    print(cust_df)
    print("=" * 50)

# Here is the secondary school products shop
    if choice ==2:
        again = True
        subtotal = 0
        total = 0
        while again:
            print(bcolors.cyan + "[" + bcolors.white, "1", bcolors.cyan + "]" + bcolors.white + "Secondary School A")
            print(bcolors.cyan + "[" + bcolors.white, "2", bcolors.cyan + "]" + bcolors.white + "Secondary School B")
            secondary_school_list = ["Secondary School A", "Secondary School B"]
# Validation
            while True:
                try:
                    s_index = int(input("Please choose a school from the list above" ))
                    if 0 < s_index <= 2:
                        s_choice = secondary_school_list[s_index - 1]
                        break
                    else:
                        print(
                            bcolors.red + "Invalid input!\nPlease select a valid option from the menu above." + bcolors.white)
                except ValueError:
                    print("Please select a valid *number* option from the menu above.")

# Category of the product boy or girl
            category_list = ["Girls", "Boys"]
            print(bcolors.cyan + "[" + bcolors.white, "1", bcolors.cyan + "]" + bcolors.white + "Girls")
            print(bcolors.cyan + "[" + bcolors.white, "2", bcolors.cyan + "]" + bcolors.white + "Boys")
# Validation
            while True:
                try:
                    category = int(input(">> "))
                    if 0 < category <= 2:
                        cat_choice = category_list[category - 1]
                        break
                    else:
                        print(
                            bcolors.red + "Invalid input!\nPlease select a valid option from the menu above" + bcolors.white)
                except ValueError:
                    print(bcolors.red + "Please select a valid *number* option from the menu above." + bcolors.white)

#Extract the headers from csv file 'school and category of products'
            extract = df.loc[(df['School'] == s_choice) & (df['Category'] == cat_choice), df.columns != "Code"]
            extract.reset_index(drop=True, inplace=True)
            extract_col = extract[["Type", "Price"]]
            print(extract_col)
            item_index = input(
                 "Select the index of the item you would like to buy e.g. 0 or 2\n>> ")
            item_choice = extract_col.iloc[[item_index]]
            print(item_choice)
            i_price = item_choice["Price"]
            print(bcolors.bold + "The price is £", float(i_price), bcolors.white)
            amount_item = input("Please enter the amount of items needed \n>> ")
            float(amount_item)
            subtotal = float(amount_item) * float(i_price)
            print("Subtotal is £", float(subtotal))

            while True:
                print("\nWould you like to: ")
                print(bcolors.cyan + "[" + bcolors.white, "1", bcolors.cyan + "]" + bcolors.white + "Buy another item")
                print(bcolors.cyan + "[" + bcolors.white, "2", bcolors.cyan + "]" + bcolors.white + "Go to checkout")
                buy_again = input(">> ")
                if buy_again == "1":
                    again = True
                    break
                elif buy_again == "2":
                    print("Checkout:")
                    again = False
                    break
                else:
                    print("Please enter 1 or 2")
            total += subtotal
            data = [[s_choice, cat_choice, item_choice["Type"].to_string(), item_choice["Price"].to_string(),
                     amount_item]]
            cust_file = open('customer.csv', 'a', newline='')
            writer = csv.writer(cust_file)
            writer.writerows(data)
            cust_file.close()
        cust_df = pd.read_csv("customer.csv")
#Here shows the receipt of purchase
        print( "Total £", total)
        print("Here is a list of the items you bought")
        print(cust_df)
        print("=" * 50)

"""
Showing the prices of the product in  function
"""


def show_prices():
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "1" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School A")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "2" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School B")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "3" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School C")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "4" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School D")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "5" + bcolors.OKCYAN, "]", bcolors.ENDC, "Primary School")
    print(bcolors.OKCYAN + "[" + bcolors.ENDC, "6" + bcolors.OKCYAN, "]", bcolors.ENDC, "Secondary School")

#Validation
    while True:
        try:
            choice = int(input(bcolors.BOLD + "" + bcolors.ENDC))
            if 0 < choice < 7:
                break
            else:
                print(bcolors.OKRED + "Please choose a number from 1-4" + bcolors.ENDC)
        except ValueError:
            print(bcolors.OKRED + "Please enter a number" + bcolors.ENDC)

    if choice ==1:
#reads primary school 1 csv file
        df = pd.read_csv("PR1.csv")
        print(df)
        main_menu()
    if choice == 2:
#reads primary school 2 csv file
        df = pd.read_csv("PR2.csv")
        print(df)
        main_menu()

    if choice == 3:
# reads primary school 3 csv file
        df = pd.read_csv("PR3.csv")
        print(df)
        main_menu()
    if choice == 4:
# reads primary school 4 csv file
        df = pd.read_csv("PR4.csv")
        print(df)
        main_menu()
    if choice == 5:
# reads secondary school 1 csv file
        df = pd.read_csv("SR1.csv")
        print(df)
        main_menu()
    if choice == 6:
# reads secondary school 2 csv file
        df = pd.read_csv("SR2.csv")
        print(df)
        main_menu()


main_menu()


