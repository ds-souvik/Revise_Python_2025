'''Create a kettle notification system for a smart kettle'''

'''Hard coded input by me'''

is_kettle_boiled = True

if is_kettle_boiled:
    print(f"Ketlle Done! Time to make Tea!")


'''Take input by user'''

is_kettle_boiled = bool(int(input("Is the kettle boiled?: (0/ 1): ")))

if is_kettle_boiled:
    print(f"Ketlle Done! Time to make Tea!")