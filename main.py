from blockchain import Blockchain
from car_sharing import Owner, Car, Customer


def show_initial_balance(cust_balance, owner_balance):
    print("Initial Customer balance: %s" % (cust_balance,))
    print("Initial Owner balance: %s\n" % (owner_balance,))

def show_final_balance(cust_balance, owner_balance):
    print("Balance after transaction for Customer: %s" % (cust_balance,))
    print("Balance after transaction for Owner: %s\n" % (owner_balance,))


def start():
    blockchain = Blockchain()
    customer = Customer(500)
    owner = Owner(500)
    eth = 50

    show_initial_balance(customer.balance, owner.balance)

    #1
    owner.deploy(eth, blockchain)

    #2
    customer.request_book(eth, blockchain)

    #3
    user = input("Are you a 1. Owner or 2. Customer (Enter 1 or 2):" )
    days = input("Mention number for days car needs to be rented:")

    if user == 2:  
        x = "yes"
        while (x == "yes") :  
           print("Enter Car details : ")  
           car = input("Enter your car name:" ) 
           daily_price  = input ("Enter rent of car per day:"  )  
           owner.add_car_to_rent(daily_price, car)
           x = input( " Do you wanna add more car, yes or no : ")

    elif user == 1:
         print("1.Honda Civic \n2.Ford Focus\n3.Tesla Model S \n")
         vehicle = input("Choose your Vehicle (by entering the number):")
         
         
         if vehicle == "1":
            car = "Honda Civic"
            daily_price = 10
            days_no = int(days)
         elif vehicle == "2":
             car = "Ford Focus"
             daily_price = 15
             days_no = int(days)
         elif vehicle == "3" :
             car = "Tesla Model X"
             daily_price = 20
             days_no = int(days)
         else:
             print("Currently no more cars are available for rent. Sorry for the inconvinence")
         owner.add_car_to_rent(daily_price, car)
         print("Details of car selected being added to smart contract" ,owner.add_car_to_rent)
         customer.pass_number_of_days(days_no)

    #4
         owner.encrypt_and_store_details(blockchain)
         owner.allow_car_usage()
    

    #5
         customer.access_car()

    #6
         customer.end_car_rental()

    #7
         owner.withdraw_earnings()
         customer.retrieve_balance()

         def show_rental_cost(cost):
          print("Rental cost of ", car ,"for " ,days, "days:", cost)

         show_rental_cost(daily_price*days_no)
         show_final_balance(customer.balance, owner.balance)


if __name__ == '__main__':
    start()
