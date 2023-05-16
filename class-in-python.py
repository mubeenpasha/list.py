class Student():
     def __init__(self, fname, lname,):
      self.fname = fname
      self.lname = lname
      self.mail = f"{fname} + {lname} + @genuni.co.uk"
#print the students first name,last name and email 
student_detail= Student("Billal", "khallid")
print(student_detail.fname)
print(student_detail.lname)
print(student_detail.mail)

