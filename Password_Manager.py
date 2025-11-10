import json
from fuzzywuzzy import fuzz
# 1) Dictionary with saved passwords, add and remove password




def New_Entry():
    Website_Name = input("Type website name: ")
    Username = input("Type username: ")
    Password = input("Type Password: ")
    try:
        with open("Password_Data.json", "r") as file:
            password_data = json.load(file)
            password_data[Website_Name] = {"Username" : Username, "Password" : Password}
        with open("Password_Data.json", "w") as file:
            json.dump(password_data, file)
    except (FileNotFoundError,json.JSONDecodeError):
        with open("Password_Data.json", "w") as file:
            password_data = {}
            password_data[Website_Name] = {"Username" : Username, "Password" : Password}
            json.dump(password_data, file)
            


def Delete_Entry():
    with open("Password_Data.json", "r") as file:
        Data = json.load(file)
        amount_of_websites = 1
        for key in Data:
            print(f"{amount_of_websites}) {key}")
            amount_of_websites += 1
        
        while True:
            chosen_entry_to_delete = input("Type website you would like to delete here: ")
            highest_score = 0
            best_match = None
            for key in Data:
                score = fuzz.ratio(chosen_entry_to_delete,key)
                if score > highest_score:
                    highest_score = score
                    best_match = key
            response = input(f"Did you mean {best_match}? Y/N: ").upper()
            if response == "Y":
                del Data[best_match]
                with open("Password_Data.json", "w") as file:
                    json.dump(Data,file)      

                break
            else:
                print("Please try again.")

            



Delete_Entry()



