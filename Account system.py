# python password storage
accounts = {}


def new_account():
    username = input("Enter Account Username - ")
    print()
    password = input("Enter Account Password? - ")
    accounts[username] = password
    print(accounts)
    main()


def remove_account():
    accounts.pop(input("Enter Username of the account you want to remove - "))
    main()


def admin():
    print(accounts)
    main()


def main():
    user_selection = 0

    print("""
    Welcome to the account system

    Select a action

    1 - Create New account

    2 - Delete Account

    3 - Enter admin system

    10 - Quit Application

    """)

    while user_selection == 0:
        user_selection = int((input("Input selection - ")))

    if user_selection == 1:
        new_account()

    elif user_selection == 2:
        remove_account()

    elif user_selection == 3:
        admin()

    elif user_selection == 10:
        pass


main()