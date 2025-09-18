class person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age

    def show_details(self):
        print("name:",self.name)
        print("age:",self.age)

class employee(person):        
    def __init__(self,name,age,employeeid):
        person.__init__(self,name, age)
        


        self.employeeid=employeeid

        def show_details(self):
            print(f"""employee name:{self.name}
employee age:{self.age}
employee id:{self.employeeid}""")

class part_time (person):
    def __init__(self,name,age,working_hours):
        person.__init__(self,name,age)

        self.working_hours=working_hours

        def show_details(self):
            print(f"""part time name:{self.name}
part time age:{self.age}
part time working hours:{self.working_hours}""")

class consultant (employee,part_time):
    def __init__(self,name,age,employeeid,working_hours,project_name):
        employee.__init__(self,name,age,employeeid)
        part_time.__init__(self,name,age,working_hours)


        self.project_name=project_name
        

    def show_details(self):
        print(f"""consultant name:{self.name}
consultant age:{self.age}
consultant employee id:{self.employeeid}
consultant working hours:{self.working_hours}
consultant project name:{self.project_name}""")




prs=person("ali",21)
prs.show_details()

emp=employee("karthik",21,109)
emp.show_details() 

par=part_time("biju",21,8.30)
par.show_details()

con=consultant("hassan",21,108,8.30,"css")
con.show_details()





    

        


