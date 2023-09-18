import pandas as pd


class Hotel:
    def __init__(self, path):
        self.df = pd.read_csv(path, dtype={"id": str})
        self.df_string = self.df.to_string(index=False)
        print(self.df_string)
        self.hotel_id_choice = input("\nEnter the ID of Hotel you want to book: ")
        self.hotel_name = ""
        self.hotel_city = ""

    def check_availability(self):
        while True:
            self.hotel_name = self.df.loc[self.df["id"] == self.hotel_id_choice]["name"].squeeze()
            self.hotel_city = self.df.loc[self.df["id"] == self.hotel_id_choice]["city"].squeeze()
            if self.hotel_id_choice in list(self.df["id"]):
                flag = self.df.loc[self.df["id"] == self.hotel_id_choice]["available"].squeeze()
                if flag == "yes":
                    return True
                else:
                    return False
            else:
                print("\nHotel not in list, please re-enter")
                print(self.df_string)
                self.hotel_id_choice = input("\nEnter the ID of Hotel you want to book again: ")

