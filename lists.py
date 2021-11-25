bikas = []


def main():
    printlists()
    delfromlist()


def printlists():
    global bikas
    bikas = ["Trek", "Gazelle", ["Redline", "Blueline", ["Yellowline", "Purpleline", "Blackline"]], "Specialized"]
    for bike in bikas:
        if isinstance(bike, list):
            for item in bike:
                if isinstance(item, list):
                    for element in item:
                        print(f"I would like to own a {element}")
                if not isinstance(item, list):
                    print(f"I would like to own a {item}")
        if not isinstance(bike, list):
            print(f"I would like to own a {bike}!")


def appendlists():
    vrienden = []
    move = False
    if not vrienden:
        print("Je hebt geen vrienden, go touch some grass bro, ga connecties maken ofzo.")
        while not move:
            newfriends = (str(input("Geef hier op welke vrienden je gemaakt hebt, of typ 'EX' om te stoppen: ")))
            if newfriends == "EX":
                move = True
            else:
                vrienden.append(newfriends)
    else:
        print(f"Dit zijn mijn vrienden: {vrienden}")
    print(f"Dit zijn nu de nieuwe vrienden: {vrienden}")
    choice = input("Zijn er nog nieuwe vrienden die je wilt toevoegen? ")
    if choice == "Ja" or "ja":
        move = False
        while not move:
            morenewfriends = input("Voeg hier je nieuwe vrienden toe, of typ EX om te stoppen: ")
            if morenewfriends == "EX":
                move = True
            else:
                vrienden.insert(-1, morenewfriends)
    elif choice == "Nee" or "nee":
        print("Prima, dan gaan we verder.")
    else:
        print("Input niet herkend")

    print(f"Dit is nu de totale lijst van vrienden: {vrienden}")


def dellist():
    premade = ["value", "test", "Lorenzo", 2, 69, True]
    print(f"Premade ver.1: {premade}")
    del premade[2]
    print(f"Premade after del statement: {premade}")


def poplist():
    anylist = ["Testvalue", "value", 1, 2, 3]
    popped_list = []
    for item in range(len(anylist)):
        popped_list.append(anylist.pop())

    print(f"Hier is de list na een pop: {popped_list}")


def sortlist():
    testlist = ["Test", "Value", "Faithley", "Lorenzo", "Lists"]
    print(testlist)
    print(sorted(testlist, reverse=True))
    print(f"Het eerste item uit een gesorteerde lijst, is: {sorted(testlist)[0]}")


def delfromlist():
    global bikas
    toberemoved = "Specialized"
    bikas.remove(toberemoved)
    print(f"Bike list without to-be-removed value is: {bikas}")


if __name__ == "__main__":
    main()

