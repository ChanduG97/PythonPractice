class Organization:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Function to get organization and employee details based on user input
def get_organization_details():
    organizations = []
    while True:
        org_name = input("Enter organization name (or 'exit' to finish): ")
        if org_name.lower() == 'exit':
            break

        org = Organization(org_name)
        organizations.append(org)

        while True:
            emp_name = input(f"Enter employee name for {org_name} (or 'done' to finish): ")
            if emp_name.lower() == 'done':
                break

            emp = Employee(emp_name)
            org.add_employee(emp)

    return organizations

# Function to display organization and employee details
def display_organization_details(organizations):
    for org in organizations:
        print(f"\nOrganization: {org.name}")
        print("Employees:")
        for employee in org.employees:
            print("-", employee.name)
        print(f"Total Employees: {len(org.employees)}")

if __name__ == "__main__":
    organizations = get_organization_details()
    display_organization_details(organizations)
