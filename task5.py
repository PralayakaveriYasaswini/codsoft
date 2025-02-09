class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No matching contact found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact['name'] == name:
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def run(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == "4":
                name = input("Enter name of the contact to update: ")
                new_phone = input("Enter new phone (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")
                self.update_contact(name, new_phone or None, new_email or None, new_address or None)
            elif choice == "5":
                name = input("Enter name of the contact to delete: ")
                self.delete_contact(name)
            elif choice == "6":
                print("Exiting Contact Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ContactManager().run()
