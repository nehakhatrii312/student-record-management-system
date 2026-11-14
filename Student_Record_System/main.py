import json
file = "Students.json"

def load_data():
    try:
      with open(file,"r") as f:
        return json.load(f)
    except FileNotFoundError:
      return[]
    except json.JSONDecodeError:
      return[]

def save_data(Students):
  with open(file,"w") as f:
    json.dump(Students,f,indent=4)

def add_student(Students):
  name = input("Enter student name: ")
  course = input("Enter student course:")
  try:
    marks = int(input("Enter marks:"))
  except ValueError:
    print("Marks must be a number:")
    return

  if len(Students) == 0:
    new_id = 1
  else:
    new_id = Students[-1]["ID"] + 1

  student = {
      "ID": new_id, "Name": name, "Course": course, "Marks": marks}
  Students.append(student)
  save_data(Students)
  print("Student added succesfully!")

def view_students(Students):
  if len(Students) == 0:
    print("No records found!")
    return 
  print("---/Students records/---")
  for s in Students:
    print(f"ID: {s['ID']}, Name: {s['Name']}, Course: {s['Course']}, Marks: {s['Marks']}")

def update_student(Students):
  try:
    student_id = int(input("Enter student ID to update:"))
  except ValueError:
    print("Invalid input. Please enter a valid student ID.")
    return

  for s in Students:
    if s["ID"] == student_id:
      new_name = input("New name (press Enter to keep old): ")
      new_course = input("New course (press Enter to keep old): ")
      new_marks = input("New marks (press Enter to keep old): ")
      if new_name != "":
                s["name"] = new_name
                if new_course != "":
                 s["course"] = new_course
                 if new_marks != "":
                    try:
                        s["marks"] = int(new_marks)
                    except ValueError:
                     print("Invalid marks, old marks kept.")        
    def save_data(Students):
            print("Student updated successfully.")
            return

    print("Student not found.")

def delete_student(Students):
        try:
         student_id = int(input("Enter student ID to delete: "))
        except ValueError:
            print("ID must be a number.")
        return

        for s in Students:
          if s["id"] == student_id:
            Students.remove(s)
            save_data(Students)
            print("Student deleted successfully.")
            return

        print("Student not found.")
def main():
      Students = load_data()

      while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student(Students)
        elif choice == "2":
            view_students(Students)
        elif choice == "3":
            update_student(Students)
        elif choice == "4":
            delete_student(Students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
main()