class Citizen:
    def __init__(self, citizen_id, name, community):
        self.citizen_id = citizen_id
        self.name = name
        self.community = community

    def display_info(self):
        print(f"Citizen ID: {self.citizen_id}")
        print(f"Name: {self.name}")
        print(f"Community: {self.community}")

    def update_community(self, new_community):
        self.community = new_community


class Complaint:
    # Class variable used to generate complaint IDs
    next_id = 1001

    def __init__(self, citizen, category, description):
        self.complaint_id = f"C{Complaint.next_id}"
        Complaint.next_id += 1
        self.citizen = citizen
        self.category = category
        self.description = description
        self.status = "Pending"

    @classmethod
    def create_complaint(cls, citizen, category, description):
        return cls(citizen, category, description)

    def update_status(self, new_status):
        allowed_statuses = ["Pending", "In Progress", "Resolved"]
        if new_status in allowed_statuses:
            self.status = new_status
        else:
            print("Invalid status. Use: Pending, In Progress, or Resolved.")

    def display_info(self):
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Citizen: {self.citizen.name}")
        print(f"Community: {self.citizen.community}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")


class ComplaintSystem:
    def __init__(self):
        self.complaints = []

    def add_complaint(self, complaint):
        self.complaints.append(complaint)

    def display_complaints(self):
        if not self.complaints:
            print("\nNo complaints have been recorded.")
            return

        print("\n========== ALL COMPLAINTS ==========")
        for complaint in self.complaints:
            complaint.display_info()
            print("------------------------------------")

    def find_complaint(self, complaint_id):
        for complaint in self.complaints:
            if complaint.complaint_id == complaint_id:
                return complaint
        return None

# TASK 2: ADD COMPLAINT

def add_complaint(system):
    print("\n========== ADD COMPLAINT ==========")

    def get_required_input(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This field cannot be empty. Please enter a value.")

    # Get validated information from the user
    citizen_id = get_required_input("Enter citizen ID: ")
    name = get_required_input("Enter citizen name: ")
    community = get_required_input("Enter community: ")
    category = get_required_input("Enter complaint category: ")
    description = get_required_input("Enter complaint description: ")

    # Create Citizen object
    citizen = Citizen(citizen_id, name, community)

    # Create Complaint object using the class method
    complaint = Complaint.create_complaint(citizen, category, description)

    # Add complaint to the list
    system.add_complaint(complaint)

    print("\nComplaint added successfully.")
    print(f"Your complaint ID is: {complaint.complaint_id}")



# TASK 3: UPDATE COMPLAINT STATUS

def update_complaint_status(system):
    print("\n========== UPDATE STATUS ==========")
    complaint_id = input("Enter complaint ID: ").strip()

    # Search for the complaint
    complaint = system.find_complaint(complaint_id)

    if complaint is None:
        print("Complaint not found.")
        return

    # Display available status options
    print("\nSelect new status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Resolved")

    choice = input("Choose new status: ").strip()

    # Dictionary used to map menu choices to statuses
    status_map = {
        "1": "Pending",
        "2": "In Progress",
        "3": "Resolved"
    }

    # Validate user's choice
    if choice in status_map:
        complaint.update_status(status_map[choice])
        print("Complaint status updated successfully.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")


# MAIN MENU & PROGRAM

def display_menu():
    print("\n==========================================")
    print(" CITIZEN COMPLAINT MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Add complaint")
    print("2. Display all complaints")
    print("3. Update complaint status")
    print("4. Exit")
    print("==========================================")


def main():
    system = ComplaintSystem()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_complaint(system)
        elif choice == "2":
            system.display_complaints()
        elif choice == "3":
            update_complaint_status(system)
        elif choice == "4":
            print("\nThank you for using the Citizen Complaint Management System.")
            break
        else:
            print("\nInvalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()