class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  #sort the list of thestudents in desending order of cgpa
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse = True)

  #sntax lambda arg: exp
  return sorted_students

students = [
     Student("sangeetha", "A123", 7.8),
     Student("pavi", "A124", 8.8),
     Student("nivi", "A125", 9.8)
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, Cgpa: {}".format(student.name, 
  student.roll_number, student.cgpa))