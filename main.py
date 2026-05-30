import json
import random
from datetime import datetime
name =input("Enter your name: ")
print("\nHello", name)
print("Welcome to Smart Student Assistant")
with open("tips.json", "r") as f:
    data =json.load(f)
file=open("output.txt", "a")
while True:
    print("\n**** SMART STUDENT ASSISTANT ****")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date and Time")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        tip=random.choice(data["study_tips"])
        print("\nStudy Tip:")
        print(tip)
        file.write("Study Tip: " + tip + "\n")

    elif choice == 2:
        quote=random.choice(data["motivation_quotes"])
        print("\nMotivation Quote:")
        print(quote)
        file.write("Motivation Quote: " + quote + "\n")
    elif choice == 3:
        current_time=datetime.now()
        print("\nCurrent Date and Time:")
        print(current_time)
        file.write("Date and Time: " + str(current_time) + "\n")
    elif choice == 4:
        print("\nThank You for using Smart Student Assistant!")
        break
    else:
        print("\nInvalid Choice! Please try again.")
file.close()