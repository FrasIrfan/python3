eng, urdu, math, comp, isl = 0, 0, 0, 0, 0
obtainedMarks, marksPerc = 0.0, 0.0
totalMarks = 500

# eng = int(input("Enter marks for English: "))
# urdu = int(input("Enter marks for Urdu: "))
# math = int(input("Enter marks for Mathematics: "))
# comp = int(input("Enter marks for Computer: "))
# isl = int(input("Enter marks for Islamiyat: "))

while True:
    try:
        eng = int(input("Enter marks for English: "))
        if eng > 100:
            print("Enter marks below 100")
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        urdu = int(input("Enter marks for Urdu: "))
        if urdu > 100:
            print("Enter marks below 100")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        math = int(input("Enter marks for Mathematics: "))
        if math > 100:
            print("Enter marks below 100")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        comp = int(input("Enter marks for Computer: "))
        if comp > 100:
            print("Enter marks below 100")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

while True:
    try:
        isl = int(input("Enter marks for Islamiyat: "))
        if isl > 100:
            print("Enter marks below 100")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

obtainedMarks = eng + urdu + comp + math + isl
marksPerc = (obtainedMarks / totalMarks) * 100


print("Percentage is", marksPerc)

if marksPerc >= 33:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you failed the test!")
