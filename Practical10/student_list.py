class Student:
  def __init__(self,first_name,last_name,programme):
    self.first_name = first_name
    self.last_name = last_name
    self.programme = programme
  def f(self):
    print(self.first_name + ' ' + self.last_name + ' ' + self.programme)
c = Student('Lu','Jingrui','BMI')
c.f()
