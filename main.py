import csv

# Define a class
class Expenditure:
    dept_name: str
    actual_expenditure: float

# Constructor for the class
    def __init__(self, dept_name,  actual_expenditure):
        self.dept_name = dept_name
        self. actual_expenditure =  actual_expenditure


# open / read CSV file and store expenditure objects in a list
with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    reader = csv.reader(file, delimiter=",")
    expenditure_list = []
    row_number = 1
    for list in reader:
        if row_number != 1:
           expenditure = Expenditure(list[0], list[3])
           expenditure_list.append(expenditure)
           row_number += 1
        else:
            row_number += 1

# key : dept_name, 2012 actual expense: list of expenditures for that department
expenditure_dict = {}
for item in expenditure_list:
    # if  actual_expenditure is empty, discard that value
    if item.actual_expenditure == '':
        continue

    temp_amt = int(item.actual_expenditure)

    # if key is NOT in the dictionary, 1st occurrence of the dept
    if not(item.dept_name in expenditure_dict):
        expenditure_dict[item.dept_name] = [temp_amt]
    else:
        expenditures = expenditure_dict[item.dept_name]
        expenditures.append(temp_amt)
        expenditure_dict[item.dept_name] = expenditures

print("City of Seattle: 2012 Actual Expense by Department\n")
# print(expenditure_dict)
print("Department: Sum" )
for department in expenditure_dict.keys():
    total_expenditures = sum(expenditure_dict.get(department))
    print("{0:11s} ${1:,.2f}".format(department, total_expenditures))



# key - dept_name, values - list of expenditures