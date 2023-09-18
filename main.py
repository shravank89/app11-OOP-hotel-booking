from classes.hotel import Hotel
from classes.ticket import Ticket
from classes.card import CreditCard


hotel = Hotel("files/hotels.csv")

if hotel.check_availability():
    name = input("Enter the name of customer:")
    name = name.strip().title()
    card = input("Enter the credit card number:")
    expiry = input("Enter the credit card expiry in MM/YY:")
    cvc = input("Enter the credit card CVC: ")
    card_object = CreditCard(name, card, expiry, cvc)
    if card_object.validate():
        ticket = Ticket()
        print(ticket.print(name, hotel.hotel_name, hotel.hotel_city))
else:
    print("\nThis hotel is not free, try another")
    hotel = Hotel("files/hotels.csv")

