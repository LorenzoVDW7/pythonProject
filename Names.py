# Store the names of a few friends into a list called names. print each person's name
def names():
    allnames = ["Ali", "Gurkan", "Serhat", "Safak", "Mathijs", "Soufiane"]
    for name in allnames:
        print(type(name))
        if isinstance(name, str):
            print(name)


def greetings():
    allgreets = ["Ali", "Gurkan", "Serhat", "Safak", "Mathijs", "Soufiane"]
    for greet in allgreets:
        print(f"Hallo mijn favoriete habibti: {greet}")


greetings()
