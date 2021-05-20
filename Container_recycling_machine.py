from Container import glass, plastic, cardboard, tin
# Then imported to main.py


class ContainerRecyclingMachine:

    def __init__(self, bal, selection, amount, stored_plastic, stored_glass, stored_cardboard, stored_tin):
        self.bal = bal
        self.selection = selection # selection value is saved from select_product() to allow subsequent functions to be executed for correct item
        self.amount = amount
        self.stored_plastic = stored_plastic
        self.stored_glass = stored_glass
        self.stored_cardboard = stored_cardboard
        self.stored_tin = stored_tin

    def select_product(self):
        print("Your initial balance is: ${}".format(self.bal))
        while True:
            self.selection = input("Please select a container type to deposit: (Plastic, Glass, Cardboard, Tin) "
                                   "Or type 'stop' to finish: ").lower()
            if self.selection == "plastic":
                if self.stored_plastic <= 49: # checks items stored aren't at 50/50, prevents accept function from executing if they are
                    self.accept_plastic()
                elif self.stored_plastic >= 50:
                    print("Sorry, the machine has reached the limit for {}. Please try depositing another"
                          " container type.".format(self.selection))
            elif self.selection == "glass":
                if self.stored_glass <= 49:
                    self.accept_glass()
                elif self.stored_glass >= 50:
                    print("Sorry, the machine has reached the limit for {}. Please try depositing another"
                          " container type.".format(self.selection))
            elif self.selection == "cardboard":
                if self.stored_cardboard <= 49:
                    self.accept_cardboard()
                elif self.stored_cardboard >= 50:
                    print("Sorry, the machine has reached the limit for {}. Please try depositing another"
                          " container type.".format(self.selection))
            elif self.selection == "tin":
                if self.stored_tin <= 49:
                    self.accept_tin()
                elif self.stored_tin >= 50:
                    print("Sorry, the machine has reached the limit for {}. Please try depositing another"
                          " container type.".format(self.selection))
            elif self.selection == "stop":
                self.print_receipt()
                break
            else:
                print("Sorry, something went wrong. Please try entering that again.")
                continue

    #accept_product functions broken down into specific items to allow machine to check how many items are already stored
    def accept_plastic(self):
        while True:
            try:
                self.amount = int(input("How many {} containers would you like to deposit? The machine can"
                                        " accept a maximum of 50 of each type. ".format(self.selection)))
                if self.amount + self.stored_plastic >= 51:
                    print("Sorry, that's too many.")
                elif self.amount <= 0:
                    print("Sorry, you can't deposit nothing.")
                else:
                    self.payout()
                    print("Please place the items into the machine.")
                    for i in range(self.amount):
                        print("{} accepted.".format(self.selection))
                    print("Thank you for depositing {} {} containers. The machine contains {}/50 plastic containers."
                          " That brings your balance to ${}.".format(self.amount, self.selection, self.stored_plastic,
                                                                     self.bal))
                break
            except ValueError:
                print("Input numbers only please.")
                continue

    def accept_glass(self):
        while True:
            try:
                self.amount = int(input("How many {} containers would you like to deposit? The machine can"
                                        " accept a maximum of 50 of each type. ".format(self.selection)))
                if self.amount + self.stored_glass >= 51:
                    print("Sorry, that's too many.")
                elif self.amount <= 0:
                    print("Sorry, you can't deposit nothing.")
                else:
                    self.payout()
                    print("Please place the items into the machine.")
                    for i in range(self.amount):
                        print("{} accepted.".format(self.selection))
                    print("Thank you for depositing {} {} containers. The machine contains {}/50 glass containers."
                          " That brings your balance to ${}.".format(self.amount, self.selection, self.stored_glass,
                                                                     self.bal))
                break
            except ValueError:
                print("Input numbers only please.")
                continue

    def accept_cardboard(self):
        while True:
            try:
                self.amount = int(input("How many {} containers would you like to deposit? The machine can"
                                        " accept a maximum of 50 of each type. ".format(self.selection)))
                if self.amount + self.stored_cardboard >= 51:
                    print("Sorry, that's too many.")
                elif self.amount <= 0:
                    print("Sorry, you can't deposit nothing.")
                else:
                    self.payout()
                    print("Please place the items into the machine.")
                    for i in range(self.amount):
                        print("{} accepted.".format(self.selection))
                    print("Thank you for depositing {} {} containers. The machine contains {}/50 cardboard containers."
                          " That brings your balance to ${}.".format(self.amount, self.selection,
                                                                     self.stored_cardboard, self.bal))
                break
            except ValueError:
                print("Input numbers only please.")
                continue

    def accept_tin(self):
        while True:
            try:
                self.amount = int(input("How many {} containers would you like to deposit? The machine can"
                                        " accept a maximum of 50 of each type. ".format(self.selection)))
                if self.amount + self.stored_tin >= 51:
                    print("Sorry, that's too many.")
                elif self.amount <= 0:
                    print("Sorry, you can't deposit nothing.")
                else:
                    self.payout()
                    print("Please place the items into the machine.")
                    for i in range(self.amount):
                        print("{} accepted.".format(self.selection))
                    print("Thank you for depositing {} {} containers. The machine contains {}/50 tin containers."
                          " That brings your balance to ${}.".format(self.amount, self.selection, self.stored_tin,
                                                                     self.bal))
                break
            except ValueError:
                print("Input numbers only please.")
                continue

    #payout called in accept functions to update prices and stored item amounts
    def payout(self):
        if self.selection == "plastic":
            self.bal = self.bal + (plastic.value * self.amount)
            self.stored_plastic = self.amount + self.stored_plastic
        elif self.selection == "glass":
            self.bal = self.bal + (glass.value * self.amount)
            self.stored_glass = self.amount + self.stored_glass
        elif self.selection == "cardboard":
            self.bal = self.bal + (cardboard.value * self.amount)
            self.stored_cardboard = self.amount + self.stored_cardboard
        elif self.selection == "tin":
            self.bal = self.bal + (tin.value * self.amount)
            self.stored_tin = self.amount + self.stored_tin
        else:
            print("sorry, something went wrong while calculating your payment.")

    def print_receipt(self):
        final_total = self.stored_tin + self.stored_cardboard + self.stored_glass + self.stored_plastic
        plastic_final = self.stored_plastic * plastic.value
        glass_final = self.stored_glass * glass.value
        cardboard_final = self.stored_cardboard * cardboard.value
        tin_final = self.stored_tin * tin.value
        print("\n--------- receipt ---------\n"
              "Containers deposited:\n"
              "\n"
              "plastic: {}\t ${}\n"
              "glass: {}\t ${}\n"
              "cardboard: {}\t${}\n"
              "tin: {}\t${}\n"
              "\n"
              "Total containers: {}\n"
              "Total payment: ${}\n"
              "\n"
              "Thank you for recycling!\n"
              "--------- receipt ---------\n".format(self.stored_plastic, plastic_final, self.stored_glass, glass_final,
                                                     self.stored_cardboard, cardboard_final, self.stored_tin, tin_final,
                                                     final_total, self.bal))
