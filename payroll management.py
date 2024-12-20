class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name  
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_basic_salary(self):
        regular_hours = min(self.hours_worked, 40)
        basic_salary = self.hourly_rate * regular_hours
        return basic_salary, regular_hours

    def calculate_overtime_pay(self, regular_hours=40, overtime_rate=1.5):
        overtime_hours = max(0, self.hours_worked - regular_hours)
        overtime_pay = overtime_hours * self.hourly_rate * overtime_rate
        return overtime_pay, overtime_hours

    def calculate_deduction(self, salary, tax_rate=0.1, insurance_rate=0.05, retirement_rate=0.03):
        tax_deduction = salary * tax_rate
        insurance_deduction = salary * insurance_rate
        retirement_deduction = salary * retirement_rate
        total_deduction = tax_deduction + insurance_deduction + retirement_deduction
        return total_deduction, tax_deduction, insurance_deduction, retirement_deduction

    def bonus_calculation(self, basic_salary, bonus_percentage=0.05):
        bonus = basic_salary * bonus_percentage
        return bonus

    def calculate_net_salary(self, basic_salary, overtime_pay, deduction, bonus):
        net_salary = basic_salary + overtime_pay + bonus - deduction
        return net_salary

    def calculate_monthly_salary(self):
        weekly_salary = self.hourly_rate * self.hours_worked
        monthly_salary = weekly_salary * 4.33  
        return monthly_salary

    def generate_payroll(self, bonus_percentage=0.05, tax_rate=0.1, insurance_rate=0.05, retirement_rate=0.03):
        basic_salary, regular_hours = self.calculate_basic_salary()
        overtime_pay, overtime_hours = self.calculate_overtime_pay()
        total_deduction, tax_deduction, insurance_deduction, retirement_deduction = self.calculate_deduction(basic_salary, tax_rate, insurance_rate, retirement_rate)
        bonus = self.bonus_calculation(basic_salary, bonus_percentage)
        net_salary = self.calculate_net_salary(basic_salary, overtime_pay, total_deduction, bonus)
        monthly_salary = self.calculate_monthly_salary()

        payroll_details = {
            'Employee Name': self.name,
            'Basic Salary': basic_salary,
            'Overtime Pay': overtime_pay,
            'Total Hours Worked': self.hours_worked,
            'Overtime Hours': overtime_hours,
            'Total Deduction': total_deduction,
            'Tax Deduction': tax_deduction,
            'Insurance Deduction': insurance_deduction,
            'Retirement Deduction': retirement_deduction,
            'Bonus': bonus,
            'Net Salary': net_salary,
            'Monthly Salary': monthly_salary
        }
        return payroll_details


employee_name = input("Enter the employee's name: ")
hourly_rate = float(input("Enter the hourly rate ($): "))
hours_worked = float(input("Enter the total hours worked in a week: "))


employee = Employee(employee_name, hourly_rate, hours_worked)


payroll_details = employee.generate_payroll()


print("\nPayroll details:")
for key, value in payroll_details.items():
    if isinstance(value, (int, float)):
        print(f"{key}: ${value:.2f}")
    else:
        print(f"{key}: {value}")
