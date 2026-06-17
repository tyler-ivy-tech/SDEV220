'''
Tyler Howard
module_2_lab.py

This app accepts student names and GPAs and determines whether they 
qualify for the Dean's List or the Honor Roll. The app includes a 
sentinel value of "ZZZ" for exiting.
'''

SENTINEL : str = "ZZZ"

def main() -> None:
    while True:
        last_name = input("Enter student's last name (enter 'ZZZ' to exit): ")
        if last_name == SENTINEL:
            print("Program exited.")
            break
        first_name = input("Enter student's first name: ")
        student_gpa = float(input("Enter student's GPA: "))
        
        if student_gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif student_gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")

if __name__ == "__main__":
    main()