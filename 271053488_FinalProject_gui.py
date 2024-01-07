import csv
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x300")
root.title("TG Enterprises")
lable = tk.Label(root, text="TG Enterprises", font=('Times New Roman', 25))
lable.pack()

function = tk.Label(root, text="Select a function", font=('Times New Roman', 16))
function.pack()

def car_rental():
    def calculate():
        rent_days = int(days.get())
        selected_car = car_table.selection()[0]
        price_per_day = car_table.item(selected_car, "values")[3]
        insurance_type = combo_insurance.get().upper()

        if insurance_type == "LIABILITY":
            insurance = int(car_table.item(selected_car, "values")[4])
        elif insurance_type == "COMPREHENSION":
            insurance = int(car_table.item(selected_car, "values")[5])

        simple_cost = int(price_per_day) * rent_days
        tax = 0.05 * simple_cost
        cost = simple_cost + insurance
        total = tax + simple_cost + insurance

        cost_label = tk.Label(rental_gui, text=f"Cost: {cost}", font=('Times New Roman', 16))
        cost_label.pack()
        tax_label = tk.Label(rental_gui, text=f"Tax: {tax}", font=('Times New Roman', 16))
        tax_label.pack()
        total_label = tk.Label(rental_gui, text=f"Total: {total}", font=('Times New Roman', 16))
        total_label.pack()

    def book():
        rent_days = int(days.get())
        temp = car_table.selection()[0]
        selected_car = int(car_table.item(temp, "values")[0]) - 1
        price_per_day = car_table.item(temp, "values")[3]
        insurance_type = combo_insurance.get().upper()

        if insurance_type == "LIABILITY":
            insurance = int(car_table.item(temp, "values")[4])
        elif insurance_type == "COMPREHENSION":
            insurance = int(car_table.item(temp, "values")[5])

        simple_cost = int(price_per_day) * rent_days
        tax = 0.05 * simple_cost

        cars_data[selected_car][2] = str(int(cars_data[selected_car][2]) - 1)  # decrements the availibiity
        # saves the total income, total insurance and total tax in csv file so that it can be used in third function
        cars_data[0][6] = int(cars_data[0][6]) + int(simple_cost)
        cars_data[1][6] = int(cars_data[1][6]) + int(insurance)
        cars_data[2][6] = int(cars_data[2][6]) + int(tax)

        # Opens file again in write mode to save the updated data

        with open("data.csv", "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(cars_data)

        booked_label = tk.Label(rental_gui, text=f"Car Booked!", font=('Times New Roman', 16))
        booked_label.pack()

    rental_gui = tk.Toplevel(root)
    root.geometry("500x300")
    root.title("Car Rental")
    select = tk.Label(rental_gui, text="Select a car:", font=('Times New Roman', 16))
    select.pack()
    with open("data.csv", "r") as csv_file:  # opens existing file for read
        csv_reader = csv.reader(csv_file)
        cars_data = list(csv_reader)  # saves it as list

    car_table = ttk.Treeview(rental_gui, columns=("No.","Model", "Available", "Price/Day", "Liability_Insurance/Day", "Comprehension_Insurance/Day"), show="headings")
    car_table.heading("No.", text="No.")
    car_table.heading("Model", text="Model")
    car_table.heading("Available", text="Available")
    car_table.heading("Price/Day", text="Price/Day")
    car_table.heading("Liability_Insurance/Day", text="Liability_Insurance/Day")
    car_table.heading("Comprehension_Insurance/Day", text="Comprehension_Insurance/Day")
    car_table.pack()

    for car in cars_data:
        if int(car[2]) > 0:
            car_table.insert("", tk.END,values=(car[0],car[1], car[2], car[3], car[4], car[5]))

    # entry for number of days the car gets rented
    days_label = tk.Label(rental_gui, text="Number of Days:", font=('Times New Roman', 15))
    days_label.pack()
    days = tk.Entry(rental_gui)
    days.pack()

    # choose b/w liability or comprehension insurance
    insurance_label = tk.Label(rental_gui, text="Select insurance:", font=('Times New Roman', 15))
    insurance_label.pack()
    combo_insurance = ttk.Combobox(rental_gui, values=["Liability", "Comprehension"])
    combo_insurance.pack()

    # button to calculate cost
    cost_button = tk.Button(rental_gui, text="Calculate", font=('Times New Roman', 15), command=calculate)
    cost_button.pack(padx=10, pady=10)
    # Button to Book a car
    book_button = tk.Button(rental_gui, text="Book?", font=('Times New Roman', 15),command=book)
    book_button.pack(padx=10, pady=10)

def car_return():
    return_gui = tk.Toplevel(root)
    root.geometry("500x300")
    root.title("Car Return")
    select = tk.Label(return_gui, text="Select a car:", font=('Times New Roman', 16))
    select.pack()
    with open("data.csv", "r") as csv_file:  # opens existing file for read
        csv_reader = csv.reader(csv_file)
        cars_data = list(csv_reader)  # saves it as list

    car_table = ttk.Treeview(return_gui, columns=("No.","Model"), show="headings")
    car_table.heading("No.", text="No.")
    car_table.heading("Model", text="Model")
    car_table.pack()

    for car in cars_data:
        car_table.insert("", tk.END,values=(car[0],car[1]))

    return_carno_label = tk.Label(return_gui, text="Enter Car No.:", font=('Times New Roman', 15))
    return_carno_label .pack()
    return_carno_entry  = tk.Entry(return_gui)
    return_carno_entry .pack()

    def returnal():
        return_option = int(return_carno_entry.get()) #to get value from entry

        with open("data.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            cars_data = list(csv_reader)

        if 0 < return_option <= len(cars_data): #checks if input is valid
            cars_data[return_option - 1][2] = str(int(cars_data[return_option - 1][2]) + 1)

            with open("data.csv", "w", newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerows(cars_data)
        returned_label = tk.Label(return_gui, text=f"Car Returned!", font=('Times New Roman', 16))
        returned_label.pack()

    car_return_btn = tk.Button(return_gui, text="Return Car", font=('Times New Roman', 15), command=returnal)
    car_return_btn.pack(padx=10, pady=10)

def print_all_totals():
    totals_gui = tk.Toplevel(root)
    root.geometry("500x300")
    root.title("Total Financial Details")

    with open("data.csv", "r") as csv_file:  # opens existing file for read
        csv_reader = csv.reader(csv_file)
        cars_data = list(csv_reader)  # saves it as list

    total_income_label = tk.Label(totals_gui, text="Total income: " + cars_data[0][6], font=('Times New Roman', 15))
    total_income_label.pack()

    total_insurance_label = tk.Label(totals_gui, text="Total insurance: " + cars_data[1][6], font=('Times New Roman', 15))
    total_insurance_label.pack()

    total_insurance_label = tk.Label(totals_gui, text="Total tax: " + cars_data[2][6], font=('Times New Roman', 15))
    total_insurance_label.pack()

rental_button = tk.Button(root, text="Car Rental", font=('Times New Roman', 15), command=car_rental)
rental_button.pack(padx=10, pady=10)


selected1_cars = tk.Label(root, text="Select Car:", font=('Times New Roman', 15))
selected1_cars = tk.Entry(root)

return_button = tk.Button(root, text="Car Return", font=('Times New Roman', 15),command=car_return)
return_button.pack(padx=10, pady=10)

totals_button = tk.Button(root, text="Total Finance Detail", font=('Times New Roman', 15),command=print_all_totals)
totals_button.pack(padx=10, pady=10)

root.mainloop()
