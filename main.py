from blockchain import Blockchain
from car_sharing import Owner, Car, Customer


def show_balance(cust_balance, owner_balance):
    print("Customer balance: %s" % (cust_balance,))
    print("Owner balance: %s" % (owner_balance,))

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    blockchain = Blockchain()
    val = input("Enter your value: ")
    val = int(val)
    customer = Customer(val)
    owner = Owner(500)
    eth = 50

    show_balance(customer.balance, owner.balance)

    #1
    owner.deploy(eth, blockchain)

    #2
    customer.request_book(eth, blockchain)

    #3
    
    print("1.Honda Civic/n2.Ford Focus/n3.Tesla Model S /n")
    vehicle = input("Choose your Vehicle (by entering the number):")
    days = input("Mention number fo days car needs to be rented:")
    if vehicle == "1":
     car = "Honda Civic"
     daily_price = 10
     days_no = int(days)
    elif vehicle == "2":
     car = "Ford focus"
     daily_price = 15
     days_no = int(days)
    elif vehicle == "3" :
        car = "Tesla Model X"
        daily_price = 20
        days_no = int(days)

      
    owner.add_car_to_rent(daily_price, car)
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

    show_rental_cost(daily_price*days_no)
    show_balance(customer.balance, owner.balance)


if __name__ == '__main__':
    start()
