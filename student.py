import os
import json
# using a while loop to create a menu for the user to interact with the program
while True:
    # user input to select an option from the menu
    print("1. Add student & Grade")
    print("2. View all student")
    print("3. Calculate average grade")
    print("0. Exit")

    choice = input("Select an option: ")
# using if statements to execute the corresponding code based on the user's choice
    if choice == "1":
        # getting the student's name and score from the user
        Name = input("Enter student name: ").lower()
        Score = float(input("Enter student score: "))
# checking if the "pupil.json" file exists, if it does, it loads the existing data, otherwise it creates a new dictionary to store the data
        if os.path.exists("pupil.json"):
            with open("pupil.json", "r") as file:
                pupil = json.load(file)

        else:
            # if the file does not exist, it creates a new dictionary with a "Grade" key that contains an empty list to store the student data
            pupil = {"Grade": []}
# it creates a new entry for the student with their name and score, and appends it to the "Grade" list in the pupil dictionary. Then it saves the updated data back to the "pupil.json" file.
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
# it calculates the average score by iterating through the "Grade" list in the pupil dictionary, summing up the scores and counting the number of valid scores. Finally, it prints the average score rounded to two decimal places.
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



            

            
