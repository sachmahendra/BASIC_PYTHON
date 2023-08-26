class student:
      def __init__(self,a,b):
          self.name=a
          self.address=b
          print("constructor invoked")
          def display_student_details(self):
            return self.name,self.address

class Teacher(student):
  pass

t1=Teacher("ashish","delhi")

print(t1.name)
print(t1.address)