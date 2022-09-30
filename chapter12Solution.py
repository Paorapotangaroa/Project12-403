# Write the program that prompts the user to enter in the customer and account information. 
# Load up the instance variables by calling constructors and methods. 
# Then call the print_customer() method to display the customer information.

# Name: Toa Pita
# Section: 003
# Project Description: This program allows the user to enter information for different customers. It then displays the processed information.

# Bring in the class files
from classes12 import Customer

# Gather input
name = input("\nWhat is the name of the customer? ")
address = input("\nWhat is the street address of the customer? ")
city = input("\nWhich city does the customer live in? ")
state = input("\nwhich state does the customer live in? ")
zipCode = input("\nWhat is the customer's zipcode? ")
balance = float(input("\nWhat is the balance for the customer? "))
# What even is the following question? I asked it because the video did but I didn't understand this
# variable or even why we have it short of testing to see if we can work with multiple datatypes
# in our classes
numEmploy = int(input("\nEnter the number of employees in Customer: "))

# Create customer
cust1 = Customer(name,address,city,state,zipCode,numEmploy)
# Access customers account
cust1.get_account().set_balance(balance)

# Print the final result
print("\n"+cust1.print_customer())
