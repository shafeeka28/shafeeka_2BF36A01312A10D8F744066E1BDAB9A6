class student:

  def __init__(self,name,roll_no,cgpa):
    self.name = name
    self.roll_no = roll_no
    self.cgpa = cgpa

  def sort_students(student_list):
    sorted_students=sorted(student_list,
                           key= lambda 
                           student:student.cgpa,
                           reverse=true)
 
    return sorted_students  

    students=[student("hari","A101",8.9),
         student("anu","A102",8.7),
         student("abi","A103",9.2),
          student("ari","A106",9.9)]

    sorted_students = sort_students(students)

    for student in sorted_students:
        print("NAME: {},ROLL_NO: {},CGPA:{}"
            .format(student.name,
                    student.roll_no,
                                    student.cgpa))


