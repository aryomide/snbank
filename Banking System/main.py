import json
import os
import random

print('Welcome to Aryomide Banking System!')
def bank():
    def check_input(*args):
       
        valid = False
        while not valid:
            user_choice = str(input('>')).lower()
            loop_end = False
            for arg in args:
                if user_choice == str(arg).lower():
                    valid = True
                    loop_end = True
                    return user_choice
            if not loop_end:
                print('Please enter a valid command.')

    def my_bank():
        logged_in = False
        if os.path.exists('session.txt'):
            logged_in = True
            with open('session.txt', 'r') as f:
                fold = json.load(f)
                name = fold[0]['username']
                print('Good to see you again ', name)
                print()
        else:
            print('Enter login to Log In.')
            print('Enter end to End Program.')
            login_choice = check_input('login', 'end')
            if login_choice == 'login':
                while not logged_in:
                    username = str(input('username: ')).lower()
                    password = str(input('password: '))
                    with open('staff.txt') as file:
                        user_data = json.load(file)
                        for user in user_data:
                            if user['username'] == username and user['password'] == password:
                                logged_in = True
                             
        if logged_in:
            if not os.path.exists('session.txt'): 
                with open('session.txt','w+') as file:                     
                        session=[{
                            'username':username
                            }]
                        json.dump(session, file)
            close_session_file = open('session.txt')
            
            is_finished = False
            while not is_finished:
                print('Press 1 to create new account details')
                print('Press 2 to check account details')
                print('Press 3 to Logout')
                staff_choice = check_input('1', '2', '3')
                if staff_choice == '1':
                    acc_name = str(input('Account Name: '))
                    while True:
                        try:
                            acc_balance = int(input('Opening Balance in dollars: '))
                            break
                        except ValueError:
                            continue
                    acc_type = str(input('Account Type: '))
                    acc_email = str(input('Account Email: '))
                    acc_num = "".join(str(random.randint(0,9)) for i in range(10))

                    with open('customer.txt') as file:
                        try:
                            customer_details = json.load(file)
                        except:
                            customer_details= []
                        customer_details.append({
                            'acc_num':acc_num,
                            'acc_name': acc_name,
                            'acc_balance': acc_balance,
                            'acc_type': acc_type,
                            'acc_email': acc_email
                            })
                    with open('customer.txt', 'w') as file:
                        json.dump(customer_details, file)
                        print(acc_num)
                elif staff_choice == '2':
                    your_acc_num = str(input('Input account number: '))
                    with open('customer.txt', 'r') as file:
                        customer_details = json.load(file)
                        found = False
                        for customer_detail in customer_details:
                            if customer_detail['acc_num'] == your_acc_num:
                                print("Account name: ", customer_detail['acc_name'])
                                print("Account number: ", customer_detail['acc_num'])
                                print("Balance: ", customer_detail['acc_balance'])
                                print("Account Type: ", customer_detail['acc_type'])
                                print("Account Email: ", customer_detail['acc_email'])
                                found = True
                        if not found:
                            print('Sorry could\'nt find a user with that account number')
                elif staff_choice == '3':
                    close_session_file.close()
                    os.remove('session.txt')
                    is_finished = True
            my_bank()
    my_bank()

bank()