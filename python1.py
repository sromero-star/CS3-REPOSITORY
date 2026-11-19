class Student:
  def __init__ (self, name, grade):
    self.__name = name
    self.__grade = grade

  #GETTER
  def get_grade(self):
    return self.__grade

  #SETTER
  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print ("Invalid Grade!")

#main code
student1 = Student("Samantha", 95)
print(student1.get_grade())
student1.set_grade(105)