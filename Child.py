class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.vaccination_schedule = []
        self.vaccination_history = []

    def add_vaccination(self, vaccine_name, date):
        self.vaccination_schedule.append((vaccine_name, date))

    def complete_vaccination(self, vaccine_name):
        for vaccine in self.vaccination_schedule:
            if vaccine[0] == vaccine_name:
                self.vaccination_history.append(vaccine)
                self.vaccination_schedule.remove(vaccine)
                break

class VaccinationSystem:
    def __init__(self):
        self.children = []

    def register_child(self, name, age):
        child = Child(name, age)
        self.children.append(child)
        print(f"Child {name} registered successfully.")

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def view_child_information(self, name):
        child = self.find_child(name)
        if child:
            print(f"Name: {child.name}, Age: {child.age}")
            print("Vaccination Schedule:")
            for vaccine in child.vaccination_schedule:
                print(f"  {vaccine[0]} on {vaccine[1]}")
            print("Vaccination History:")
            for vaccine in child.vaccination_history:
                print(f"  {vaccine[0]} completed on {vaccine[1]}")
        else:
            print("Child not found.")

    def schedule_appointment(self, name, vaccine_name, date):
        child = self.find_child(name)
        if child:
            child.add_vaccination(vaccine_name, date)
            print(f"Appointment for {vaccine_name} scheduled on {date} for {name}.")
        else:
            print("Child not found.")

    def view_appointments(self, name):
        child = self.find_child(name)
        if child:
            print(f"Upcoming Vaccination Appointments for {child.name}:")
            for vaccine in child.vaccination_schedule:
                print(f"  {vaccine[0]} on {vaccine[1]}")
        else:
            print("Child not found.")

def main_menu():
    system = VaccinationSystem()

    while True:
        print("\nChild Vaccination Management System")
        print("1. Register Child")
        print("2. View Child Information")
        print("3. Schedule Vaccination Appointment")
        print("4. View Vaccination Appointments")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter child's name: ")
            age = int(input("Enter child's age: "))
            system.register_child(name, age)
        elif choice == '2':
            name = input("Enter child's name: ")
            system.view_child_information(name)
        elif choice == '3':
            name = input("Enter child's name: ")
            vaccine_name = input("Enter vaccine name: ")
            date = input("Enter appointment date (dd/mm/yyyy): ")
            system.schedule_appointment(name, vaccine_name, date)
        elif choice == '4':
            name = input("Enter child's name: ")
            system.view_appointments(name)
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
