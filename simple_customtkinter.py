import customtkinter

def button_callback():
    print("Python is very high level language")

app=customtkinter.CTk()
app.title("Python Information")
app.geometry("400x150")

button=customtkinter.CTkButton(app, text="Introduction", command=button_callback)
button.grid(row=0,column=0,padx=20,pady=20)

app.mainloop()