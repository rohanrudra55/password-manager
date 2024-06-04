from src.server import Connect
from src.Authenticator.PasswordModule import Data
import getpass
import argparse


def manager_system():
    parser = argparse.ArgumentParser(description='Password Manager')
    parser.add_argument('-i', '--signin', type=str, help='Sign in to an existing account')
    parser.add_argument('-u', '--signup', type=str, help='Sign up to create a new account')
    args = parser.parse_args()

    if args.signup:
        """
        Sign Up Page for System
        """
        username = args.signup
        while True:
            if len(username) > 45:
                print("Username should contains 45 characters!")
                break

            print("Password should contains 10 characters!")
            password = getpass.getpass("Enter your password: ")
            password_rc = getpass.getpass("Confirm your password: ")
            if password != password_rc and not Data.validate(password):
                print('In valid password. Please try again!')
                pass

            email = input('Enter you valid email: ')
            if not Data.is_valid_email(email):
                print('Invalid mail ID. Try Again!')
                pass

            obj = Connect()
            if obj.add_user(username, email, password):
                print("successfully Registered!")
                break

            else:
                print('Server Error!')
                break

    elif args.signin:
        """
        Sign Up Page for System
        """
        username = args.signin
        obj = Connect()
        while True:
            if len(username) > 45:
                print("Invalid Username!")
                break

            password = getpass.getpass("Enter your password: ")
            if not obj.verify_user_signin(username, password):
                print("Invalid Password! Try again.")
                pass
            break

        while True:
            choice = input('Press (1) to view stored passwords\n'
                           'Press (2) to add new password\n'
                           'Press (q) to exit\n'
                           ': ')

            if choice == '1':
                obj.view_stored_data()
                choice_in = input('Press (q) to exit\n'
                                  'Press (b) go back\n'
                                  'Provide site to view password\n'
                                  ': ')
                if choice_in == 'q':
                    exit(0)
                elif choice_in == 'b':
                    pass
                else:
                    site = choice_in
                    obj.view_stored_password(site)

            elif choice == '2':
                username = input('Username: ')
                password = getpass.getpass('Password: ')
                site = input('Site: ')
                note = input('Note: ')
                if not obj.add_user_data(username, password, site, note):
                    print("Error !")
                    pass
            else:
                exit(0)

    else:
        print("Error: Invalid input. Enter \'-h\' for help.")


if __name__ == "__main__":
    manager_system()
