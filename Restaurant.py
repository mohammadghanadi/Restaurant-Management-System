# -*- coding: utf-8 -*-
import csv

__author__ = "8422130, Kulikovskyi, 8157153, Ghanadi"


class Products:
    """
    Save the Classe Products class and its attributes
    Parameters:
    name(str): The name of the Product
    typ(str): The Catagory of the product
    catagorie(str): The catagorie of the Product
    price(int): the price of the produkt
    """
# The __init__ method initializes the properties of the Products class
    def __init__(self, name, typ, categorie, price):
        self.name = name
        self.typ = typ
        self.categorie = categorie
        self.price = price


class Main_menu:
    """
    The main class of the programm. Managing the menu functions:

    load_produkts: Load the food menu from the saved storage.
    programm_flow: User interface. show the user the information and take the inputs.
    order_input: Take the orders from user.
    order_show: write a summary of orders at the console.
    get_bill : show the bill for each table in console.
    """

    def __init__(self):
        # create an empty dictionary to save the tables in it.
        self.tables_in_restaurant = {}
        # save the products in the list prodkts_list.
        self.products_list = self.load_products("/Users/mohammadghanadi/Documents/Uni/wintersemester24:25/EPR/Übung/Abgabe/ÜB7.Gruppe/food/food.csv")

    def load_products(self, file_name):
        """
        Load Products from a CSV file.
        Parameters:
        file_name(str): The path of the CSV file containing the products
        
        Returns:
        list: A list of Products objects loaded from the CSV file.
        Raises:
        FileNotFoundError: If the specified file does not exist.
        """
        products_list = []
        try:
            # open the file in read mode with UTF-8 encoding.
            with open(file_name, mode="r", encoding="utf-8") as file:
                # Create a CSV reader object with semicolon as delimiter
                reader = csv.reader(file, delimiter=";")
                
                # Skip the header row
                next(reader, None)
                
                # Iterate over each row in the CSV file
                for el in reader:
                    # Check if the row has the expected number of elements
                    if len(el) == 4:
                        # Extract the product details from the row
                        name, typ, categorie, price = el
                        # Create a new Products object and add it to the list
                        products_list.append(Products(name, typ, categorie, price))
                    else:
                        # Skip malformed lines (like the total bill lines at the end)
                        continue
        except FileNotFoundError:
            # print an errorr massage if the file is not found
            print("File mit Produkten wurde nicht gefunden")
            # Return the list of loaded products
        return products_list

    def programm_flow(self):
        # to divide each part with a line.
        print("-"*100)
        print("Willkommen zum Restaurant")
        while True:
            print("-"*100)
            print("1-Bestellung eingeben")
            print("2-Bestellung anzeigen")
            print("3-Rechnung")
            print("0-Restaurant verlassen")
            try:
                eingabe = int(input("Wählen Sie eine Aktion:"))

                # Give the order using input 1.
                if eingabe == 1:
                    self.order_input()
                # show the order using input 2.
                elif eingabe == 2:
                    self.order_show()
                # show the bill using input 3.
                elif eingabe == 3:
                    self.get_bill()
                # nothing else required using input 0.
                elif eingabe == 0:
                    print("Danke für den Besuch, kommen Sie wieder!")
                    break
            except ValueError:
                print("Ungültige Eingabe, bitte eine Zahl wählen.")

    def order_input(self):
        """
        This method creates the order for a table.
        """
        # Try-except block to avoid errors during input
        try:
            # Creation of tables.
            table_number = int(input("Gegen Sie Tischnummer ein:"))
            # create a new Table_number if it doesent already exist.
            if table_number not in self.tables_in_restaurant:
                self.tables_in_restaurant[table_number] = Table(table_number)

            print("-"*100)
            print("Produkte in der Lage:")
            # output of all products in food_list with their characteristics in numbered order.
            for el, product in enumerate(self.products_list):
                print(el, product.name, ":", product.typ, ",", product.categorie, ",", product.price)
            
            # While loop for multiple inputs of the product.
            while True:
                print("-"*100)
                print("Geben Sie Nummer des Produkts ein: ")
                print("Geben Sie -1 ein, um Bestellung beenden: ")
                select_product = int(input())
                if select_product != -1:
                    if 0 <= select_product < len(self.products_list):
                        # If the number matches,select the corresponding product
                        product = self.products_list[select_product]

                        print("Haben Sie Sonderwünsche, wie extra Käse oder kein?")
                        # Input for special requests.
                        wish = str(input())
                        
                        # Use a temporary variable for price to avoid changing the original product price in the list
                        current_price = float(product.price.replace(',', '.'))
                        
                        # If the string contains the part "extra", it counts as special requests.
                        if "extra" in wish.lower():
                            current_price += 1.0

                        # Create a copy or a representation to store in the table
                        # For simplicity, we create a new Product instance with the new price for this specific order
                        ordered_product = Products(product.name, product.typ, product.categorie, str(current_price))
                        ordered_product.wish = wish # Store the wish
                        
                        # Add the already edited product(with special requests) to the current table.
                        self.tables_in_restaurant[table_number].order_per_table(ordered_product)
                        print(ordered_product.name, "(Sonderwünsche:", wish, ") wurde zur Bestellung hinzugefügt")
                    else:
                        print("Produkt wurde nicht gefunden!")
                else:
                    print("Bestellung ist geschloßen")
                    break

        except ValueError:
            print("Ungültige Eingabe")
    
    def order_show(self):
        """"
        This method displays all orders made by the selected table.
        The user can edit the order.
        If the order is empty, the table will be cleared(deleted).
        """
        # Try-except block to avoid errors during input.
        try:
            # Search for the selected table, if it exists.
            table_number = int(input("Gaben Sie Tischnummer ein:"))
            if table_number in self.tables_in_restaurant:
                table = self.tables_in_restaurant[table_number]
                # Call the method show_order_per_table() for the current table.
                list_in_table = table.show_order_per_table()
                # We return the value True in list_in_table if the order is empty, \
                # to delete the current table, if the order of table empty is
                if list_in_table:
                    self.tables_in_restaurant.pop(table_number)
            else:
                print("Tisch wurde nicht gefunden")
        except ValueError:
            print("Ungültige Eingabe")

    def get_bill(self):
        """
        This method creates a bill for a table.
        """
        # Try-except block to avoid errors during input.
        try:
            # Search for the selected table, if it exists.
            table_number = int(input("Geben Sie Tischnummer ein:"))
            if table_number in self.tables_in_restaurant:
                table = self.tables_in_restaurant[table_number]
                # Call the method bill_per_table() for the current table.
                table.bill_per_table()
                # Removes an already served table from the tables list
                self.tables_in_restaurant.pop(table_number)
            else:
                print("Tisch wurde nicht gefunden")
        except ValueError:
            print("Ungültige Eingabe")


class Table:
    """
    Class Table represents an object used as a table in a restaurant. \
    Parameters:
    table_number(int): number of each table
    orders_from_table(list): for all orders from table
    """
    def __init__(self, table_number):
        """
        This method initializes the table number and a list of al l orders for the table.  
        """
        # Create variables, such as table number and list of orders, for the current class Table.
        self.table_number = table_number
        self.orders_from_table = []

    def order_per_table(self, order):
        """
        This method creates a list of all orders from the table.
        """
        # Add already edited product(with special requests) to list of orders for the current table.
        self.orders_from_table.append(order)

    def show_order_per_table(self):
        """
        This method displays all orders that the selected table has already made.
        The user can edit the order and remove products.
        """
        print("Bestellung für Tisch:", self.table_number)
        # Execution of all orders for the current table.
        for el, product in enumerate(self.orders_from_table):
            print(el + 1, product.name, ":", product.typ, ",", product.categorie, ",", product.price)

        # While loop to edit the order.
        run = True
        while run:
            print("Wollen Sie ein Produkt entfernen? Wählen Sie Nummer(0 um Entfernung zu beenden)")
            try:
                remove = int(input())
                # Variable 'remove' to end the editing process.
                if remove == 0:
                    run = False
                    break
                
                if 1 <= remove <= len(self.orders_from_table):
                    self.orders_from_table.pop(remove - 1)
                    
                    # If the order becomes empty during editing, the table will be cleared (deleted).
                    if not self.orders_from_table:
                        print("Die Bestellung wurde gelöscht")
                        return True
                        
                    print("Aktuelle Bestellung:")
                    for el, product in enumerate(self.orders_from_table):
                        print(el + 1, product.name, ":", product.typ, ",", product.categorie, ",", product.price)
                else:
                    print("Ungültige Nummer.")
            except ValueError:
                print("Bitte eine Zahl eingeben.")

    def bill_per_table(self):
        """
        This method creates a bill for each table.
        """
        total_sum = 0
        # For loop to calculate the sum of all orders for the current table.
        for product in self.orders_from_table:
            # Handle possible comma in price string
            price_val = float(product.price.replace(',', '.'))
            total_sum += price_val
            
        # Try-except block to avoid errors while searching for a file to save the invoice.
        try:
            # Add bills to file.
            with open("/Users/mohammadghanadi/Documents/Uni/wintersemester24:25/EPR/Übung/Abgabe/ÜB7.Gruppe/food/food.csv", mode="a", encoding="utf-8") as file:
                output_str = "\nDie Rechnung für Tisch №" + str(self.table_number) + ":" + str(total_sum)
                file.write(output_str)

        except FileNotFoundError:
            print("CSV Datei nicht gefunden zum Speichern der Rechnung.")
            
        print("-"*100) 
        print("Rechnung für Tisch", self.table_number, ":", total_sum)
        return total_sum


if __name__ == "__main__":
    # Main programm:
    programm = Main_menu()
    programm.programm_flow()
