import os
import json

while True:
    print("1. Add student & Grade")
    print("2. View all student")
    print("3. Calculate average grade")
    print("0. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        Name = input("Enter student name: ").lower()
        Score = float(input("Enter student score: "))

        if os.path.exists("pupil.json"):
            with open("pupil.json", "r") as file:
                pupil = json.load(file)

        else:
            pupil = {"Grade": []}

        new_entry = {
                "Name": Name,
                "Score": Score
            }
        pupil["Grade"].append(new_entry)
        print("Updated")

        with open("pupil.json", "w") as file:
            json.dump(pupil, file, indent=4)

    elif choice == "2":
        with open("pupil.json", "r") as file:
            pupil = json.load(file)

        for student in pupil["Grade"]:
            if "name" in student and "score" in student:
                print(f"name: {student['name']}, score: {student['score']}")

    elif choice == "3":
        with open("pupil.json", "r") as file:
            pupil = json.load(file)

        total = 0
        count = 0

        for student in pupil["Grade"]:
            score = student.get("score")

            if isinstance(score, (int, float)):
                total += score
                count += 1

        if count > 0:
            average = total / count
            print(f"Average score: {round(average, 2)}")
        else:
            print("No valid scores found")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option")



            

            
