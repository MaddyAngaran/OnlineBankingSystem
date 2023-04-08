import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Bank import Bank


class BankGUI:
    def __init__(self, master):
        self.master = master
        self.bank = Bank('users.dat')
        self.current_user = None
        self.create_widgets()

    def create_widgets(self):
        # create login frame
        self.login_frame = ttk.Frame(self.master, padding=20)
        self.login_frame.grid(row=0, column=0, padx=50, pady=50)

        # create login form
        ttk.Label(self.login_frame, text="UserId: ").grid(row=0, column=0, padx=10, pady=10)
        self.userId_entry = ttk.Entry(self.login_frame)
        self.userId_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.login_frame, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        login_button.grid(row=2, column=1, padx=10, pady=10)

        signup_button = ttk.Button(self.login_frame, text="Sign Up", command=self.show_signup_frame)
        signup_button.grid(row=3, column=1, padx=10, pady=10)

        # create sign-up frame
        self.signup_frame = ttk.Frame(self.master, padding=20)

        # create sign-up form
        ttk.Label(self.signup_frame, text="Name: ").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(self.signup_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.signup_frame, text="Phone Number: ").grid(row=1, column=0, padx=10, pady=10)
        self.phoneNumber_entry = ttk.Entry(self.signup_frame)
        self.phoneNumber_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.signup_frame, text="e-mail: ").grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = ttk.Entry(self.signup_frame)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.signup_frame, text="Password: ").grid(row=3, column=0, padx=10, pady=10)
        self.new_password_entry = ttk.Entry(self.signup_frame, show='*')
        self.new_password_entry.grid(row=3, column=1, padx=10, pady=10)

        ttk.Label(self.signup_frame, text="Account Type: ").grid(row=4, column=0, padx=10, pady=10)
        self.account_type_combobox = ttk.Combobox(self.signup_frame, values=['Chequing', 'Savings'])
        self.account_type_combobox.grid(row=4, column=1, padx=10, pady=10)

        signup_button = ttk.Button(self.signup_frame, text="Sign Up", command=self.signup)
        signup_button.grid(row=5, column=1, padx=10, pady=10)

        # create main menu frame
        self.main_menu_frame = ttk.Frame(self.master, padding=20)

        # create account listbox
        ttk.Label(self.main_menu_frame, text="Accounts").grid(row=0, column=0, padx=10, pady=10)
        self.account_listbox = tk.Listbox(self.main_menu_frame, width=30, height=10)
        self.account_listbox.grid(row=1, column=0, padx=10, pady=10)

        # create account details frame
        self.account_details_frame = ttk.Frame(self.main_menu_frame, padding=20)
        self.account_details_frame.grid(row=1, column=1, padx=10, pady=10)

        # create account details form
        ttk.Label(self.account_details_frame, text="Account Number: ").grid(row=0, column=0, padx=10, pady=10)
        self.account_number_label = ttk.Label(self.account_details_frame, text="")
        self.account_number_label.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.account_details_frame, text="Account Type: ").grid(row=1, column=0, padx=10, pady=10)
        self.account_type_label = ttk.Label(self.account_details_frame, text="")
        self.account_type_label.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.account_details_frame, text="Balance: ").grid(row=2, column=0, padx=10, pady=10)
        self.balance_label = ttk.Label(self.account_details_frame, text="")
        self.balance_label.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.account_details_frame, text="Deposit: ").grid(row=3, column=0, padx=10, pady=10)
        self.deposit_entry = ttk.Entry(self.account_details_frame)
        self.deposit_entry.grid(row=3, column=1, padx=10, pady=10)

        deposit_button = ttk.Button(self.account_details_frame, text="Deposit", command=self.deposit)
        deposit_button.grid(row=3, column=2, padx=10, pady=10)

        ttk.Label(self.account_details_frame, text="Withdraw: ").grid(row=4, column=0, padx=10, pady=10)
        self.withdraw_entry = ttk.Entry(self.account_details_frame)
        self.withdraw_entry.grid(row=4, column=1, padx=10, pady=10)
        withdraw_button = ttk.Button(self.account_details_frame, text="Withdraw", command=self.withdraw)
        withdraw_button.grid(row=4, column=2, padx=10, pady=10)

        # create logout button
        logout_button = ttk.Button(self.main_menu_frame, text="Logout", command=self.logout)
        logout_button.grid(row=2, column=1, padx=10, pady=10)

        # create new account frame
        create_account_button = ttk.Button(self.main_menu_frame, text="Create Account", command=self.show_create_account_frame)
        create_account_button.grid(row=0, column=0, padx=10, pady=10)


        self.create_account_frame = ttk.Frame(self.master, padding=20)

        ttk.Label(self.create_account_frame, text="Account Type: ").grid(row=0, column=0, padx=10, pady=10)
        self.new_account_type_combobox = ttk.Combobox(self.create_account_frame, values=['Chequing', 'Savings'])
        self.new_account_type_combobox.grid(row=0, column=1, padx=10, pady=10)

        create_account_button = ttk.Button(self.create_account_frame, text="Create Account", command=self.create_new_account)
        create_account_button.grid(row=1, column=1, padx=10, pady=10)


    def create_account(self):
        self.current_user.create_account()

    def show_create_account_frame(self):
        self.main_menu_frame.grid_forget()
        self.create_account_frame.grid(row=0, column=0, padx=50, pady=50)

    def create_new_account(self):
        account_type = self.new_account_type_combobox.get()
        success = self.current_user.create_account(account_type)

        if success:
            messagebox.showinfo("Success", "Account created successfully!")
            self.create_account_frame.grid_forget()
            self.update_account_listbox()
            self.show_account_details()
            self.main_menu_frame.grid(row=0, column=0, padx=50, pady=50)
        else:
            messagebox.showerror("Error", "Username already exists")

    def login(self):
        userId = self.userId_entry.get()
        password = self.password_entry.get()

        if self.bank.login(userId, password):
            self.current_user = self.bank.get_user(userId)
            self.update_account_listbox()
            self.show_account_details()
            self.login_frame.grid_forget()
            self.main_menu_frame.grid(row=0, column=0, padx=50, pady=50)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def logout(self):
        self.current_user = None
        self.account_listbox.delete(0, tk.END)
        self.account_number_label.config(text="")
        self.account_type_label.config(text="")
        self.balance_label.config(text="")
        self.withdraw_entry.delete(0, tk.END)
        self.deposit_entry.delete(0, tk.END)
        self.main_menu_frame.grid_forget()
        self.bank.save_users()
        self.login_frame.grid(row=0, column=0, padx=50, pady=50)
        

    def update_account_listbox(self):
        self.account_listbox.delete(0, tk.END)
        for account in self.current_user.accounts:
            print(account)
            self.account_listbox.insert(tk.END, self.current_user.accounts[account].account_number)

    def show_account_details(self):
        if len(self.current_user.accounts) > 0:
            account = self.get_selected_account()
            self.account_number_label.config(text=account.account_number)
            self.account_type_label.config(text=account.type)
            self.balance_label.config(text=account.balance)
        else:
            self.account_number_label.config(text="")
            self.account_type_label.config(text="")
            self.balance_label.config(text="$"+str(account.balance))

    def deposit(self):
        amount = float(self.deposit_entry.get())
        account = self.get_selected_account()
        account.deposit(amount)
        self.show_account_details()

    def withdraw(self):
        amount = float(self.withdraw_entry.get())
        account = self.get_selected_account()
        success = account.withdraw(amount)
        if success:
            self.show_account_details()
        else:
            messagebox.showerror("Error", "Insufficient funds")

    def get_selected_account(self):
        try:
            selected_index = (self.account_listbox.curselection())[0]
            account_number = self.account_listbox.get(selected_index)
            return self.current_user.get_account(account_number)
        except IndexError:
            return list(self.current_user.accounts.values())[0]

    def show_signup_frame(self):
        self.login_frame.grid_forget()
        self.signup_frame.grid(row=0, column=0, padx=50, pady=50)

    def signup(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phoneNumber = self.phoneNumber_entry.get()
        password = self.new_password_entry.get()
        account_type = self.account_type_combobox.get()

        success = self.bank.create_user(name, email, phoneNumber, password)
        success.create_account(account_type)

        if success:
            messagebox.showinfo("Success",
                                "Account created successfully!\n\nYour user identification number is: " + str(
                                    success.userId) + "\n\nWrite this down somewhere safe as this will be the number you log into your account with.")
            self.show_login_frame()
        else:
            messagebox.showerror("Error", "Username already exists")

    def show_login_frame(self):
        self.signup_frame.grid_forget()
        self.userId_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.login_frame.grid(row=0, column=0, padx=50, pady=50)

