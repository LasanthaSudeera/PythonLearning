employees = {}

noEmployees = int(input("Enter the number of employees: "))
for i in range(noEmployees):
    name = input("Enter the name of the employee {}: ".format(i))
    salary = input("Enter the salary of the employee {}: ".format(i))
    employees[name] = salary

print("Enter the employee name to get the salary...")
while True:
    getName = input("Enter the name of the employee to look for: ")
    salary = employees.get(getName, -1)
    if salary == -1:
        print("Employee does not exists!")
    else:
        print("Salary of the employee is $", salary)
    
    choice = input("Do you want to look for another employee salary? If YES Type 'Yes' and press enter \n -> ")
    if not choice == "Yes":
        break