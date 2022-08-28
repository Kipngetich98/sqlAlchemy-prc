import pymysql #Access database properly
pymysql.install_as_MySQLdb()
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""Main steps to create ORM
-Create Engine
- Create Session
- Create Table
-Migrate

"""
#To create Engine
url = "mysql://root:password:3306/db"
engine = create_engine(url, echo = False)

#To create Session

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

# table inheriting Base
class Employee(Base):
  __tablename__ = "Employee"
  employee_id = Column(Integer, primary_key = True)
  name = Column(String(100))
  address = Column(String(100))
# migrating table
Base.metadata.create_all(engine)

# Instances of class student
EM1 = Employee(Emp_id = 1, name = "Vincent Kirui", address = "Vincent")
EM2 = Employee(Emp_id = 2, name = "Vinnie Kip", address = "Kip")
EM3 = Employee(Emp_id = 3, name = "Kipngetich Kirui", address = "Kipngetich")
EM4 = Employee(Emp_id = 4, name = "Hilaary Kip", address = "Hilaary")

# Adding the data to session
session.add_all([EM1, EM2, EM3, EM4])

# commiting to the session
session.commit()



# Showing all data
Employees = session.query(Employee)
for E in Employees:
    print(E.Emp_id, E.name, E.address)

# Showing data in an order
Employees = session.query(Employee).order_by(Employee.name)
for E in Employees:
    print(E.Emp_id, E.name, E.address)

# Getting data by filtering
employee = session.query(Employee).filter(Employee.name == "Bishal Pathak").first()
print(employee.Emp_id, employee.name)

emp = session.query(Employee).filter(Employee.Emp_id == 1).first()
emp.name = "Faith Chepkirui"
session.commit()

print(emp.Emp_id, emp.name)