from tkinter import messagebox
import json


class PasswordManager:

    def __init__(self):
        pass

    # Method to save password. Takes data from GUI, then adds to json file if conditions are met

    def save(self, website_input, email_input, pass_input, end):

        # Pulling information from GUI, then formatting output

        website_get = website_input.get()
        email_get = email_input.get()
        password_get = pass_input.get()
        new_data = {
            website_get: {
                "email": email_get,
                "password": password_get
            }
        }
        # If website and/or password fields are empty, error message displays

        if len(website_get) == 0 or len(password_get) == 0:
            messagebox.showerror(title="Error", message="Please don't leave any fields empty!")

            # If website and password fields are filled, data is added to json file

        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open("data.json", "w") as file2:
                    json.dump(data, file2, indent=4)
                    website_input.delete(0, end)
                    pass_input.delete(0, end)

            # If json file isn't found, it is created, and the data added to it

            except FileNotFoundError:
                with open("data.json", "w") as file3:
                    json.dump(new_data, file3, indent=4)

            # Website and password fields of GUI cleared

            website_input.delete(0, end)
            pass_input.delete(0, end)

            # Success message displayed to user to let them know that the data was added

            messagebox.showinfo(title="Success", message="Password saved successfully!")

    # Method to find a password within the json file

    def find_password(self, website_input):

        # Pulling website info from GUI

        website_get = website_input.get()

        # Looking for website data within json file

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                reply = data[website_get]

                # If no error is raised, "Match Found" message is displayed to the user

                messagebox.showinfo(title="Match Found", message=
                                    f"Website: {website_get}\nEmail: {reply['email']}\nPassword: {reply['password']}")

        # Error handling/message if json file isn't found

        except FileNotFoundError:
            messagebox.showerror(title="File Not Found", message="No Data File Found.")

        # Error handling/message if no matching website key is found in the json file

        except KeyError:
            messagebox.showerror(title="No Match Found", message= "No details for the website exists.")
