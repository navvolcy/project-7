class employee:

    def __init__(self,emp_nunm,emp_name, emp_add,emp_Wage, emp_hour):
        self.num = emp_nunm
        self.name = emp_name
        self.add = emp_add
        self.wage = float(emp_Wage)
        self.hour= float(emp_hour)

    def get_num(self):
        return self.num

    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.add
    
    def calc_pay(self):
        total = self.wage * self.hour
        deduct = total * .2
        state_tax = total * .075
        result = total - deduct - state_tax
        return result





employees = open('data.txt', 'r')

emp=[]

while True:
    emp_nunm = employees.readline()
    if emp_nunm == '':
        break 
    emp_name = employees.readline()
    emp_add = employees.readline()
    emp_Wage,emp_hour = employees.readline().split()

    emp.append(employee(emp_nunm,emp_name,emp_add,emp_Wage,emp_hour))


import tkinter as tk
from tkinter import ttk 

index =  0
def next_employ():
    global index
    index= index + 1
    name_name.delete(0,'end')
    name_name.insert(0,emp[index].get_name())
    name_address.delete(0,'end')
    name_address.insert(0,emp[index].get_address())
    name_netpay.delete(0,'end')
    name_netpay.insert(0,emp[index].calc_pay())


#Create the application window
name_window = tk.Tk()


# Create the user interface 

my_name = ttk.Label(name_window, text= "Name" )
my_address = ttk.Label(name_window, text= "Address")
my_netpay = ttk.Label(name_window,text= "NetPay")

next_person = ttk.Button(name_window, text= "Next", command=next_employ)

name_name = ttk.Entry(name_window)
name_address = ttk.Entry(name_window)
name_netpay = ttk.Entry(name_window)

name_name.delete('end')
name_name.insert(0,emp[0].get_name())
name_address.delete('end')
name_address.insert(0,emp[0].get_address())
name_netpay.delete('end')
name_netpay.insert(0,emp[0].calc_pay())



#what the user will see
my_name.grid(row = 1, column = 1, ipady= 12)
my_address.grid(row = 3, column = 1, ipady= 12)
my_netpay.grid(row = 5, column = 1)

next_person.grid(row = 7, column = 2, ipady= 10)

name_name.grid(row = 1, column = 2, ipady= 5)
name_address.grid(row= 3, column= 2, ipady= 5)
name_netpay.grid(row= 5, column= 2, ipady= 5)

name_window.mainloop() 
