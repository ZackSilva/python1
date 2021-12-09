if __name__ == '__main__':
    # Creates class instance "Birds" and assigns two attributes
    class Birds:

        # Defines birds as wild
        attr1 = "wild"

        def __init__(self, color, species):
            self.color = color
            self.species = species

        # Function to display bird attributes to user
        def show_bird(self):
            return (f"{self.color} {self.species}")

        # Function to let the birds sing!
        def caw(self):
            print("cacaw!")

    b1 = Birds("black", "raven")
    b2 = Birds("red", "cardinal")

    # Begins to prompt user
    print(f"Look, it's a {Birds.show_bird(b1)}!")
    name1 = input(f"Please name it: ")

    print(f"Now here comes a {Birds.show_bird(b2)}!")
    name2 = input(f"Please name this one, too: ")

    print(f"Accompanying you now are two friends: a {Birds.show_bird(b1)} named {name1}")
    print(f"and a {Birds.show_bird(b2)} named {name2}")

    # Allows the user to choose whether to hold each bird
    hold_decision1 = input(f"Will you try to pick up {name1}? Please type 'yes' or 'no': ")
    if hold_decision1 == "yes":
        print(Birds.caw(b1))
        print("I'm not sure he liked that...")
    else:
        print("Good idea.")

    hold_decision2 = input(f"Will you try to pick up {name2}? Please type 'yes' or 'no': ")
    if hold_decision2 == "yes":
        print(Birds.caw(b2))
        print("Probably wasn't the best idea you've had...")
    else:
        print("Good idea.")

    # Ridicules the user if they opted to hold wild birds... twice
    if hold_decision1 == "yes" and hold_decision2 == "yes":
        print("Didn't you learn the first time?")
    else:
        pass

