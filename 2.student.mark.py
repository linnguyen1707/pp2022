from datetime import datetime

class StudentMark():
    class StudentCount():
        def studentcount(student):
            student.count = int (input (" Num of students: "))
            return student.count

        def StudentInformation(student):
            student.studentID = input ("Student's ID: ")
            student.studentname = input ("Student's Name: ")
      
            while True:
              try:
                studentdob = input ("Enter student's date of birth dd/mm/yyyy: ")
                student.dob = datetime.strptime(studentdob, "%d/%m/%Y")
              except ValueError:
                print("\033[1;31;40m Wrong date of birth format! \033[0m")
              break 
            dobd = str(student.dob.day) + "/" + str(student.dob.month) + "/" + str(student.dob.year)
            return student.studentID, student.studentname, student.dob
            
        def StudentList(student):
            studentList = []
            for i in range(student.count):
                studentList.append ((student.studentID, student.studentname, student.dob))
                studentList.sort()       
            for s in studentList:
                print (f"Student list: id: {s[0]} Name: {s[1]} Date of birth: {s[2]}") 
            
    class CourseCount():
        def coursecount (course):
            course.count = int (input ("Number of courses: "))

        def CourseInformation (course):
            course.courseID = input ("Course's id: ")
            course.coursename = input ("Course's name: ")
            return course.courseID, course.coursename
            
        def CourseList(course):
            coursList = []
            for i in range(course.count):
                coursList.append ((course.courseID, course.coursename))
                coursList.sort()       
            for c in coursList:
                print (f"Course list: id: {c[0]} Name: {c[1]}")                

    class StudentMark(StudentCount,CourseCount):            
        def studentMarkCount(m):
            m.count = int (input ("How many student marks do you want? "))
                    
        def studentMark(m):
            m.CourseInformation()
            m.StudentInformation()
            m.mark = float(input("Enter student's mark: "))
            sml = []
            for i in range(m.count):
                sml.append((m.studentname,m.mark))
                sml.sort()
            for l in sml:
                print(f"Student {l[0]} has {l[1]} points")