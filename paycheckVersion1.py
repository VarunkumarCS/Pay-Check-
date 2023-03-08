from tabulate import tabulate
from pprint import pprint as pp
from datetime import datetime as dt
import time

print()
#To Print the name of the Employee
name = (input("Enter the employee name: "))

#To print the start date of the Employee
start_date = input("Enter a date when the pay period started (in the format MM/DD/YYYY) : ")
date_obj = dt.strptime(start_date, '%m/%d/%Y')

#To print the end date of the Employee
end_date = input("Enter a date when the pay period started (in the format MM/DD/YYYY) : ")
date_obj = dt.strptime(end_date, '%m/%d/%Y')

#To print the gross wages
Gross_wages = int(input("Enter the gross wage of the employee: "))

#Tax Deduction
if Gross_wages > 70000:
    Federal_Tax = 10000
    State_Tax = 3000

    tax_deduction = (Federal_Tax + State_Tax)
    Gross_Wages_After_Tax_Deduction = (Gross_wages - tax_deduction)
    
elif Gross_wages <= 70000:
    Federal_Tax = 8168
    State_Tax = 2321
    tax_deduction = (Federal_Tax + State_Tax)
    Gross_Wages_After_Tax_Deduction = (Gross_wages - tax_deduction)
    
elif 70000 >= Gross_wages <= 65000:
    Federal_Tax = 7288
    State_Tax = 1332
    tax_deduction = Gross_wages - (Federal_Tax + State_Tax)
    Gross_Wages_After_Tax_Deduction = (Gross_wages - tax_deduction)
    
else:
    print("Enter the valid amount")

#Employee Benefits Deduction
benefits = input("Is the Employee taking benefits (enter 'yes' for the employee benefit deduction) or (enter 'no')? ")
if benefits == "yes":
    Employee_Benefits = 100
    Gross_Wages_After_Tax_And_EmployeeBenefitDeduction = (Gross_wages - (tax_deduction + Employee_Benefits))
    
elif benefits == "no":
    Employee_Benefits = 0
    Gross_Wages_After_Tax_And_EmployeeBenefitDeduction = (Gross_wages - tax_deduction)

else:
    print("Invalid input. Please enter either 'Yes' or 'No'.")

#Net Pay
net_pay = Gross_Wages_After_Tax_And_EmployeeBenefitDeduction
print()

#Make a Table
pp(f"The Information of the Employee is")
time.sleep(1)
data= {'Name': [name], 
       'Starting Date' :[start_date],
       'Ending Time' :[end_date],
       'Gross Wage' : [Gross_wages], 
       'Gross Wage after Tax Deduction':[Gross_Wages_After_Tax_Deduction], 
       'Gross Wage after Tax and Employee Benefit Deduction': [Gross_Wages_After_Tax_And_EmployeeBenefitDeduction], 
       'Take Home' : [net_pay]}

print(tabulate(data, headers=['Name','Starting Date','Ending Time','Gross Wage','Gross Wage after Tax Deduction','Gross Wage after Tax and Employee Benefit Deduction','Take Home'], tablefmt = "pretty",showindex = True, missingval = 'n/a'))
print()