class employee():

    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@company.com")
        employee.num_of_emps +=1

    def fullname(self):
        return (self.first + ' ' + self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.10)

emp_1 = employee("chaitan", "hanmanthu", 10000)
emp_2 = employee("sach", "in", 1000)

print emp_1(__dict__)
print emp_1.fullname()
print employee.fullname(emp_1)
