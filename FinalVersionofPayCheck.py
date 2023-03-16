from tabulate import tabulate
from pprint import pprint as pp
from datetime import datetime as dt

#Print the Name of the Employee
def isNumber(name):
    return name.isnumeric()

if __name__ == "__main__":
    while True:
        # Saving the input in a string
        name = input("Enter the name: ")
        # Function returns true if st is number
        if isNumber(name):
            print("Enter a valid name. The name can only be in Alphabets")
        # Function returns false if st is not number
        else:
            pp('Enter more information')
            break

#Print the Startand End of the Employee
def date(start_date,end_date):
    return start_date, end_date

if __name__ == "__main__":
    while True:
        start_date = input("Enter a date when the pay period started (in the format MM/DD/YYYY) : ")
        end_date = input("Enter a date when the pay period started (in the format MM/DD/YYYY) : ")
        try:
            if date(start_date,end_date):
                date_object1 = dt.strptime(start_date, '%m/%d/%Y')
                sd = date_object1.strftime("%B %d, %Y")

                date_object2 = dt.strptime(end_date, '%m/%d/%Y')
                ed = date_object2.strftime("%B %d, %Y")
                break
        except ValueError:
                print(' ENTER THE VALID DATE FORMAT ====== MM/DD/YY.')
    
#Print the Gross Wage of the Employee
def isNumber(Gross_wages):
    return Gross_wages.isnumeric()

if __name__ == "__main__":
    while True:
        Gross_wages = input("Enter the gross wage of the employee: ")      
        try:
            if isNumber(Gross_wages):
                Gross_wages = int(Gross_wages) 
                
                if Gross_wages >= 100000:
                    Federal_Tax = 12000
                    State_Tax = 2200
                elif 90000 <= Gross_wages < 100000:
                    Federal_Tax = 10000
                    State_Tax = 2200
                elif 80000 <= Gross_wages < 90000:
                    Federal_Tax = 9000
                    State_Tax = 2200
                elif 70000 <= Gross_wages < 80000:
                    Federal_Tax = 8000
                    State_Tax = 2200
                elif 60000 <= Gross_wages < 70000:
                    Federal_Tax = 7000
                    State_Tax = 2200
                elif 50000 <= Gross_wages < 60000:
                    Federal_Tax = 5000
                    State_Tax = 2200
                        
                tax_deduction = Federal_Tax + State_Tax
                GW = Gross_wages - tax_deduction
                break     
            else:
                print("The Gross Wages can only be in range fromm $50,000 to $1,00,000")             
        except ValueError:
            print("Every employee in this company makes at least $50000 or more.")
            
##Print the Benefit of the Employee
def employee_benefits(benefits):
    return benefits

if __name__ == "__main__":
    while True:
        benefits = input("Is the Employee taking benefits (enter 'yes' for the employee benefit deduction) or (enter 'no')?:  ")        
        try:
            if benefits == "yes":
                while True:
#If the Employee choose option "yes", print which type of benefit employee is choosing
                    name_of_the_insurance = input("Which type of insurance employee is taking - premium || basic: ")
                    try:
                        if name_of_the_insurance == "premium":
                            cost_of_chosen_medical_benefit = 1440
                            Benefit_Deduction = tax_deduction + cost_of_chosen_medical_benefit
                            break
                        elif name_of_the_insurance == "basic":
                            cost_of_chosen_medical_benefit = 1200
                            Benefit_Deduction = tax_deduction + cost_of_chosen_medical_benefit
                            break
                        else:
                            print("Invalid input. Please enter either 'premium' or 'basic'.")
                    except ValueError:
                        print("Invalid input. Please enter the corect Medical policy - 'premium' or ''basic'. ")

#If the Employee choose option "no"
            elif benefits == "no":
                name_of_the_insurance == 'No Medical Benefit'
                cost_of_chosen_medical_benefit == 0
                Benefit_Deduction = tax_deduction + cost_of_chosen_medical_benefit
            else:
                print("Invalid input. Please enter either 'yes' or 'no'.")
                continue
                
            employee_benefits = Gross_wages - Benefit_Deduction
            Monthly_Paycheck = round(employee_benefits/12)
            Bi_weekely_Paycheck = round(Monthly_Paycheck/2)
            Weekely_Paycheck = round(Monthly_Paycheck/4)
            Hourly_Pay = round(Weekely_Paycheck/40)    
            print()
            break
            
        except ValueError:
            print("Only two options can be chosen: 'yes' if the employee has chosen medical benefits or 'no' if not.")
            

#Printing the information of the data in the Table (using 'tabulate' package)            
data1 = {'Name of the Employee':[name], 'Start Date' :[sd],'End Date':[ed], 'Gross Wage': [Gross_wages],'Tax Deduction': [tax_deduction],'Gross wage after tax deduction':[GW],
        'Insurance Policy':[name_of_the_insurance],'Cost of Chosen Medical Benefit': [cost_of_chosen_medical_benefit], 'Take Home':[employee_benefits],
        'Monthly Paycheck':[Monthly_Paycheck],'Bi-Weekely Paycheck':[Bi_weekely_Paycheck]}

print(tabulate(data1, headers =['Name', 'Start Date', 'End Date', 'Gross Wage','Tax Deduction','Gross wage after tax deduction','Insurance Policy',
                                'Cost of Chosen Medical Benefit','Take Home','Monthly Paycheck','Bi-Weekely Paycheck'], tablefmt = "pretty", showindex = True, missingval = 'N/A'))
