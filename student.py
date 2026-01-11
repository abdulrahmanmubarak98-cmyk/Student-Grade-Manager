import json
while True:
    print("menu")
    print("1. Add student & grade")
    print("2. view all students")
    print("3. calculate average grade")
    print("4. exit")

    choice = input("select an option (1/2/3/4): ")  
    if choice == "1":
        Name = input("Enter student name: ").lower()
        Grade = float(input("Enter student grade: "))
## using json to store student data
        file = open("student.json", "r")
        student = json.load(file)
        file.close()

        student[Name] = Grade

        file = open("student.json", "w")
        json.dump(student, file)
        file.close()
## using json to read student data 
    elif choice == "2":
        file = open("student.json", "r")
        student = json.load(file)
        for Name, Grade in student.items():
            print(f"{Name}: {Grade}")
        file.close()
      ## calculate average grade  
    elif choice == "3":
        file = open("student.json", "r")
        student = json.load(file)
        total = sum(student.values())
        average = total / len(student) if student else 0
        print(f"Average grade: {average}")
        file.close()
## exit the app
    elif choice == "4":
        print("Thank you for using this app.")
        break

    else:
        print("invalid option")