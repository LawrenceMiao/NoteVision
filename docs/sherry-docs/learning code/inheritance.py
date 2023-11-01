class Person: # parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  
  def PrintInfo(self):
    print(self.firstname + " " + self.lastname, end = "")

class Professor(Person): # child class
  def __init__(self, fname, lname, depname):
    super().__init__(fname, lname)
    self.dep = depname

  def PrintDep(self):
    print("Professor {}'s department is {}.".format(self.lastname, self.dep))

class Doctor(Person): # child class
  def __init__(self, fname, lname, hname):
    super().__init__(fname, lname)
    self.hospital = hname

  def PrintHospital(self):
    print("Dr. " + self.lastname + " works at " + self.hospital)

class CanTeach(Professor):
   def __init__(self, fname, lname, depname, classname):
        super().__init__(fname, lname, depname)
        print("{} is a {} professor that teaches {}.".format(self.lastname, depname, classname))

if __name__ == '__main__':
  p1 = Person("Emma", "Smith")
  p1.PrintInfo()

  print()

  p2 = Person("Sophia", "Miller")
  p2.PrintInfo()

  print()

  p3 = Professor("Wes", "Turner", "Computer Science")
  p3.PrintDep()

  p4 = Professor("Konstantin", "Kuzmin", "Computer Science")
  p4.PrintInfo()

  print()

  p5 = Doctor("Ava", "Jones", "Samaritan Hospital")
  p5.PrintHospital()
  p5.PrintInfo()
  print()

  p6 = CanTeach("Mia", "Brown", "Math", "Calculus 1")
  p6.PrintDep()