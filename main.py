from classes.hotel import Hotel
from classes.ticket import Ticket
from classes.card import SecureCreditCard


hotel = Hotel("files/hotels.csv")
while 1:
    if hotel.check_availability():
        name = input("\nEnter the name of customer:")
        name = name.strip().title()
        card = input("\nEnter the credit card number:")
        expiry = input("\nEnter the credit card expiry in MM/YY:")
        cvc = input("\nEnter the credit card CVC: ")
        user = input("\nEnter the username: ")
        password = input("\nEnter the password: ")
        card_object = SecureCreditCard(name, card, expiry, cvc, user, password)
        if card_object.validate():
            ticket = Ticket()
            print(ticket.print(name, hotel.hotel_name, hotel.hotel_city))
            break
        else:
            print("\nCard can not be validated, Transaction failed!")
            break
    else:
        hotel.hotel_id_choice = input("\nThis hotel is not free, try another: ")
