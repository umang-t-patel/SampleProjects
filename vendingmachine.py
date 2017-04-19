def function_main_menu(): # function for the main menu
	while True:
		print('-----------------------------------------')# Printing Main Menu
		print('Main Menu:')
		print('-----------------------------------------')
		print('[1] Drinks \n[2] Snacks \n[3] Exit')
		print('-----------------------------------------')
		main_menu_option = int(input('Select an option <3 to exit>: ')) # Input for the main menu option
		if main_menu_option == 1:
			function_drinks_menu() # Calling function for the drinks menu.
		elif main_menu_option == 2:
			function_snacks_menu() # Calling function for the snacks menu.
		elif main_menu_option ==3: # Exiting Main Menu and printing summary of the purchase.
			print('-----------------------------------------')
			print('Inserted amount: ', global_entered_amount,'| total purchase: ',global_total_amount_spend, '| change: ', global_total_amount_left,'\nGood Bye!!')
			print('-----------------------------------------')
			break;
		else:
			print('Invalid option!') # Options other then 1,2,3 then it will print an Invalid option message. 
def function_drinks_menu(): # function for the drinks menu
	while True:
		print('-----------------------------------------')# Printing Snacks Menu
		print('Drinks Menu:')
		print('-----------------------------------------')
		print('Water $0.75 \nJuice $0.99 \nSoda $1.39')
		print('-----------------------------------------')
		drinks_menu_option = input('Select a drink by entering the full name <X to exit to the main menu>\nDrink option: ')# Input for the drink option
		print('-----------------------------------------')
		if drinks_menu_option.lower() == 'water': # Using .lower(), if user provide input in any case.
			fuction_vending_item('Water',0.75)# Calling vending item function
		elif drinks_menu_option.lower() == 'juice':
			fuction_vending_item('Juice',0.99)
		elif drinks_menu_option.lower() =='soda':
			fuction_vending_item('Soda',1.39)
		elif drinks_menu_option.lower() =='x': # Exit and go back to main menu
			print('Exiting Drinks Menu')
			break;
		else:
			print('Invalid option!') # Options other then specified drinks menu then it will print an Invalid option message. 
def function_snacks_menu():# function for the snacks menu
	while True:
		print('-----------------------------------------')# Printing Snacks Menu
		print('Snacks Menu:')
		print('-----------------------------------------')
		print('Chips $0.99 \nPeanuts $0.5 \nGum $0.35')
		print('-----------------------------------------')
		snacks_menu_option = input('Select a snack by entering the full name <X to exit to the main menu>\nSnack option: ')# Input for the snack option
		print('-----------------------------------------')
		if snacks_menu_option.lower() == 'chips':# Using .lower(), if user provide input in any case.
			fuction_vending_item('Chips',0.99)# Calling vending item function
		elif snacks_menu_option.lower() == 'peanuts':
			fuction_vending_item('Peanuts',0.5)
		elif snacks_menu_option.lower() =='gum':
			fuction_vending_item('Gum',0.35)
		elif snacks_menu_option.lower() =='x': # Exit and go back to main menu
			print('Exiting Snacks Menu!!')
			break;
		else:
			print('Invalid option!')# Options other then specified snacks menu then it will print an Invalid option message. 
def fuction_vending_item(item,amount): 
# function for checking whether user have enough money to buy specified item
# if yes the provide the item and show the change, if no then display the message of not enough money
	global global_total_amount_left, global_total_amount_spend # Accessing the global variable.
	if amount < global_total_amount_left: #Check whether user has enough money to buy specified item
		global_total_amount_left = global_entered_amount - global_total_amount_spend - amount # calculate the amount left
		global_total_amount_spend = global_total_amount_spend + amount # calculate the amount spend
		print("Vending ",item,", you have ", global_total_amount_left," dollars left" )
	else:
		print("You don't have enough money to buy ",item,"[ ", global_total_amount_left, " < ",amount ," ]" )	
global_entered_amount = global_total_amount_left = global_total_amount_spend = 0.0 # Declaring the global variables
print('Welcome to the UB Vending Machine')
global_entered_amount = global_total_amount_left = int(input('Enter the number of nickels you wish to enter: ')) * 0.05 # input from user for number of nickels
print('You inserted ',global_entered_amount, ' dollars')
function_main_menu() # calling main menu function
