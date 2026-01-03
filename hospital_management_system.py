patients = []

def add_patient():
    name = input("Enter patient name: ")
    ailment = input("Enter ailment: ")
    patients.append({"name": name, "ailment": ailment})
    print("Patient record added")

def view_patients():
    if not patients:
        print("No patient records found")
    else:
        for patient in patients:
            print(patient["name"], "-", patient["ailment"])

def main():
    while True:
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
