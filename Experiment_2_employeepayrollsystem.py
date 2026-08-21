import customtkinter as ctk

#function to perform calculation
def calculate():
    try:
        number1=float(first_number_entry.get())
        number2=200

        result=number1*number2
        result_label.configure(text=f"Result: {result}")
    
    except ValueError:
        result_label.configure(text="please enter valid number:")


def clear_fields():
    first_number_entry.delete(0,"end")
    result_label.configure(text="result:")

#

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app=ctk.CTk()

app.title("")
app.geometry("500x500")


heading=ctk.CTkLabel(
    app,
    text="Employee Payroll System",
    font=("Arial",28,"bold")
)

heading.pack(pady=30)

first_number_label=ctk.CTkLabel(
    app,
    text="Enter how many hours worked:",
    font=("Arial",16)
)

first_number_label.pack(pady=(10,5))

first_number_entry=ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="Hours worked"
)
first_number_entry.pack(pady=5)

calculator_button=ctk.CTkButton(
    app,
    text="calculate",
    width=180,
    command=calculate
)
calculator_button.pack(pady=10)
clear_button=ctk.CTkButton(
    app,
    text="clear",
    width=180,
    command=clear_fields
)
clear_button.pack(pady=10)

result_label=ctk.CTkLabel(
    app,
    text="result:",
    font=("Arial",20,"bold")
)
result_label.pack(pady=25)
app.mainloop()