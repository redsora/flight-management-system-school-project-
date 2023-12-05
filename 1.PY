
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox


# This module is for the reminder
# In the code given below, which is for the function of reminder. 
# The reminder will pop up if there’s a flight not updated or cancelled.

def reminder(scheduler):
    # Check every 15 minutes
    time_check = datetime.now() - timedelta(minutes=15)
    
    for flight_number, flight_info in scheduler.items():
        # Parse time
        flight_time = datetime.strptime(flight_info[0], '%H:%M')
        
        # If flight time is earlier than the check time
        if flight_time < time_check:
            scheduled_reminders = tk.Tk()
            scheduled_reminders.title("Reminder!")
            tk.Label(master=scheduled_reminders, text="Flight Number " + flight_number + " Not Updated").grid(row=0, column=0)
            scheduled_reminders.mainloop()

# Test data
scheduler = {
    '123': ['08:30', 'Status: Delayed'],
    '456': ['09:00', 'Status: On Time'],
    '789': ['09:30', 'Status: Cancelled']
}

reminder(scheduler)


# This module is for the deleted user account
# The code given below is for the function of deleting a user account. 


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Delete A User")

        self.label = tk.Label(self, text="Enter the Username")
        self.label.grid(row=0, column=0)

        self.username = tk.Entry(self)
        self.username.grid(row=0, column=1)

        self.submit_button = tk.Button(self, text="Confirm Deletion", width=25, command=self.delete_user)
        self.submit_button.grid(row=0, column=2)

    def delete_user(self):
        username = self.username.get()

        if username in ('admin', 'manager', 'cancelled'):
            tk.messagebox.showerror("Error", "Cannot Delete user!")
            return

        try:
            user = None

            if username in self.admin:
                user = self.admin.pop(username)
            elif username in self.manager:
                user = self.manager.pop(username)
            elif username in self.standard:
                user = self.standard.pop(username)

            if user:
                tk.messagebox.showinfo("Success", f"{username} Successfully Deleted!")

        except KeyError:
            tk.messagebox.showerror("Error", "Username not found! Please try again!")

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()


# This module is for adding admin users
# In the code given below, which is for the function of adding admin users



class UserManager:
    def __init__(self):
        self.admins = {}
        self.managers = {}
        self.standards = {}

        self.root = tk.Tk()
        self.root.title("User Management")

        self.add_admin_button = tk.Button(self.root, text="Add An Admin", command=self.add_admin)
        self.add_admin_button.pack()

    def add_admin(self):
        username = tk.simpledialog.askstring("Enter Username", "Please enter the username")

        if username in self.admins or username in self.managers or username in self.standards:
            messagebox.showerror("Error", "Username Already Exists!")
        else:
            password = tk.simpledialog.askstring("Enter Password", "Please enter the password", show='*')
            self.admins[username] = password
            messagebox.showinfo("Success", "Admin Successfully Added!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    manager = UserManager()
    manager.run()

# This module is for the adding manager
# In the code given below, which is for the function of adding manager.




class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Add A Manager")
        self.geometry("300x200")

        self.manager = {}
        self.standard = {}
        self.admin3 = {}

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Enter the Username")
        self.username_label.grid(row=1, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1)

        self.confirm_username_button = tk.Button(self, text="Confirm Username", width=25, command=self.manager_username)
        self.confirm_username_button.grid(row=1, column=3)

        self.password_label = tk.Label(self, text="Enter the Password")
        self.password_label.grid(row=2, column=0)

        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.grid(row=2, column=1)

        self.confirm_password_button = tk.Button(self, text="Confirm Password", width=25, command=self.manager_users_back)
        self.confirm_password_button.grid(row=2, column=3)

    def manager_username(self):
        user = self.username_entry.get()
        if user in self.admin3 or user in self.manager or user in self.standard:
            self.confirm_username_button.config(state=tk.DISABLED)
            self.username_label.config(text="Username Already Exists! Please Try Again")
        else:
            self.confirm_password_button.config(state=tk.NORMAL)

    def manager_users_back(self):
        user = self.username_entry.get()
        password = self.password_entry.get()

        self.manager[user] = password

        self.confirm_password_button.config(state=tk.DISABLED)
        self.username_label.config(text="Manager Successfully Added!")

if __name__ == "__main__":
    app = App()
    app.mainloop()


# This module is for adding standard user
# In the code given below. which is for the function adding a standard user.

class UserManager:
    def __init__(self):
        self.admin = set()
        self.manager = set()
        self.standard = {}

        self.create_ui()

    def create_ui(self):
        self.root = tk.Tk()
        self.root.title("User Manager")

        self.add_admin_button = tk.Button(master=self.root, width=25, text="Add An Admin", command=self.adding_admin)
        self.add_admin_button.grid(row=1, column=1)

        self.add_manager_button = tk.Button(master=self.root, width=25, text="Add A Supervisor", command=self.add_manager)
        self.add_manager_button.grid(row=2, column=1)

        self.add_standard_user_button = tk.Button(master=self.root, width=25, text="Add A Standard User", command=self.adding_standard)
        self.add_standard_user_button.grid(row=3, column=1)

        self.root.mainloop()

    def adding_admin(self):
        self.create_add_user_window(self.admin)

    def add_manager(self):
        self.create_add_user_window(self.manager)

    def adding_standard(self):
        self.create_add_user_window(self.standard)

    def create_add_user_window(self, user_dict):
        add_user_window = tk.Toplevel(self.root)
        add_user_window.title("Add A User")

        def check_user_exists():
            username = username_entry.get()
            if username in user_dict:
                messagebox.showerror("Error", "Username Already Exists! Please Try Again")
                return False
            return True

        def add_user():
            if check_user_exists():
                username = username_entry.get()
                password = password_entry.get()
                user_dict[username] = password
                messagebox.showinfo("Success", "User Successfully Added!")
                add_user_window.destroy()

        tk.Label(master=add_user_window, text="Enter the Username").grid(row=1, column=0)
        username_entry = tk.Entry(master=add_user_window)
        username_entry.grid(row=1, column=1)

        tk.Label(master=add_user_window, text="Enter the Password").grid(row=2, column=0)
        password_entry = tk.Entry(master=add_user_window, show='*')
        password_entry.grid(row=2, column=1)

        tk.Button(master=add_user_window, text="Add User", command=add_user, width=25).grid(row=3, column=1)

UserManager()



# This module is for the view of all users
# In the code given below, which is for the function of view of all users.




def display_users():
    # Define a tkinter window
    display_scheduled = tk.Tk()
    display_scheduled.title("View Users")

    # Define row positions for the different types of users
    row_positions = {'Admin': 0, 'Manager': 2, 'Standard User': 4}

    # Loop through the different types of users
    for user_type, row in row_positions.items():
        # Create a label for the user type
        tk.Label(master=display_scheduled, text=f"{user_type} Are:").grid(row=row, column=0)

        # Create a list of the current type of users
        users = eval(user_type.lower())

        # Loop through the users of the current type and create a label for each one
        for index, user in enumerate(users):
            tk.Label(master=display_scheduled, text=f"----- {user}").grid(row=row + index + 1, column=0)

    # Start the tkinter main loop
    display_scheduled.mainloop()



# # This module is for the delete users
# The code given below is for the function of deleting users such as admin, manager, and standard accounts.

def deleting_users():
    def deleting_back_user():
        user = username.get()
        if not (user in admin or user in manager or user in standard):
            messagebox.showerror("Username Not Found!", "Username not found! Please try again!")
        else:
            if user in admin:
                del admin[user]
                messagebox.showinfo("Success!", "Admin User Successfully Deleted!")
            if user in manager:
                del manager[user]
                messagebox.showinfo("Success!", "Manager Successfully Deleted!")
            if user in standard:
                del standard[user]
                messagebox.showinfo("Success!", "Standard User Successfully Deleted!")

    delete_users_scheduled = tk.Toplevel()
    delete_users_scheduled.title("Delete A User")
    tk.Label(master=delete_users_scheduled, text="Enter the Username").grid(row=1, column=0)
    username = tk.Entry(master=delete_users_scheduled)
    username.grid(row=1, column=1)
    admin2 = tk.Button(master=delete_users_scheduled, text="Confirm Deletion", width=25,
                       command=deleting_back_user).grid(row=1, column=2)






# This module is for the update
# The code given below, which is for the function of updating the destination, status, and flight number.

import tkinter as tk

def update_btn1():
    flight_number = number_of_flight.get()
    if flight_number not in scheduled:
        scheduled[flight_number] = ["", "", ""]
        tk.Label(master=scheduled_update, text="Enter Departure Time").grid(row=3, column=0)
        tk.Label(master=scheduled_update, text="Enter Status").grid(row=4, column=0)
        tk.Label(master=scheduled_update, text="Enter Destination").grid(row=5, column=0)

def update_btn2():
    flight_number = number_of_flight.get()
    departure_time = departure_time.get()
    stat = stat.get()
    destination_place = destination_place.get()

    if departure_time:
        scheduled[flight_number][0] = departure_time
    if stat:
        scheduled[flight_number][2] = stat
    if destination_place:
        scheduled[flight_number][1] = destination_place

    update_root = tk.Toplevel(scheduled_update)
    update_root.title("Successfully Updated!")
    tk.Label(master=update_root, text="Successfully Updated!!").grid(row=0, column=0)

def main():
    scheduled_update = tk.Tk()
    scheduled_update.title("Update/Add A Flight")

    tk.Label(master=scheduled_update, text="Enter The Flight Number").grid(row=1, column=0)
    number_of_flight = tk.Entry(master=scheduled_update)
    number_of_flight.grid(row=1, column=1)

    tk.Button(master=scheduled_update, text="Confirm", command=update_btn1).grid(row=2, column=1)

    departure_time = tk.Entry(master=scheduled_update)
    stat = tk.Entry(master=scheduled_update)
    destination_place = tk.Entry(master=scheduled_update)

    tk.Button(master=scheduled_update, text="Confirm", command=update_btn2).grid(row=6, column=1)

    scheduled_update.mainloop()

if __name__ == "__main__":
    main()












