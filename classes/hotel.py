import pandas as pd


class Hotel:
    def __init__(self, path):
        self.df = pd.read_csv(path, dtype={"id": str})
        print(self.df.to_string(index=False))
        self.hotel_id_choice = input("\nEnter the ID of Hotel you want to book: ")
        self.hotel_name = self.df.loc[self.df["id"] == self.hotel_id_choice]["name"].squeeze()
        self.hotel_city = self.df.loc[self.df["id"] == self.hotel_id_choice]["city"].squeeze()


    def check_availability(self):
        while 1:
            if self.hotel_id_choice in list(self.df["id"]):
                flag = self.df.loc[self.df["id"] == self.hotel_id_choice]["available"].squeeze()
                if flag == "yes":
                    return True
                else:
                    return False
            else:
                print("Hotel not in list, please renter")
                print(self.df)
                self.hotel_id_choice = input("\nEnter the ID of Hotel you want to book: ")