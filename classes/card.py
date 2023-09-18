import pandas as pd


class CreditCard:
    def __init__(self, name, card, expiry, cvc):
        self.name = name.upper()
        self.card = card
        self.expiry = expiry
        self.cvc = cvc
        self.df = pd.read_csv("files/cards.csv", dtype=str)

    def validate(self):
        customer_tuple = (self.card, self.expiry, self.cvc, self.name)
        list_of_cards = list(self.df.itertuples(index=False, name=None))
        if customer_tuple in list_of_cards:
            return True
        else:
            return False
