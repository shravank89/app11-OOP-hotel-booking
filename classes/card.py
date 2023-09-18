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


class SecureCreditCard(CreditCard):
    def __init__(self, name, card, expiry, cvc, number, password):
        CreditCard.__init__(self, name, card, expiry, cvc)
        self.number = number
        self.password = password
        self.df1 = pd.read_csv("files/card_security.csv", dtype=str)

    def validate(self):
        customer_tuple = (self.card, self.expiry, self.cvc, self.name)
        list_of_cards = list(self.df.itertuples(index=False, name=None))
        if customer_tuple in list_of_cards:
            card_tuple = (self.number, self.password)
            list_of_secure_card = list(self.df1.itertuples(index=False, name=None))
            if card_tuple in list_of_secure_card:
                return True
        else:
            return False
