from Container_recycling_machine import ContainerRecyclingMachine
# Container objects already imported to recycling machine file

print("Welcome to the recycling machine.")
depositing = True
while depositing:
    if __name__ == "__main__":
        # parameters of recycling machine set to 0 each time the function is called so values reset for next customer
        ContainerRecyclingMachine(0, "", 0, 0, 0, 0, 0).select_product()
    while True:
        try:
            deposit_again = input("(N)ext customer or (Q)uit? ").lower()
            if deposit_again == "n":
                depositing = True
                print("\n")
                break
            else:
                depositing = False
                break
        except ValueError:
            print("Sorry, something went wrong. Please try again.")
            continue


