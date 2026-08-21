import customtkinter as ctk

#function to perform calculation
def calculate():
    try:
        number1=float(first_number_entry.get())
        number2=float(second_number_entry.get())

        operation=operation_menu.get()

        if operation=="Addition":
            result=number1+number2

        elif operation=="Subtraction":
            result=number1-number2
            
        elif operation=="Multiplication":
            result=number1*number2
        
        elif operation=="Division":
            if number2==0:
                result_label.configure(text="cannot divide by zero")
                return

            result=number1/number2
        
        elif operation=="Modulus":
            result=number1%number2

        elif operation=="Exponentiation":
            result=number1**number2

        

        result_label.configure(text=f"Result: {result}")
    
    except ValueError:
        result_label.configure(text="please enter valid number:")


def clear_fields():
    first_number_entry.delete(0,"end")
    second_number_entry.delete(0,"end")
    operation_menu.set("Addition")
    result_label.configure(text="result:")

#

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app=ctk.CTk()

app.title("smart calculator")
app.geometry("5000x5000")


heading=ctk.CTkLabel(
    app,
    text="smart calculator by: Dhyey Raja",
    font=("Arial",28,"bold")
)

heading.pack(pady=30)

first_number_label=ctk.CTkLabel(
    app,
    text="enter first number:",
    font=("Arial",16)
)

first_number_label.pack(pady=(10,5))

first_number_entry=ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="First number"
)
first_number_entry.pack(pady=5)

second_number_label=ctk.CTkLabel(
    app,
    text="enter second number:",
    font=("Arial",16)
)

second_number_label.pack(pady=(20,5))

second_number_entry=ctk.CTkEntry(
    app,
    width=250,
    placeholder_text="second number"
)
second_number_entry.pack(pady=5)

operation_menu=ctk.CTkComboBox(
    app,
    width=250,
    values=[
        "Addition","Subtraction","Multiplication","Division","Modulus","Exponentiation"
    ]
)

operation_menu.set("Addition")
operation_menu.pack(pady=25)

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