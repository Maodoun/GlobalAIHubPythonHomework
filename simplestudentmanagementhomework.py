#Global Ai Hub Ödev #Simple Student Management System:

print("**********Welcome to Student Management System*********")

namelist = ["metehan gül"]

check = False
lesson_list = []
signin_attempt = 3

resultofexams = {"midterm": 90, "final": 40, "project":50}

def calculate_score():
    score = (resultofexams["midterm"]*30 + resultofexams["final"]*50 + resultofexams["project"]*20)/100
    return score

while range(3):
    name1 = str(input("Please confirm your name&surname: "))
    if name1 == namelist[0]:
        print(f"welcome {namelist[0]}")
        for i in range(5):
            fquit = input("Press q for complete or enter any key for adding lessons: ")
            i += 1
            if fquit == "q":
                break
            lessons = input(f"Please choose lesson {i} : ")
            lesson_list.append(lessons)
            check = True
    
        break
    else:
        signin_attempt -= 1
        if signin_attempt == 0:
            print("Plese try again later.")
            break
#lesson list sayı kontrolü
if len(lesson_list) < 3:
    print("You are failed in class.")

if check == True:
    print("".center(20,"-"))
    print("Please select lesson for calculate your grade")
    print(f"Your lessons\n1-{lesson_list[0]}\n2-{lesson_list[1]}\n3-{lesson_list[2]}\n4-{lesson_list[3]}\n5-{lesson_list[4]}")
    lessonNum = int(input("Choose your lesson number:"))
    while True:    
        if lessonNum < 1 and lessonNum > 5:
            print("You must enter number of list")
        else:
            grade = calculate_score()
            if grade < 30:
                print(f"Your grade is {grade}:FF\nYou did not pass this lesson.")
            elif grade >= 30 and grade < 50:
                print(f"Your grade is {grade}:DD ")
            elif grade >= 50 and grade < 70:
                print(f"Your grade is {grade}:CC ")    
            elif grade >= 70 and grade < 90:
                print(f"Your grade is {grade}:BB ")
            elif grade > 90:
                print(f"Your grade is {grade}:AA")
        break


        
