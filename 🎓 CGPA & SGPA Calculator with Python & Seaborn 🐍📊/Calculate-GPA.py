import os 
import matplotlib.pyplot as plt
import seaborn as sns

def C_CGPA():
    os.system("cls")
    print("***************** Calculate Your Calculate Your CGPA ****************")
    cgpa=(int(input("Enter your Total Semester which you calculate your CGPA: ")))
    cal_gpa=[]
    gpas=0
    fina_cgpa=0
    for var in range(1,cgpa+1):
        gpa=(float(input(f"your {var} Semester CGPA is: ")))
        cal_gpa.append(gpa)
        gpas+=gpa
    print("Your Overall CGPA List is:",cal_gpa)
    print(gpas)
    fina_cgpa=gpas/cgpa
    os.system('cls')
    print("***********************************************************************")
    print("                      Your CGPA is ",fina_cgpa)
    print("")
    print("                                                     ***Graph Represenatation Delay to Process***")

    again=int(input("If You Want Again Calaulate your CGPA press('1') Otherwise Press('0'): "))
    if again==1:
        return True
    elif again==0:
        print("Your Pragram is Terminate:")
        exit()
    else:
        print("You Enter Wrong Number:")


def C_SGPA(): 
    os.system("cls")
    print("***************** Calculate Your Calculate Your SGPA ****************") 
    subject=int(input("Enter Your Total Subject:"))
    
    # for var in range(1,subject+1):
    #     var=str(input(f"Enter your "{var}"st subject Credit Hours:"))
    #     print("you entered",var)
        # print(cgpa)
    credits=[]
    grades=[]
    point=[]
    total_points=0
    total_credits=0
    for var in range(1, subject+1):
        credit = int(input(f"Enter your {var} subject Credit Hours: "))
        grade=str(input(f"Enter your {var}st subect grade: (A, A-, B+, ...):"))
        credits.append(credit)
        grades.append(grade)
        # if grade>='A','A+':
        if grade=="A":
            points=4
        elif grade=="A-":
            points=3.7
        elif grade=="B+":
            points=3.3
        elif grade=="B-":
            points=2.7
        elif grade=="B":
            points=3.0
        elif grade=="C+":
            points=2.3
        elif grade=="C":
            points=2.0
        elif grade=="C-":
            points=1.7
        elif grade=="F":
            points=0.00
        else:
            points=0
        point.append(points)
        total_points+=credit*points
        total_credits+=credit


    total_credit=sum(credits) 
    sgpa=total_points/total_credits   
    print("You Entered", credit)
    print("Your Total Credit Hour is:",credits)
    print("Your Total Credit Hour is:",total_credit)
    print("Your Achievements Grades is:",grades)
    print(point)
    print("\n🎓 Congratulations! Your CGPA has been successfully calculated.",round(sgpa,2))
    print("Keep working hard and aim higher each semester!")



    print("*********************Choose*********************")
    print("1. Bar Plot")
    print("2. Line Plot")
    print("3. Scatter Plot")
    print("4. Pie Chart ")

    chose=int(input("Choose Your Best Plot: "))
    plt.figure()

    if chose == 1:  # Bar Plot
        sns.barplot(x=[f"Sub {i+1}" for i in range(subject)], y=points)
        plt.xlabel("Subjects")
        plt.ylabel("Grade Points")
        plt.title("Bar Plot: Grade Points per Subject")

    elif chose == 2:  # Line Plot
        plt.plot([f"Sub {i+1}" for i in range(subject)], points, marker="o")
        plt.xlabel("Subjects")
        plt.ylabel("Grade Points")
        plt.title("Line Plot: Trend of Grade Points")

    elif chose == 3:  # Scatter Plot
        plt.scatter(credits, points, s=100, c="blue")
        plt.xlabel("Credit Hours")
        plt.ylabel("Grade Points")
        plt.title("Scatter Plot: Credits vs Grade Points")

    elif chose == 4:  # Pie Chart
        unique_grades = list(set(grades))
        counts = [grades.count(g) for g in unique_grades]
        plt.pie(counts, labels=unique_grades, autopct="%1.1f%%")
        plt.title("Pie Chart: Grade Distribution")

    else:
        print("Invalid choice, no plot shown.")
        return

    plt.show()
    again=int(input("If You Want Again Calaulate your CGPA press('1') Otherwise Press('0'): "))
    if again==1:
        return True
    elif again==0:
        print("Your Pragram is Terminate:")
        exit()
    else:
        print("You Enter Wrong Number:")

    def exits():
        exit()

while True:
    os.system('cls')
    print("*****************************************************************************")
    print("                     Instant Calculate Your GPA                    ")
    print("*****************************************************************************")

    print("1.Calculate Your Current CGPA")
    print("2.Calculate Your SGPA")
    print("3.Exit")




    choose=int(input("Enter your choice: "))
    def switch_example(choose):
        match choose:
            case 1:
                C_CGPA()
            case 2:
                C_SGPA()
            case 3:
                exit()
            case _:
                os.system('cls')
                print("You Enter Wrong Number")
                print("You want again vist then press 1 otherwise press 0 and termiante:")

                press=int(input("Press 1 or 0: "))
                if press==1:
                    print("Waiting for Advancement in Program")
                else:
                    print("Program Terminate")
                    print()

    switch_example(choose)
