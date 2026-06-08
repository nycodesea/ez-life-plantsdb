import plantsdb

plantsdb.init_db()
user_input = input("0 : showing data\n1 : Input data\n")
if user_input == "1":
    plantsdb.save_plants(plantsdb.Input_plants_data())
    print("Saved.")
else:
    user_input = input("Input a search word or blank for table: ")
    print("Display Plants Database\n")
    plantsdb.show_data(user_input)
