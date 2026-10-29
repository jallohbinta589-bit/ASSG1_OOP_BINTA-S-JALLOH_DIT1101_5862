# PROG211 – Object-Oriented Programming 1

## Citizen Complaint Management System

**University:** Limkokwing University of Creative Technology – Sierra Leone  
**Department:** Information and Communication Technology  
**Course:** PROG211 – Object-Oriented Programming 1  
**Project Domain:** Government
**Project Type:** Individual Assignment  

---

## 1. Project Overview

The **Citizen Complaint Management System** is a simple Python command-line application developed using **Object-Oriented Programming (OOP)** concepts.

The system allows citizens to submit complaints about problems within their communities. Examples of complaints include:

- Road damage
- Waste management
- Street lighting
- Public facility problems
- Other community-related issues

The system stores complaint records, displays them, and allows the status of a complaint to be updated.

The project was developed to demonstrate the OOP concepts covered in **Lectures 1–3** of PROG211 while solving a simple real-world government problem.

---

## 2. Problem Statement

Citizens often experience problems in their communities, such as damaged roads, poor waste collection, and broken public facilities.

When complaints are handled manually, it can become difficult to organize records and track whether a complaint has been addressed.

The Citizen Complaint Management System provides a simple digital method for:

1. Recording citizen complaints
2. Storing multiple complaints
3. Displaying complaint records
4. Tracking complaint status
5. Updating complaints when progress is made

---

## 3. Project Objectives

The main objectives of this project are to:

- Apply Python Object-Oriented Programming concepts.
- Create classes and objects representing real-world entities.
- Demonstrate attributes and methods.
- Demonstrate interaction between objects.
- Use a Python list to store multiple complaint objects.
- Create functions for adding and displaying records.
- Implement an instance method.
- Implement a class method using `@classmethod`.
- Validate user input.
- Follow basic Digital Public Goods (DPG) principles.
- Produce reusable and understandable Python code.

---

# 4. System Features

The system provides the following features:

### 4.1 Add Complaint

Users can add a new complaint by entering:

- Citizen ID
- Citizen name
- Community
- Complaint category
- Complaint description

The system automatically generates a complaint ID.

---

### 4.2 Display Complaints

The system displays all complaints currently stored in the program.

Example:

```text
Complaint ID: C1001
Citizen: Mohamed Kamara
Community: Freetown
Category: Road Damage
Description: A large pothole is affecting vehicles and pedestrians.
Status: Pending
```

---

### 4.3 Update Complaint Status

A complaint can have one of three statuses:

```text
Pending
In Progress
Resolved
```

The user selects the desired status using the menu.

---

### 4.4 Input Validation

The system prevents users from submitting empty information.

For example, if the user presses Enter without entering a name:

```text
Enter citizen name:
This field cannot be empty. Please enter a value.
```

The program continues asking until a valid value is entered.

The status menu also validates the user's choice.

If the user enters:

```text
5
```

the program responds:

```text
Invalid choice. Please choose 1, 2, or 3.
```

---

# 5. Object-Oriented Programming Design

The system contains three main classes:

```text
Citizen
   |
   | submits
   ↓
Complaint
   |
   | managed by
   ↓
ComplaintSystem
```

## 5.1 Citizen Class

The `Citizen` class represents a person who submits a complaint.

### Attributes

```python
citizen_id
name
community
```

### Methods

```python
display_info()
update_community()
```

Example:

```python
citizen = Citizen(
    "CT001",
    "Mohamed Kamara",
    "Freetown"
)
```

---

## 5.2 Complaint Class

The `Complaint` class represents a complaint submitted by a citizen.

### Attributes

```python
complaint_id
citizen
category
description
status
```

The default status is:

```text
Pending
```

### Methods

```python
create_complaint()
update_status()
display_info()
```

---

## 5.3 ComplaintSystem Class

The `ComplaintSystem` class manages multiple complaints.

### Attribute

```python
complaints
```

The `complaints` attribute is a Python list.

### Methods

```python
add_complaint()
display_complaints()
find_complaint()
```

---

# 6. Task 1 – Lecture 1: OOP Basics

The assignment requires at least two classes relevant to the selected domain.

This project contains **three classes**:

1. `Citizen`
2. `Complaint`
3. `ComplaintSystem`

This exceeds the minimum requirement.

---

## 6.1 Attributes

Attributes represent the data belonging to an object.

For example:

```python
class Citizen:

    def __init__(self, citizen_id, name, community):
        self.citizen_id = citizen_id
        self.name = name
        self.community = community
```

The Citizen object therefore has:

- `citizen_id`
- `name`
- `community`

---

## 6.2 Methods

Methods represent actions that an object can perform.

For example:

```python
def update_community(self, new_community):
    self.community = new_community
```

This method allows the community associated with a Citizen object to be changed.

---

## 6.3 Object Creation

A Citizen object can be created using:

```python
citizen = Citizen(
    "CT001",
    "Mohamed Kamara",
    "Freetown"
)
```

A Complaint object can be created using:

```python
complaint = Complaint.create_complaint(
    citizen,
    "Road Damage",
    "A large pothole is affecting vehicles."
)
```

---

## 6.4 Object Interaction

The project demonstrates interaction between objects.

A `Complaint` object contains a `Citizen` object:

```python
self.citizen = citizen
```

Therefore, the Complaint object can access information belonging to its Citizen object:

```python
self.citizen.name
```

and:

```python
self.citizen.community
```

This demonstrates how objects can work together to model a real-world relationship.

---

# 7. Task 2 – Lecture 2: Python Data Structures

The assignment requires the use of **one Python data structure**.

This project uses a:

## List

The ComplaintSystem creates an empty list:

```python
self.complaints = []
```

Complaint objects are then added to the list:

```python
self.complaints.append(complaint)
```

Multiple complaints can therefore be stored in the same list.

---

## 7.1 Displaying Records

The program uses a `for` loop to go through the list:

```python
for complaint in self.complaints:
    complaint.display_info()
```

This displays each complaint stored in the system.

---

## 7.2 Adding Records

The `add_complaint()` function creates a new Complaint object and passes it to:

```python
system.add_complaint(complaint)
```

The `add_complaint()` method then stores it in the list:

```python
self.complaints.append(complaint)
```

---

## 7.3 Finding a Record

The program also provides a method for finding a complaint by its ID:

```python
def find_complaint(self, complaint_id):

    for complaint in self.complaints:

        if complaint.complaint_id == complaint_id:
            return complaint

    return None
```

This is used when updating a complaint's status.

---

# 8. Task 3 – Lecture 3: Classes, Methods and DPG Alignment

## 8.1 Instance Method

The project includes the required instance method:

```python
def update_status(self, new_status):
```

It changes the status of a particular Complaint object.

Example:

```python
complaint.update_status("Resolved")
```

The status of that specific complaint becomes:

```text
Resolved
```

---

# 9. Class Method

The assignment requires at least one class method using `@classmethod`.

The project implements:

```python
@classmethod
def create_complaint(cls, citizen, category, description):
    return cls(citizen, category, description)
```

The `@classmethod` decorator makes this a class method.

The `cls` parameter refers to the `Complaint` class.

The method creates a new Complaint object.

Example:

```python
complaint = Complaint.create_complaint(
    citizen,
    "Road Damage",
    "A large pothole is affecting vehicles."
)
```

---

# 10. Automatic Complaint ID

The `Complaint` class uses a class variable:

```python
next_id = 1001
```

When a new complaint is created:

```python
self.complaint_id = f"C{Complaint.next_id}"
```

The number is then increased:

```python
Complaint.next_id += 1
```

Therefore, complaints receive IDs such as:

```text
C1001
C1002
C1003
C1004
```

This helps distinguish between different complaint records.

---

# 11. Input Validation

Input validation was included to make the program more reliable.

The program uses:

```python
def get_required_input(prompt):

    while True:

        value = input(prompt).strip()

        if value:
            return value

        print(
            "This field cannot be empty. "
            "Please enter a value."
        )
```

This ensures that required fields cannot be left blank.

For example:

```text
Enter community:
This field cannot be empty. Please enter a value.
```

The user must enter a value before the program continues.

---

# 12. Status Validation

The system uses a dictionary to map menu choices to valid status values:

```python
status_map = {
    "1": "Pending",
    "2": "In Progress",
    "3": "Resolved"
}
```

The program checks whether the user's choice exists:

```python
if choice in status_map:
```

If the user enters an invalid value such as `5`, the program displays:

```text
Invalid choice. Please choose 1, 2, or 3.
```

This prevents invalid status values from being assigned through the menu.

---

# 13. Digital Public Goods (DPG) Alignment

The assignment requires the project to follow basic Digital Public Goods principles.

## 13.1 Open Source

The project is written in Python and can be uploaded to GitHub.

The source code can be viewed, studied, reused, and improved by other developers and students.

---

## 13.2 Inclusive and Accessible Design

The application uses a simple command-line interface.

It does not require:

- Expensive software
- Special hardware
- A web server
- A database server
- Paid APIs

Only Python 3 is required to run the application.

---

## 13.3 Privacy Respecting

The program avoids collecting sensitive personal information.

It does not request or store:

- Passwords
- Bank details
- Financial information
- Medical records
- National identification numbers
- Authentication credentials

The sample records only contain basic demonstration information.

---

## 13.4 Modular and Reusable

The system is divided into separate classes and functions.

For example:

```text
Citizen
Complaint
ComplaintSystem
add_complaint()
update_complaint_status()
display_menu()
```

This makes the program easier to understand, maintain, and extend.

---

# 14. Program Menu

When the program starts, the following menu is displayed:

```text
==========================================
 CITIZEN COMPLAINT MANAGEMENT SYSTEM
==========================================
1. Add complaint
2. Display all complaints
3. Update complaint status
4. Exit
==========================================
```

The user can select one of the available options.

---

# 15. Example Input

Example of adding a complaint:

```text
Enter your choice: 1

========== ADD COMPLAINT ==========

Enter citizen ID: CT003
Enter citizen name: Abdul Sesay
Enter community: Lumley
Enter complaint category: Street Lighting
Enter complaint description: Several street lights are not working.
```

The program responds:

```text
Complaint added successfully.
Your complaint ID is: C1003
```

---

# 16. Example Output

When the user selects **Display all complaints**:

```text
========== ALL COMPLAINTS ==========

Complaint ID: C1001
Citizen: Mohamed Kamara
Community: Freetown
Category: Road Damage
Description: A large pothole is affecting vehicles and pedestrians.
Status: Pending
------------------------------------

Complaint ID: C1002
Citizen: Mariama Conteh
Community: Kissy
Category: Waste Management
Description: Waste has not been collected regularly in the community.
Status: Pending
------------------------------------
```

---

# 17. Example Status Update

The user can update a complaint:

```text
========== UPDATE STATUS ==========

Enter complaint ID: C1001

Select new status:

1. Pending
2. In Progress
3. Resolved

Choose new status: 2
```

Output:

```text
Complaint status updated successfully.
```

The complaint will now have:

```text
Status: In Progress
```

---

# 18. Project Structure

The GitHub repository can have the following structure:

```text
Citizen-Complaint-Management-System/
│
├── main.py
├── README.md
├── ASSIGNMENT_REPORT.md
├── sample_output.txt
└── .gitignore
```

### `main.py`

Contains the complete Python application.

### `README.md`

Contains project documentation, OOP explanation, DPG alignment, and instructions.

### `ASSIGNMENT_REPORT.md`

Contains the written assignment explanation.

### `sample_output.txt`

Contains examples of program execution.

### `.gitignore`

Contains files and folders that should not be uploaded to GitHub.

---

# 19. How to Run the Program

## Step 1 – Install Python

Install Python 3 on the computer.

## Step 2 – Open the Project

Open the project folder using:

- VS Code
- PyCharm
- IDLE
- Command Prompt/Terminal

## Step 3 – Run the Program

Open the terminal inside the project folder and enter:

```bash
python main.py
```

On some systems, you may use:

```bash
python3 main.py
```

No external Python packages are required.

---

# 20. GitHub Submission

The project can be uploaded to a GitHub repository.

Suggested repository name:

```text
Citizen-Complaint-Management-System
```

The repository should contain:

```text
main.py
README.md
ASSIGNMENT_REPORT.md
sample_output.txt
.gitignore
```

The README explains:

- The problem
- Objectives
- Classes
- Attributes
- Methods
- Data structure
- Class method
- Input validation
- DPG alignment
- How to run the program
- Example output

---

# 21. Screenshots for Hardcopy

For the physical assignment submission, screenshots should be taken showing the program running.

Recommended screenshots:

### Screenshot 1 – Main Menu

Show:

```text
CITIZEN COMPLAINT MANAGEMENT SYSTEM
1. Add complaint
2. Display all complaints
3. Update complaint status
4. Exit
```

### Screenshot 2 – Display Complaints

Show the existing complaint records.

### Screenshot 3 – Add Complaint

Show a new complaint being entered successfully.

### Screenshot 4 – Input Validation

Show what happens when an empty field is submitted.

Example:

```text
Enter citizen name:
This field cannot be empty. Please enter a value.
```

### Screenshot 5 – Update Status

Show a complaint changing from:

```text
Pending
```

to:

```text
In Progress
```

### Screenshot 6 – Invalid Status Choice

Show an invalid choice such as `5` being rejected:

```text
Invalid choice. Please choose 1, 2, or 3.
```

---

# 22. Future Improvements

Although this project focuses on the basic OOP requirements of PROG211, a larger version could include:

- Database integration
- User authentication
- Government department accounts
- Complaint search
- Complaint filtering
- Email notifications
- SMS notifications
- Photo evidence
- GPS/location information
- Complaint priority levels
- Government department assignment
- Reports and statistics
- Web interface
- Mobile application

These features are not included in this version because the purpose of the assignment is to demonstrate fundamental Python OOP concepts.

---

# 23. Conclusion

The Citizen Complaint Management System demonstrates the major requirements of the PROG211 Object-Oriented Programming 1 assignment.

The project includes:

- Three classes
- Attributes
- Objects
- Object interaction
- Instance methods
- A class method using `@classmethod`
- A Python list data structure
- Functions for adding and displaying records
- Input validation
- Status validation
- Digital Public Goods principles
- GitHub-ready documentation
