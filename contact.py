import tkinter as tk

# Create a dictionary to store contact information
contacts = {}

# Function to add a contact
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name:
        contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        update_contact_list()
        clear_entry_fields()

# Function to update the contact list
def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

# Function to clear the entry fields
def clear_entry_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Function to view contact details
def view_contact():
    selected_name = contact_list.get(tk.ACTIVE)
    if selected_name:
        contact_details.config(text=f"Name: {selected_name}\nPhone: {contacts[selected_name]['Phone']}\nEmail: {contacts[selected_name]['Email']}\nAddress: {contacts[selected_name]['Address']}")

# Function to search for a contact
def search_contact():
    query = entry_search.get().lower()
    matching_contacts = [name for name in contacts if query in name.lower()]
    contact_list.delete(0, tk.END)
    for name in matching_contacts:
        contact_list.insert(tk.END, name)

# Function to update a contact
def update_contact():
    selected_name = contact_list.get(tk.ACTIVE)
    if selected_name:
        name = entry_name.get()
        phone = entry_phone.get()
        email = entry_email.get()
        address = entry_address.get()
        if name:
            contacts[selected_name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            update_contact_list()
            clear_entry_fields()

# Function to delete a contact
def delete_contact():
    selected_name = contact_list.get(tk.ACTIVE)
    if selected_name:
        del contacts[selected_name]
        update_contact_list()
        clear_entry_fields()

# Create the main window
root = tk.Tk()
root.title("Contact Management")

# Entry widgets for contact details
entry_name = tk.Entry(root, width=30)
entry_phone = tk.Entry(root, width=30)
entry_email = tk.Entry(root, width=30)
entry_address = tk.Entry(root, width=30)
entry_search = tk.Entry(root, width=30)

entry_name.grid(row=0, column=1, padx=10)
entry_phone.grid(row=1, column=1, padx=10)
entry_email.grid(row=2, column=1, padx=10)
entry_address.grid(row=3, column=1, padx=10)
entry_search.grid(row=6, column=1, padx=10)

# Labels for contact details
label_name = tk.Label(root, text="Name:")
label_phone = tk.Label(root, text="Phone:")
label_email = tk.Label(root, text="Email:")
label_address = tk.Label(root, text="Address:")
label_search = tk.Label(root, text="Search:")

label_name.grid(row=0, column=0)
label_phone.grid(row=1, column=0)
label_email.grid(row=2, column=0)
label_address.grid(row=3, column=0)
label_search.grid(row=6, column=0)

# Buttons for actions
add_button = tk.Button(root, text="Add Contact", command=add_contact)
view_button = tk.Button(root, text="View Contact", command=view_contact)
search_button = tk.Button(root, text="Search", command=search_contact)
update_button = tk.Button(root, text="Update Contact", command=update_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)

add_button.grid(row=4, column=0, columnspan=2, pady=10)
view_button.grid(row=5, column=0, columnspan=2, pady=10)
search_button.grid(row=6, column=2)
update_button.grid(row=7, column=0, pady=10)
delete_button.grid(row=7, column=1, pady=10)

# Listbox to display contacts
contact_list = tk.Listbox(root, width=40)
contact_list.grid(row=8, column=0, columnspan=2)

# Label to display contact details
contact_details = tk.Label(root, text="", width=40, justify=tk.LEFT)
contact_details.grid(row=9, column=0, columnspan=2)

# Run the application
root.mainloop()
