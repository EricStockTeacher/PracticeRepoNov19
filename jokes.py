import random

def tell_joke(joke_list):
    joke = random.choice(joke_list)
    print(f"{joke[0]}")
    input("Press enter to continue...")
    print(f"{joke[1]}")
    

def list_jokes(joke_list):
    for i, joke in enumerate(joke_list, 1):
        print(f"{i}. {joke[0]}")

def menu():
    print("Please make a selection")
    print("tell - tell a joke")
    print("list - list all jokes")
    print("exit - exit the program")

def load_jokes_from_file():
    pass


def main():
    joke_list = load_jokes_from_file()
            
    menu()

    while True:
        choice = input("Enter your choice ")
        if choice.lower() == "tell":
            tell_joke(joke_list)
        elif choice.lower() == "list":
            list_jokes(joke_list)
        elif choice.lower() == "exit":
            break
        else:
            print("invalid selection")
    print("bye!")

if __name__ == "__main__":
    main()
